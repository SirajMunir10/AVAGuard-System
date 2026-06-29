# Troubleshooting: BitLocker policy troubleshooting

**Domain:** Intune
**Subdomain:** BitLocker policy troubleshooting
**Incident Type:** Troubleshooting

## Scenario / Query
How to verify TPM status using PowerShell when troubleshooting BitLocker policy issues in Intune?

## Environment Context
- **Tenant Type:** Intune-managed Windows devices
- **Configuration:** BitLocker encryption policies

## Symptoms
- BitLocker cannot use the TPM
- TPM values set to False in Get-Tpm output

## Error Codes
N/A

## Root Causes
1. TPM not present, ready, enabled, activated, or owned

## Remediation Steps
1. Run PowerShell with administrator rights
2. Execute the Get-Tpm cmdlet
3. Check that TPM values equal True; if False, indicates a problem with the TPM

## Validation
Get-Tpm output shows TPM present and active with values equal True

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-bitlocker-policies>
