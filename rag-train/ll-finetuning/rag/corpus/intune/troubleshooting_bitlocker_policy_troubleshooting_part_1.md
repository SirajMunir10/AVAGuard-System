# Troubleshooting: BitLocker policy troubleshooting

**Domain:** Intune
**Subdomain:** BitLocker policy troubleshooting
**Incident Type:** Troubleshooting

## Scenario / Query
How to manually sync a Windows device with Intune when the encryption report shows no actionable information?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** BitLocker encryption policies

## Symptoms
- Encryption report shows no actionable information

## Error Codes
N/A

## Root Causes
1. Device may not have synced recently with Intune service

## Remediation Steps
1. On the Windows device, select Settings > Accounts > Access work or school > Select your work or school account > Info
2. Under Device sync status, select Sync

## Validation
After the sync is complete, continue to the following sections in the documentation to gather data from the affected device.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-bitlocker-policies>
