# Troubleshooting: Windows Autopilot (0x80180014)

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve 0x80180014 error when redeploying a device in Windows Autopilot self-deployment mode or pre-provisioning mode?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Windows Autopilot self-deployment mode or pre-provisioning mode

## Symptoms
- Device fails with a 0x80180014 error code when rerunning Windows Autopilot deployment

## Error Codes
- `0x80180014`

## Root Causes
1. Device record in Intune was not deleted before redeploying the device

## Remediation Steps
1. Delete the device record in Intune, and then redeploy the device so that it reruns the Windows Autopilot deployment. For more information, see Deregister a device.
2. Remove the device enrollment restriction for Windows (MDM) personally owned devices. For more information, see Set enrollment restrictions in Microsoft Intune.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/autopilot/known-issues>
