# Security Policies - Endpoint Security Lab

## Implemented Policies

### 1. Password Complexity Policy
**Enforcement Level:** Device-level via JumpCloud MDM

**Requirements:**
- Minimum length: 12 characters
- Character complexity:
  - At least 1 uppercase letter (A-Z)
  - At least 1 lowercase letter (a-z)
  - At least 1 number (0-9)
  - At least 1 special character (!@#$%^&*)
- Password expiration: 90 days
- Password history: Remember last 5 passwords
- Failed login lockout: 5 attempts
- Account lockout duration: 15 minutes

**Applied to:** All enrolled devices
**Compliance monitoring:** Automated via Python health scripts

### 2. Screen Lock Policy
**Enforcement Level:** Device-level via JumpCloud MDM

**Configuration:**
- Idle timeout: 5 minutes
- Lock on sleep: Immediate
- Require password on wake: Yes
- Lock screen message: "Property of [Organization Name]"
- Allow control center when locked: No

**Applied to:** All enrolled devices
**Platform-specific implementations:**
- macOS: System Preferences enforcement
- Linux: PAM module configuration

### 3. Full Disk Encryption Policy
**Enforcement Level:** Device-level via JumpCloud MDM

**Requirements:**
- Encryption algorithm: AES-256
- Recovery key escrow: JumpCloud console
- Pre-boot authentication: Required

**Platform-specific:**
- **macOS:** FileVault 2 enforcement
- **Linux:** LUKS encryption
- **Windows:** BitLocker (if applicable)

**Verification:** Encryption status reported to JumpCloud console
**Non-compliance action:** Device flagged in monitoring dashboard

## Policy Enforcement Workflow
```
Device Enrollment
       ↓
Policy Auto-Assignment
       ↓
Policy Application (5-10 mins)
       ↓
Compliance Verification (Python script)
       ↓
Monitoring Dashboard Update
       ↓
Non-Compliance Alert (if needed)
```

## Compliance Monitoring

Policies are monitored via:
1. JumpCloud console policy results API
2. Automated Python health monitoring scripts
3. Daily compliance reports
4. Real-time alerting for violations

## Audit Trail

All policy changes and compliance events are logged in:
- JumpCloud audit logs
- Python monitoring script logs
- Exported to compliance reports