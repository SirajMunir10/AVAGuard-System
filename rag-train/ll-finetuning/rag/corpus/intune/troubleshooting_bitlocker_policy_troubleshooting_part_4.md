# Troubleshooting: BitLocker policy troubleshooting

**Domain:** Intune
**Subdomain:** BitLocker policy troubleshooting
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot BitLocker policy errors related to WinRE not being enabled?

## Environment Context
- **Tenant Type:** Intune-managed Windows devices
- **Configuration:** BitLocker encryption policies requiring WinRE

## Symptoms
- Error messages in the BitLocker-API about WinRe not being enabled

## Error Codes
N/A

## Root Causes
1. Windows Recovery Environment (WinRE) is disabled on the device

## Remediation Steps
1. Right-click on Start > Run, enter cmd
2. Right-click cmd and select Run as administrator
3. Run reagentc /info command to determine the WinRE status
4. If the WinRE status is disabled, run reagentc /enable command as an administrator to enable it manually

## Validation
Run reagentc /info command to confirm WinRE status is enabled

## Rollback
Run reagentc /disable command as an administrator to disable WinRE if needed

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-bitlocker-policies>
