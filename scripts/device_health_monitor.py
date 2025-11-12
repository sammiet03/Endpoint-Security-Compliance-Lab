#!/usr/bin/env python3
"""
JumpCloud Device Health Monitor
Monitors device compliance and health status
SECURITY: Uses environment variables for API credentials
"""

import requests
import os
import sys
from datetime import datetime, timedelta
from dotenv import load_dotenv
from tabulate import tabulate

# Load environment variables from .env file
load_dotenv()

# Configuration from environment variables
API_KEY = os.getenv('JUMPCLOUD_API_KEY')
BASE_URL = 'https://console.jumpcloud.com/api'

# Validate API key is set
if not API_KEY:
    print("❌ ERROR: JUMPCLOUD_API_KEY not found in environment variables")
    print("Please create a .env file with your API key")
    print("See .env.example for template")
    sys.exit(1)

# API Headers
HEADERS = {
    'x-api-key': API_KEY,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

def get_all_devices():
    """
    Fetch all devices from JumpCloud API
    Returns: List of device objects
    """
    try:
        response = requests.get(
            f'{BASE_URL}/systems',
            headers=HEADERS,
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        
        # Handle both list and dict responses
        if isinstance(data, dict):
            return data.get('results', [])
        return data if isinstance(data, list) else []
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching devices: {e}")
        return []

def check_device_health(device):
    """
    Evaluate device health and compliance
    Args:
        device: Device object from JumpCloud API
    Returns:
        Dictionary with health status and issues
    """
    # Ensure device is a dictionary
    if not isinstance(device, dict):
        return {
            'hostname': 'Unknown',
            'id': 'N/A',
            'os': 'Unknown',
            'agent_version': 'Unknown',
            'last_contact': None,
            'active': False,
            'healthy': False,
            'issues': ['Invalid device data format']
        }
    
    issues = []
    
    # Check last contact time
    last_contact = device.get('lastContact')
    if last_contact:
        try:
            # Parse ISO 8601 timestamp
            last_seen = datetime.fromisoformat(last_contact.replace('Z', '+00:00'))
            hours_since_contact = (datetime.now(last_seen.tzinfo) - last_seen).total_seconds() / 3600
            
            if hours_since_contact > 24:
                issues.append(f"No contact for {int(hours_since_contact)} hours")
        except Exception as e:
            issues.append("Invalid timestamp format")
    else:
        issues.append("Never contacted JumpCloud")
    
    # Check if device is active
    if not device.get('active', False):
        issues.append("Device marked inactive")
    
    # Check agent version
    agent_version = device.get('agentVersion', '')
    if not agent_version:
        issues.append("Agent version unknown")
    
    # Check if OS is recognized
    os_family = device.get('os', 'Unknown')
    if os_family == 'Unknown':
        issues.append("Operating system not detected")
    
    return {
        'hostname': device.get('hostname', device.get('displayName', 'Unknown')),
        'id': device.get('_id', device.get('id', 'N/A')),
        'os': f"{device.get('os', 'Unknown')} {device.get('version', '')}".strip(),
        'agent_version': agent_version if agent_version else 'N/A',
        'last_contact': last_contact,
        'active': device.get('active', False),
        'healthy': len(issues) == 0,
        'issues': issues
    }

def generate_health_report(devices_health):
    """
    Generate formatted health report
    Args:
        devices_health: List of device health status dictionaries
    """
    healthy_devices = [d for d in devices_health if d['healthy']]
    unhealthy_devices = [d for d in devices_health if not d['healthy']]
    
    print("\n" + "="*80)
    print(f"🔍 JumpCloud Device Health Report")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80)
    
    # Summary statistics
    total = len(devices_health)
    healthy_count = len(healthy_devices)
    health_percentage = (healthy_count / total * 100) if total > 0 else 0
    
    print(f"\n📊 Summary:")
    print(f"   Total Devices: {total}")
    print(f"   Healthy: {healthy_count} ({health_percentage:.1f}%)")
    print(f"   Need Attention: {len(unhealthy_devices)}")
    
    # Healthy devices table
    if healthy_devices:
        print(f"\n✅ Healthy Devices ({len(healthy_devices)}):")
        table_data = []
        for device in healthy_devices:
            table_data.append([
                device['hostname'],
                device['os'],
                device['agent_version'],
                '✓ Active' if device['active'] else '✗ Inactive'
            ])
        print(tabulate(
            table_data,
            headers=['Hostname', 'OS', 'Agent Version', 'Status'],
            tablefmt='simple'
        ))
    
    # Unhealthy devices with details
    if unhealthy_devices:
        print(f"\n⚠️  Devices Requiring Attention ({len(unhealthy_devices)}):")
        for device in unhealthy_devices:
            print(f"\n   🚨 {device['hostname']}")
            print(f"      OS: {device['os']}")
            print(f"      Issues:")
            for issue in device['issues']:
                print(f"         • {issue}")
    
    print("\n" + "="*80 + "\n")

def send_alerts(unhealthy_devices):
    """
    Send alerts for unhealthy devices
    In production: integrate with Slack, PagerDuty, email, etc.
    Args:
        unhealthy_devices: List of devices with issues
    """
    if not unhealthy_devices:
        return
    
    print("📧 Alert System:")
    print("   In production, alerts would be sent via:")
    print("   • Slack webhook")
    print("   • Email notifications")
    print("   • PagerDuty incidents")
    print(f"   • {len(unhealthy_devices)} devices need immediate attention")

def main():
    """Main execution function"""
    print("🚀 Starting JumpCloud Device Health Monitor...")
    
    # Fetch all devices
    devices = get_all_devices()
    
    if not devices:
        print("⚠️  No devices found or API error occurred")
        print("   Make sure:")
        print("   1. Your API key is correct in .env file")
        print("   2. You have devices enrolled in JumpCloud")
        print("   3. The API key has proper permissions")
        return
    
    # Check health of each device
    devices_health = []
    for device in devices:
        health_status = check_device_health(device)
        devices_health.append(health_status)
    
    # Generate report
    generate_health_report(devices_health)
    
    # Send alerts for unhealthy devices
    unhealthy = [d for d in devices_health if not d['healthy']]
    if unhealthy:
        send_alerts(unhealthy)
    else:
        print("✅ All devices are healthy - no alerts needed\n")

if __name__ == "__main__":
    main()