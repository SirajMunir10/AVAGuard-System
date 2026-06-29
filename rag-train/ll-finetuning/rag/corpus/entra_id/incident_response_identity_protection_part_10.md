# Incident Response: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Incident Response

## Scenario / Query
How to investigate a Microsoft Entra threat intelligence risk detection when the account was the victim of a password spray attack?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** Identity Protection risk detection

## Symptoms
- Account was the victim of a password spray attack

## Error Codes
N/A

## Root Causes
1. Password spray attack targeting the account

## Remediation Steps
1. Validate that no other users in your directory are targets of the same attack
2. Determine if other users have sign-ins with similar atypical patterns seen in the detected sign-in within the same time frame
3. Investigate unusual patterns in: user agent string, application, protocol, ranges of IPs/ASNs, time and frequency of sign-ins

## Validation
1. Sign in to the Microsoft Entra admin center as a Security Administrator. 2. Navigate to Protection > Identity Protection > Risky sign-ins. 3. Filter by the risk detection type 'Threat intelligence' and the time frame of the original incident. 4. Review the list for any other users with similar sign-in patterns (e.g., same user agent string, application, protocol, IP ranges, ASN, or time/frequency patterns). 5. Confirm that no other users show the same atypical patterns as the detected sign-in. 6. Optionally, use Microsoft Graph PowerShell: `Get-MgRiskDetection -Filter "riskType eq 'threatIntelligence' and riskLevel eq 'high'"` to programmatically verify no other detections exist for the same attack.

## Rollback
1. If the validation reveals additional affected users, repeat the investigation steps for each user: review their risky sign-ins and sign-in logs for similar patterns. 2. For each affected user, follow the remediation guidance in the Microsoft documentation: a. Confirm the user is aware of the suspicious sign-in. b. If the sign-in is confirmed as malicious, initiate a password reset for the user and revoke their sessions. c. If the sign-in is benign (e.g., false positive), dismiss the risk in Identity Protection by selecting 'Dismiss user risk' or 'Dismiss sign-in risk' as appropriate. 3. Document all findings and actions taken in the incident response record.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk>
