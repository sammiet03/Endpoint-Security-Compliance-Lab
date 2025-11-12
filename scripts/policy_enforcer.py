#!/usr/bin/env python3
"""
JumpCloud Policy Compliance Checker
Verifies device compliance with organizational policies
SECURITY: Uses environment variables for API credentials
"""

import requests
import os
import sys
from dotenv import load_dotenv
from tabulate import tabulate

# Load environment variables
load_dotenv()

API_KEY = os.getenv('JUMPCLOUD_API_KEY')
BASE_URL = 'https://console.jumpcloud.com/api/v2'

if not API_KEY:
    print("❌ ERROR: JUMPCLOUD_API_KEY not found")
    sys.exit(1)

HEADERS = {
    'x-api-key': API_KEY,
    'Content-Type': 'application/json'
}

def get_all_policies():
    """Fetch all policies from JumpCloud"""
    try:
        response = requests.get(
            f'{BASE_URL}/policies',
            headers=HEADERS,
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching policies: {e}")
        return []

def get_policy_results():
    """Fetch policy compliance results"""
    try:
        response = requests.get(
            f'{BASE_URL}/policyresults',
            headers=HEADERS,
            timeout=10
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching policy results: {e}")
        return []

def analyze_compliance():
    """Analyze policy compliance across all devices"""
    print("\n" + "="*80)
    print("🛡️  JumpCloud Policy Compliance Report")
    print("="*80)
    
    policies = get_all_policies()
    policy_results = get_policy_results()
    
    if not policies:
        print("\n⚠️  No policies found")
        return
    
    print(f"\n📋 Active Policies: {len(policies)}")
    
    # Display policy summary
    table_data = []
    for policy in policies:
        table_data.append([
            policy.get('name', 'Unknown'),
            policy.get('template', {}).get('name', 'Custom'),
            '✓ Enabled' if policy.get('enabled') else '✗ Disabled'
        ])
    
    print(tabulate(
        table_data,
        headers=['Policy Name', 'Type', 'Status'],
        tablefmt='simple'
    ))
    
    # Compliance summary
    if policy_results:
        compliant = sum(1 for r in policy_results if r.get('status') == 'compliant')
        total = len(policy_results)
        print(f"\n✅ Compliance Rate: {compliant}/{total} checks passed")
    
    print("\n" + "="*80 + "\n")

if __name__ == "__main__":
    analyze_compliance()