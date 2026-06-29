# Troubleshooting: Attack Surface Reduction Rules (VirtualAllocEx failed: 5)

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction Rules
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot issues with Quest Dirsync Password Sync when the ASR rule 'Block credential stealing from the Windows local security authority subsystem' is enabled?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** ASR rule GUID: 9e6c4e1f-7d60-472f-ba1a-a39ef669e4b2; Known issue with Quest Dirsync Password Sync

## Symptoms
- Dirsync Password Sync is not working when Windows Defender is installed
- Error: 'VirtualAllocEx failed: 5' (4253914)

## Error Codes
- `VirtualAllocEx failed: 5`

## Root Causes
1. The ASR rule blocks access to LSASS process memory, which is required by Quest Dirsync Password Sync

## Remediation Steps
1. Refer to Microsoft support article: Dirsync Password Sync isn't working when Windows Defender is installed, error: 'VirtualAllocEx failed: 5' (4253914)
2. Consider adding Quest Dirsync to the ASR rule exclusion list if necessary

## Validation
Verify that Dirsync Password Sync functions correctly after applying exclusion or adjusting configuration

## Rollback
Remove the exclusion for Quest Dirsync if it was added

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
