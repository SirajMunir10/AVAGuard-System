# Troubleshooting: Windows Autopilot Enrollment (0x800705b4)

**Domain:** Intune
**Subdomain:** Windows Autopilot Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Windows Autopilot self-deploying mode enrollment failure with error 0x800705b4: Securing your hardware failed?

## Environment Context
- **Tenant Type:** Microsoft Entra ID (Azure AD) tenant with Intune
- **Configuration:** Windows Autopilot self-deploying mode; Microsoft Entra hybrid join may be used

## Symptoms
- Error message: Securing your hardware (Failed: 0x800705b4)
- Subsequent steps fail: Joining your organization's network (Previous step failed), Registering your device for mobile management (Previous step failed)

## Error Codes
- `0x800705b4`

## Root Causes
1. The targeted Windows device does not have a physical TPM 2.0 chip. Devices with virtual TPMs (e.g., Hyper-V VMs) or TPM 1.2 chips do not work with self-deploying mode.
2. The device is not running a supported version of Windows: Windows 10 build 1709 or later (or Windows 10 build 1809 or later if Microsoft Entra hybrid join is used).

## Remediation Steps
1. Ensure the targeted device has a physical TPM 2.0 chip.
2. Ensure the device is running Windows 10 build 1709 or later (or Windows 10 build 1809 or later if Microsoft Entra hybrid join is used).

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-windows-enrollment-errors>
