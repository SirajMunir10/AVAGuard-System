# Troubleshooting: Windows Enrollment (0x801C03EA)

**Domain:** Intune
**Subdomain:** Windows Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Windows enrollment error 0x801C03EA (Failed: 3) related to TPM chip version and Autopilot profile conflicts?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Windows Autopilot deployment

## Symptoms
- Registering your device for mobile management (Failed: 3, 0x801C03EA)

## Error Codes
- `0x801C03EA`
- `3`

## Root Causes
1. The device has a TPM chip that supports version 2.0, but hasn't yet been upgraded to version 2.0.
2. The same device is in two assigned groups, with each group being assigned a different Autopilot profile.

## Remediation Steps
1. Upgrade the TPM chip to version 2.0.
2. If the issue persists, check whether the same device is in two assigned groups, with each group being assigned a different Autopilot profile.
3. If it is in two groups, determine which Autopilot profile should be applied to the device, and then remove the other profile's assignment.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-windows-enrollment-errors>
