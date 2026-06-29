# Troubleshooting: Hybrid Identity

**Domain:** Entra ID
**Subdomain:** Hybrid Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to monitor Authentication Agents using Performance Monitor counters for Pass-through Authentication?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Pass-through Authentication with multiple Authentication Agents

## Symptoms
- Authentication Agent receives no traffic at all
- Uneven distribution of authentication requests among Authentication Agents

## Error Codes
N/A

## Root Causes
1. Pass-through Authentication provides high availability using multiple Authentication Agents, and not load balancing
2. Depending on configuration, not all Authentication Agents receive roughly equal number of requests

## Remediation Steps
1. Track specific Performance Monitor counters on each server where the Authentication Agent is installed
2. Use Global counters: # PTA authentications, #PTA failed authentications, #PTA successful authentications
3. Use Error counters: # PTA authentication errors

## Validation
On each server with the Pass-through Authentication Agent installed, open Performance Monitor (perfmon.msc). Add the following counters under the 'Pass-through Auth' object: '# PTA authentications', '# PTA failed authentications', '# PTA successful authentications', and '# PTA authentication errors'. Observe the counters over a period of at least 5–10 minutes while user authentication requests are occurring. Confirm that '# PTA authentications' increments on each server, indicating the agent is receiving traffic. Verify that '# PTA successful authentications' and '# PTA failed authentications' sum to the total authentications, and that '# PTA authentication errors' remains low or zero. If counters show zero on a server, that agent is not receiving requests.

## Rollback
If the monitoring reveals an agent is not receiving traffic or counters are unexpectedly zero, review the agent registration status by running the PowerShell cmdlet `Get-PassThroughAuthenticationAgent` on the server. If the agent is not listed as 'Active', re-register it using the steps in the Pass-through Authentication agent installation guide. If counters show excessive errors, restart the agent service (Microsoft Azure AD Connect Authentication Agent) via Services.msc. If the issue persists, uninstall and reinstall the Authentication Agent from the server, then re-run the validation steps to confirm traffic distribution.

## References
- <https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/tshoot-connect-pass-through-authentication>
