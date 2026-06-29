# Incident Response: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Incident Response

## Scenario / Query
How to investigate user risk using other security tools like Microsoft Sentinel or Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** Entra ID tenant with Microsoft Sentinel or Microsoft Defender XDR integrated
- **Configuration:** N/A

## Symptoms
- User risk event detected in Identity Protection

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. If you have Microsoft Sentinel, check for corresponding alerts that might indicate a larger issue
2. If you have Microsoft Defender XDR, follow a user risk event through other related alerts and incidents
3. Use the MITRE ATT&CK chain through Microsoft Sentinel in Microsoft Defender XDR for insights
4. In the Microsoft Defender portal, browse to Incidents & alerts > Alerts > and set the Product name filter to AAD Identity Protection to find alerts from Microsoft Entra ID Protection

## Validation
1. In the Microsoft Defender portal (https://security.microsoft.com), navigate to Incidents & alerts > Alerts. Set the Product name filter to 'AAD Identity Protection' and verify that alerts corresponding to the user risk event are listed. 2. In Microsoft Sentinel, run a query such as: IdentityProtection_UserRiskEvents_CL | where TimeGenerated > ago(24h) | summarize count() by UserPrincipalName, RiskLevel. Confirm that the user risk event appears and matches the Identity Protection detection. 3. In Microsoft Defender XDR, open the incident related to the user and review the MITRE ATT&CK chain to ensure the user risk event is linked to other related alerts or incidents.

## Rollback
1. If the validation steps reveal missing or incorrect alerts, re-run the Identity Protection risk investigation from the Microsoft Entra admin center (https://entra.microsoft.com) under Identity Protection > Risky users. 2. If Sentinel queries return no results, verify that the Identity Protection data connector is enabled and properly configured in Sentinel. 3. If Defender XDR incidents are not linked, manually create a new incident in the Microsoft Defender portal by selecting 'Create incident' and adding the relevant user risk alert from AAD Identity Protection.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk>
