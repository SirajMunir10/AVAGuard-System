# Hardening: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Hardening

## Scenario / Query
How to restrict app execution on a device to contain an attack and prevent malicious programs from running?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Devices on Windows 10 version 1709 or later, Windows 11, Windows Server 2019 or later; Microsoft Defender Antivirus enabled; Windows Defender Application Control code integrity policy formats and signing requirements

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. On the device page, select Restrict app execution.
2. Type a comment and select Confirm.

## Validation
The Action center shows the scan information and the device timeline includes a new event.

## Rollback
To reverse the restriction, select Remove app restrictions on the device page and follow the same steps as restricting app execution.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
