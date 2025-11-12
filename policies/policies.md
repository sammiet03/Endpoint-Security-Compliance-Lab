# Creating Policies in JumpCloud
### Policy 1: Password Policy

1. Navigate to Policy Management:
- Click "Device Management" (left sidebar)
Click "Policy Management"

2. Create New Password Policy:
- Click "+ Add Policy" or "New" button (top right)
- Policy Type: Select "macOS" or "Linux" (depending on your devices)
- Template: Choose "Password" or "Password Requirements"

3. Configure Settings:
```
Policy Name: Password Policy - Lab
Settings:
✓ Minimum password length: 12
✓ Require at least 1 uppercase letter
✓ Require at least 1 lowercase letter  
✓ Require at least 1 number
✓ Require at least 1 special character
✓ Password expiration: 90 days
✓ Remember password history: 5 passwords
```

4. Apply to Devices:
- Under "Apply To" or "Device Groups"
- Select your enrolled devices
- Click Save


### Policy 2: Screen Lock in Policy 
1. Create New Policy: 
- Still in Policy Management
- Click "+ Add Policy" again

2. Select Template:
- Choose "Login Window" (macOS) or "Screen Lock" (Linux)

3. Configure:
```
Policy Name: Screen Lock Policy - Lab   
Settings:
✓ Require password after sleep or screen saver: Immediately
✓ Start screen saver after: 5 minutes of inactivity
✓ Show message on lock screen (optional)
```

### Policy 3: Disk Encryption (macOS)
- Since we are on Mac, you'll use FileVault instead of BitLocker:

1. Create New Policy:
- Policy Management → + Add Policy

2. Select Template:
- Choose "FileVault" or "Full Disk Encryption"

3. Configure:
```
Policy Name: Disk Encryption - Lab
Settings:
✓ Enable FileVault
✓ Escrow recovery key to JumpCloud
```
4. Apply and Save 
