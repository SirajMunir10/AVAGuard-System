# Troubleshooting: Device Registration

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to interpret the DeviceAuthStatus field in dsregcmd output to determine device health in Microsoft Entra ID?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Windows 10 May 2021 update (version 21H1) or later

## Symptoms
- DeviceAuthStatus shows FAILED. Device is either disabled or deleted
- DeviceAuthStatus shows FAILED. ERROR if the test was unable to run

## Error Codes
N/A

## Root Causes
1. Device is either disabled or deleted in Microsoft Entra ID
2. Test was unable to run due to lack of network connectivity to Microsoft Entra ID under the system context

## Remediation Steps
1. For FAILED. Device is either disabled or deleted: Refer to Microsoft Entra device management FAQ for more information about this issue
2. For FAILED. ERROR: Ensure network connectivity to Microsoft Entra ID under the system context

## Validation
DeviceAuthStatus shows SUCCESS if the device is present and enabled in Microsoft Entra ID

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-device-dsregcmd>
