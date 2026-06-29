# Troubleshooting: Microsoft Defender Antivirus (Error Code: Error code Result code associated with threat status. Standard HRESULT values.)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Event ID 2004 (MALWAREPROTECTION_SIGNATURE_REVERSION) indicating a problem loading antimalware definitions in Microsoft Defender Antivirus?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Event ID 2004 with symbolic name MALWAREPROTECTION_SIGNATURE_REVERSION is logged
- Message: There was a problem loading antimalware definition. The antimalware engine attempts to load the last-known good set of definitions.
- Microsoft Defender Antivirus encountered an error trying to load signatures and will attempt reverting back to a known-good set of signatures.

## Error Codes
- `Error Code: Error code Result code associated with threat status. Standard HRESULT values.`
- `Error Description: Error description Description of the error.`

## Root Causes
1. The Microsoft Defender Antivirus client attempted to download and install the latest definitions file and failed.
2. This error can occur when the client encounters an error while trying to load the definitions, or if the file is corrupt.

## Remediation Steps
1. Restart the computer and try again.
2. Download the latest definitions from the Microsoft Security Intelligence site. Note: The size of the definitions file downloaded from the site can exceed 60 MB and shouldn't be used as a long-term solution for updating definitions.
3. Contact Microsoft Technical Support.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
