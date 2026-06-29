# Incident Response: Identity Protection (TI_RI_####)

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Incident Response

## Scenario / Query
How to investigate a Microsoft Entra threat intelligence risk detection when the detection was triggered by a real-time rule?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Identity Protection risk detection

## Symptoms
- Detection was triggered by a real-time rule

## Error Codes
- `TI_RI_####`

## Root Causes
1. Novel attacks identified by Microsoft's threat intelligence research

## Remediation Steps
1. Validate that no other users in your directory are targets of the same attack
2. Use the TI_RI_#### number assigned to the rule to find information
3. If multiple users in your directory were targets of the same attack, investigate unusual patterns in other attributes of the sign-in

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk>
