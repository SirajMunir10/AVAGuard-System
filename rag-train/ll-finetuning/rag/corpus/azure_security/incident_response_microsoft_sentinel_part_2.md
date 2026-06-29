# Incident Response: Microsoft Sentinel

**Domain:** Azure
**Subdomain:** Microsoft Sentinel
**Incident Type:** Incident Response

## Scenario / Query
A security analyst notices an incident in Microsoft Sentinel labeled 'Solorigate Network Beacon' with high severity. The incident involves a compromised on-premises server communicating with a known C2 domain. How should the analyst triage, investigate, and contain this incident using Microsoft Sentinel and Microsoft 365 Defender?

## Environment Context
- **Tenant Type:** Enterprise (hybrid identity, Azure AD, Microsoft 365 E5, Microsoft Sentinel enabled)
- **Configuration:** Microsoft Sentinel is connected to Azure AD, Azure Activity Logs, Microsoft 365 Defender, and Windows Security Events from on-premises servers via Azure Arc. Analytic rule 'Solorigate Network Beacon' is enabled.

## Symptoms
- Microsoft Sentinel incident created with title 'Solorigate Network Beacon'
- Alert details show outbound network connection from on-premises server to suspicious IP address 185.220.101.45
- User account on the server shows anomalous logon times and lateral movement attempts
- Microsoft 365 Defender portal shows related alerts for the same entity

## Error Codes
N/A

## Root Causes
1. On-premises server was compromised via a phishing email that delivered a malicious payload
2. The payload established persistence and beaconed to a command-and-control server
3. The attacker used compromised credentials to move laterally within the environment

## Remediation Steps
1. 1. Open the incident in Microsoft Sentinel and review the full timeline and related alerts.
2. 2. Use the 'Investigation' graph to identify all impacted entities (user, device, IP).
3. 3. Isolate the compromised server using Microsoft Defender for Endpoint: run 'Investigate - Isolate device' from the device page.
4. 4. Reset the compromised user's password and revoke all refresh tokens in Azure AD.
5. 5. Block the C2 IP address in Azure Firewall or network security group.
6. 6. Run a full antivirus scan on the isolated server using Microsoft Defender Antivirus.
7. 7. Enable 'Account Protection' and 'Conditional Access' policies to require MFA for all users.
8. 8. Review and apply the Microsoft Sentinel 'Solorigate' detection rule tuning guidance.

## Validation
Confirm that the isolated server no longer shows outbound connections to the C2 IP. Verify that the user account has no active sessions. Run a simulated attack test to ensure detection rules fire correctly.

## Rollback
If isolation causes business disruption, remove the device from isolation via Microsoft Defender for Endpoint. Restore user access after password reset and MFA enrollment. Remove IP block after confirming no further malicious traffic.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/investigate-incidents>
- <https://learn.microsoft.com/en-us/azure/sentinel/tutorial-investigate-incidents>
