# Hardening: Attack Surface Reduction Rules

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction Rules
**Incident Type:** Hardening

## Scenario / Query
How to block Office applications from injecting code into other processes using ASR rule GUID 75668c1f-73b5-4cf0-bb93-3ecf5cb7cc84?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Microsoft Defender Antivirus dependency; no Warn mode support; applies to Word, Excel, OneNote, PowerPoint; requires restart of Microsoft 365 Apps

## Symptoms
- Code injection attempts from Office apps into other processes
- Malicious code masquerading as a clean process

## Error Codes
N/A

## Root Causes
1. Office applications allowed to inject code into other processes

## Remediation Steps
1. Enable ASR rule 'Block Office applications from injecting code into other processes' with GUID 75668c1f-73b5-4cf0-bb93-3ecf5cb7cc84 via Intune or Configuration Manager
2. Use Microsoft Intune name: Block Office applications from injecting code into other processes
3. Use Microsoft Configuration Manager name: Block Office applications from injecting code into other processes
4. Restart Microsoft 365 Apps (Office applications) for configuration changes to take effect

## Validation
Monitor Advanced hunting action types: AsrOfficeProcessInjectionAudited or AsrOfficeProcessInjectionBlocked

## Rollback
Disable the ASR rule or configure exclusions per File and folder exclusions for ASR rules documentation

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
