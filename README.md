# Endpoint Security & Compliance Lab

Automated MDM deployment and device lifecycle management using JumpCloud with Python automation for compliance monitoring and policy enforcement.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![JumpCloud](https://img.shields.io/badge/JumpCloud-MDM-green.svg)](https://jumpcloud.com)

## 🎯 Project Overview

This lab demonstrates enterprise endpoint management and security automation using:
- **MDM Platform**: JumpCloud for centralized device management
- **Monitored Endpoints**: Windows, Linux, and macOS devices
- **Automation**: Python scripts for health monitoring and compliance checking
- **Security**: Zero-trust device verification and policy-based compliance

## 🏗️ Architecture
```
┌─────────────────────────────────────────────────────────────┐
│                    JumpCloud Console                        │
│          (Policies, Users, Device Management)               │
└───────────────────┬─────────────────────────────────────────┘
                    │
        ┌───────────┴───────────┬────────────────┐
        │                       │                │
    ┌───▼────┐            ┌────▼─────┐     ┌───▼─────┐
    │Windows │            │  Linux   │     │  macOS  │
    │  VM    │            │   VM     │     │   VM    │
    └───┬────┘            └────┬─────┘     └───┬─────┘
        │                      │               │
        └──────────────┬───────┴───────────────┘
                       │
              ┌────────▼────────-─┐
              │  Python Scripts   │
              │  • Health Monitor │
              │  • Policy Check   │
              │  • Alerting       │
              └──────────────────-┘
```

## ✨ Features

### Device Lifecycle Management
- ✅ Automated device enrollment and provisioning
- ✅ Continuous compliance monitoring
- ✅ Policy enforcement across all endpoints
- ✅ Streamlined offboarding and retirement workflows

### Security & Compliance
- 🔒 Password complexity enforcement
- 🔒 Full disk encryption requirements
- 🔒 Screen lock policies
- 🔒 Zero-trust device verification
- 🔒 Automated compliance reporting

### Automation & Monitoring
- 🤖 Real-time device health checks
- 🤖 Policy compliance verification
- 🤖 Automated alert generation
- 🤖 Integration-ready (Slack, PagerDuty, email)

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- JumpCloud account ([free trial available](https://jumpcloud.com))
- pip package manager

### Installation

1. **Clone the repository**
   ```
   git clone https://github.com/sammiet03/endpoint-security-lab.git
   cd endpoint-security-lab
   ```

2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   ```
   cp .env.example .env
   - Edit .env and add your JumpCloud API key
   ```

4. **Run device health monitor**
   ```
   python scripts/device_health_monitor.py
   ```

## 📁 Project Structure
```
endpoint-security-lab/
├── scripts/
│   ├── device_health_monitor.py    # Main health monitoring script
│   └── policy_enforcer.py          # Policy compliance checker
├── docs/
│   ├── device_lifecycle.md         # Lifecycle management documentation
│   └── setup_guide.md              # Detailed setup instructions
├── policies/
│   └── README.md                   # Policy templates and examples
├── screenshots/
│   └── README.md                   # Lab screenshots
├── .env.example                    # Environment variable template
├── .gitignore                      # Git ignore rules (security)
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## 🔧 Configuration

### JumpCloud API Setup

1. Log into [JumpCloud Console](https://console.jumpcloud.com)
2. Navigate to your profile → "My API Key"
3. Generate a new API key
4. Add to `.env` file:
   ```
   JUMPCLOUD_API_KEY=your_api_key_here
   ```

### Device Enrollment

See [Setup Guide](docs/setup_guide.md) for detailed enrollment instructions.

## 📊 Example Output

### Device Health Monitor
```
🔍 JumpCloud Device Health Report
Generated: 2025-01-15 14:30:22
================================================================================

📊 Summary:
   Total Devices: 5
   Healthy: 4 (80.0%)
   Need Attention: 1

✅ Healthy Devices (4):
Hostname           OS                    Agent Version    Status
-----------------  --------------------  ---------------  --------
JC-Windows-01      Windows 11 Pro        1.182.0          ✓ Active
JC-Ubuntu-01       Ubuntu 22.04 LTS      1.182.0          ✓ Active
JC-MacBook-01      macOS 14.2            1.182.0          ✓ Active
JC-Linux-Server    Debian 12             1.182.0          ✓ Active

⚠️  Devices Requiring Attention (1):

   🚨 JC-Windows-02
      OS: Windows 10 Pro
      Issues:
         • No contact for 26 hours
         • Device marked inactive
```

## 🛡️ Security Policies Implemented

| Policy | Description | Platforms |
|--------|-------------|-----------|
| Password Complexity | 12+ chars, complexity required | All |
| Disk Encryption | Full disk encryption mandatory | All |
| Screen Lock | 5-minute idle timeout | All |
| OS Updates | Automatic security updates | All |

## 📚 Documentation

- [Device Lifecycle Management](docs/device_lifecycle.md)
- [Setup Guide](docs/setup_guide.md)
- [Policy Templates](policies/README.md)

## 🔐 Security Notes

- Never commit `.env` files or API keys to version control
- Rotate API keys regularly (every 90 days minimum)
- Use least privilege access for API keys
- Enable MFA on your JumpCloud admin account
- Review audit logs regularly

## 🛠️ Technologies Used

- **MDM**: JumpCloud
- **Languages**: Python 3.8+
- **Libraries**: requests, python-dotenv, tabulate
- **APIs**: JumpCloud REST API v1 & v2
- **Security**: Environment-based credential management

## 📈 Skills Demonstrated

- Mobile Device Management (MDM) implementation
- Identity and Access Management (IAM)
- Python automation and API integration
- Security policy enforcement
- Infrastructure as Code principles
- DevOps/SRE practices
- Documentation and knowledge sharing
