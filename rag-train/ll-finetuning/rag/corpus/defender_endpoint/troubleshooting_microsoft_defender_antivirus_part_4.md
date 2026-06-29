# Troubleshooting: Microsoft Defender Antivirus (Error Code: Error code Result code associated with threat status. Standard HRESULT values.)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Event ID 2001: Security intelligence update failed in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 2001 with symbolic name MALWAREPROTECTION_SIGNATURE_UPDATE_FAILED
- Message: The security intelligence update failed

## Error Codes
- `Error Code: Error code Result code associated with threat status. Standard HRESULT values.`

## Root Causes
1. Problem updating definitions

## Remediation Steps
1. Update definitions and force a rescan directly on the endpoint.
2. Review the entries in the %Windir%\WindowsUpdate.log file for more information about this error.
3. Contact Microsoft Technical Support.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
