# Incident Response: Incident Response

**Domain:** Sentinel
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
A security analyst in a Microsoft Sentinel environment receives an incident indicating that a user account was used to sign in from an unfamiliar location and device. The incident was automatically created by an analytics rule. How should the analyst triage and investigate this incident using built-in Sentinel capabilities?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Microsoft Sentinel enabled
- **Configuration:** Analytics rule 'Suspicious sign-in from unfamiliar location' enabled, using UEBA data

## Symptoms
- Incident created in Microsoft Sentinel with high severity
- Sign-in log shows IP address from a country not in the user's typical travel pattern
- User agent string indicates a browser version not previously seen for this user

## Error Codes
N/A

## Root Causes
1. Analytics rule triggered based on UEBA anomaly detection for sign-in location
2. No explicit error; the incident is a result of a configured detection

## Remediation Steps
1. 1. Open the incident in Microsoft Sentinel and review the incident details pane.
2. 2. Use the 'Investigate' button to open the investigation graph and explore related entities (user, IP, device).
3. 3. Run the built-in hunting query 'Anomalous sign-in location' from the Sentinel hunting blade to gather additional context.
4. 4. If the sign-in is confirmed malicious, use the 'Actions' menu to assign the incident to an analyst and change status to 'Active'.
5. 5. Initiate a playbook (e.g., 'Block user' or 'Force password reset') from the incident page if automated response is configured.

## Validation
After remediation, verify that the user's account shows no further anomalous sign-ins in the next 24 hours using the Sentinel 'IdentityInfo' table and Azure AD sign-in logs.

## Rollback
If the playbook blocked the user, re-enable the account via Azure AD admin center and reset the user's password. Remove any conditional access policy that was applied by the playbook.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/investigate-incidents>
- <https://learn.microsoft.com/en-us/azure/sentinel/incident-investigation>
