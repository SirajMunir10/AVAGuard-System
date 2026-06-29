# Hardening: Attack Surface Reduction Rules

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction Rules
**Incident Type:** Hardening

## Scenario / Query
How to block Office applications from creating executable content using ASR rule GUID 3b576869-a4ec-4529-8536-b80a7769e899?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Microsoft Defender Antivirus, RPC dependencies; limited exclusion support

## Symptoms
- Malicious components survive computer reboot and persist on the system
- Untrusted files saved by Office macros are executed

## Error Codes
N/A

## Root Causes
1. Office applications allowed to create executable content from untrusted macros

## Remediation Steps
1. Enable ASR rule 'Block Office applications from creating executable content' with GUID 3b576869-a4ec-4529-8536-b80a7769e899 via Intune or Configuration Manager
2. Use Microsoft Intune name: Block Office applications from creating executable content
3. Use Microsoft Configuration Manager name: Block Office applications from creating executable content

## Validation
Monitor Advanced hunting action types: AsrExecutableOfficeContentAudited or AsrExecutableOfficeContentBlocked

## Rollback
Disable the ASR rule or configure exclusions per File and folder exclusions for ASR rules documentation

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
