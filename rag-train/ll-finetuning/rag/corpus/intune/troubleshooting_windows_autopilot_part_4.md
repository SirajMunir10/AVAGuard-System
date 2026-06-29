# Troubleshooting: Windows Autopilot (0x80180014)

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Windows Autopilot OOBE enrollment failure due to MDM enrollment restrictions blocking Windows (MDM) platform?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Enrollment restrictions for Windows (MDM) platform

## Symptoms
- Error 0x80180014 during Autopilot OOBE
- ETW logs show: MDM Enroll: Server Returned Fault/Code/Subcode/Value=(DeviceNotSupported) Fault/Reason/Text=(Enrollment blocked for AP device by SDM One Time Limit Check)

## Error Codes
- `0x80180014`

## Root Causes
1. Windows (MDM) platform set to Block in enrollment restrictions
2. Device is a member of a group where MDM enrollment is blocked

## Remediation Steps
1. Navigate to All Users screen, under Manage select Properties.
2. In Properties screen, next to Platform settings select the Edit link.
3. In Edit restriction screen, locate Windows (MDM) under the Type column.
4. Ensure Windows (MDM) is set to Allow under the Platform column. If set to Block, change it to Allow.
5. Select Review + save, then either Save if a setting was changed, or Cancel if no settings were changed.
6. Repeat the above steps for any additional restrictions that might exist in the Enrollment restrictions screen other than All Users. Only restrictions for the Windows platform need to be verified.
7. If multiple restrictions exist, verify the device is not a member of a group where MDM enrollment is blocked. Alternatively, change the MDM enrollment setting for that restriction to Allow.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
