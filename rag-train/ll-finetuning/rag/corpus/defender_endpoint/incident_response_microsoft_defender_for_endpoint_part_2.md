# Incident Response: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Incident Response

## Scenario / Query
How do I contain a compromised user identity from the network using Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Supported Microsoft Defender for Endpoint onboarded devices

## Symptoms
- Identity in the network might be compromised
- Potential ransomware attack

## Error Codes
N/A

## Root Causes
1. Compromised identity accessing the network and different endpoints

## Remediation Steps
1. Contain the identity using Defender for Endpoint to block it from access
2. Block incoming traffic in specific protocols related to attacks (deny network logons, RPC, SMB, RDP)
3. Terminate ongoing remote sessions
4. Logoff existing RDP connections (terminating the session itself including all its related processes)
5. Enable legitimate traffic while blocking attack-related protocols

## Validation
N/A

## Rollback
Once contained by automatic attack disruption, a user is automatically removed from containment in the next five days.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
