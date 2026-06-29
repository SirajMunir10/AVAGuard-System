# Troubleshooting: BitLocker policy troubleshooting

**Domain:** Intune
**Subdomain:** BitLocker policy troubleshooting
**Incident Type:** Troubleshooting

## Scenario / Query
How to diagnose TPM issues when BitLocker silent encryption fails in Intune?

## Environment Context
- **Tenant Type:** Intune-managed Windows devices
- **Configuration:** BitLocker policy requiring TPM for silent encryption

## Symptoms
- BitLocker silent encryption fails
- TPM errors in BitLocker-API and system event logs

## Error Codes
N/A

## Root Causes
1. TPM is missing or unhealthy
2. TPM is disabled in the BIOS

## Remediation Steps
1. Open TPM.msc by entering 'tpm.msc' in the Search box and selecting 'Run as administrator'
2. Check the TPM status: verify specification version (e.g., 2.0) and that status is 'ready for use'
3. If TPM is disabled in BIOS, enable it in the BIOS settings

## Validation
After enabling TPM in BIOS, verify TPM.msc shows 'ready for use' status and retry BitLocker encryption

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-bitlocker-policies>
