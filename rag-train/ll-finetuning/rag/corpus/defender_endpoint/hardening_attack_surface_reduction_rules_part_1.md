# Hardening: Attack Surface Reduction Rules

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction Rules
**Incident Type:** Hardening

## Scenario / Query
How to configure and deploy the ASR rule 'Block credential stealing from the Windows local security authority subsystem' when Credential Guard or LSA protection cannot be enabled?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** ASR rule GUID: 9e6c4e1f-7d60-472f-ba1a-a39ef669e4b2; Microsoft Intune name: Block credential stealing from the Windows local security authority subsystem; Microsoft Configuration Manager name: Block credential stealing from the Windows local security authority subsystem

## Symptoms
- Large volume of audit events from ASR rule, most safe to ignore in Block mode
- Blocking of processes like svchost.exe from accessing LSASS process memory
- Event log entries in Security log in Windows Event Viewer for denied open process actions

## Error Codes
N/A

## Root Causes
1. Cannot enable Credential Guard due to compatibility issues with custom smartcard drivers or other programs that load into the LSA
2. Cannot enable LSA protection
3. Attackers can use tools like Mimikatz to scrape cleartext passwords and NTLM hashes from LSASS

## Remediation Steps
1. Configure the ASR rule with GUID 9e6c4e1f-7d60-472f-ba1a-a39ef669e4b2 in Block mode
2. Skip audit mode evaluation and proceed to block mode deployment
3. Start with a small set of devices and gradually expand to cover the rest
4. Do not add apps that simply enumerate LSASS to the exclusion list unless they affect functionality
5. Note: This rule does not support Warn mode
6. Note: This rule has limited exclusion support; see File and folder exclusions for ASR rules

## Validation
Monitor for AsrLsassCredentialTheftBlocked events in Advanced hunting; verify that LSASS process memory access is blocked for unauthorized processes

## Rollback
Disable the ASR rule by setting it to Disabled mode in Intune or Configuration Manager

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
