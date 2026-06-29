# Incident Response: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Incident Response

## Scenario / Query
How to investigate a risky sign-in in Microsoft Entra ID Protection?

## Environment Context
- **Tenant Type:** Entra ID tenant with Identity Protection enabled
- **Configuration:** N/A

## Symptoms
- User or sign-in flagged as risky in Identity Protection

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Contact the user to confirm if they recognize the sign-in; however, keep in mind that email or Teams might be compromised.
2. Confirm the information you have such as: Timestamp, Application, Device, Location, IP address.
3. Depending on the results of the investigation, mark the user or sign-in as confirmed compromised, confirmed safe, or dismiss the risk.
4. You can confirm compromise in the Microsoft Entra admin center or programmatically using Microsoft Graph.
5. Set up risk-based Conditional Access policies to prevent similar attacks or to address any gaps in coverage.

## Validation
1. In the Microsoft Entra admin center, navigate to Protection > Identity Protection > Risky sign-ins. 2. Locate the specific risky sign-in by filtering on the user, timestamp, application, device, location, or IP address. 3. Confirm that the risk state has been updated to 'Confirmed compromised', 'Confirmed safe', or 'Dismissed' as appropriate. 4. Optionally, use Microsoft Graph to verify the risk state: GET https://graph.microsoft.com/v1.0/identityProtection/riskySignIns?$filter=userId eq '{user-id}' and riskState eq 'confirmedCompromised' (or 'confirmedSafe' or 'dismissed'). 5. Verify that risk-based Conditional Access policies are enabled and applied to the user or sign-in by checking the policy assignments and sign-in logs.

## Rollback
1. If the user or sign-in was incorrectly marked as confirmed compromised, change the risk state back to 'atRisk' in the Microsoft Entra admin center: Protection > Identity Protection > Risky sign-ins > select the sign-in > Confirm safe. 2. If the user or sign-in was incorrectly marked as confirmed safe or dismissed but further investigation indicates it is compromised, change the risk state to 'Confirmed compromised' via the admin center or Microsoft Graph: PATCH https://graph.microsoft.com/v1.0/identityProtection/riskySignIns/{riskySignInId} with body {"riskState": "confirmedCompromised"}. 3. If risk-based Conditional Access policies were modified or created, revert those changes by disabling or deleting the policies in Protection > Conditional Access > Policies. 4. Notify the user of any changes to their risk state or access policies.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk>
