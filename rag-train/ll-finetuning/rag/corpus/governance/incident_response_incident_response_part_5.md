# Incident Response: Incident Response

**Domain:** Governance
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
How do I configure and validate Microsoft 365 incident response policies to ensure proper logging and alerting for suspicious sign-in activities?

## Environment Context
- **Tenant Type:** Microsoft 365 E5
- **Configuration:** Azure AD Premium P2 licensing required for Identity Protection and Privileged Identity Management

## Symptoms
- Unusual sign-in locations or devices
- Multiple failed sign-in attempts followed by a successful sign-in
- Sign-ins from anonymous IP addresses or Tor exit nodes

## Error Codes
N/A

## Root Causes
1. Incident response policies not configured to detect and alert on high-risk sign-ins
2. Identity Protection risk policies not enabled or misconfigured
3. Lack of automated response actions for confirmed compromises

## Remediation Steps
1. Configure Azure AD Identity Protection user risk policy: Sign-in risk policy to block high-risk sign-ins and require MFA for medium risk
2. Enable audit logging in Microsoft 365 Defender and Azure AD (sign-in logs, audit logs)
3. Create an incident response playbook in Microsoft Sentinel or Microsoft 365 Defender that triggers automated investigation and response for high-severity alerts
4. Assign appropriate roles (e.g., Security Administrator, Incident Responder) to personnel responsible for incident response

## Validation
Verify that Azure AD Identity Protection risk policies are enabled and applied to all users. Confirm that sign-in logs show risk detections and that automated actions (e.g., blocking sign-in, requiring password change) are triggered for high-risk events.

## Rollback
Disable or modify the Identity Protection risk policies to a lower risk threshold or remove automated blocking actions if false positives occur.

## References
- Microsoft Learn: 'Configure Azure AD Identity Protection risk policies' - https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/howto-identity-protection-configure-risk-policies
- Microsoft Learn: 'Audit logs in Azure Active Directory' - https://learn.microsoft.com/en-us/azure/active-directory/reports-monitoring/concept-audit-logs
