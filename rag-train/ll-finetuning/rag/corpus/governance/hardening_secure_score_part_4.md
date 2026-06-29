# Hardening: Secure Score

**Domain:** Governance
**Subdomain:** Secure Score
**Incident Type:** Hardening

## Scenario / Query
A security administrator notices that the Microsoft Secure Score for their tenant has dropped significantly. Investigation reveals that several security defaults and recommended security policies are not applied. How can the administrator identify and remediate the missing security controls to improve the Secure Score?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft 365 Defender portal, Secure Score dashboard

## Symptoms
- Decrease in overall Secure Score
- Security recommendations marked as 'Not implemented' or 'Risk accepted'
- Alerts from Microsoft Defender for Cloud Apps indicating weak security posture

## Error Codes
N/A

## Root Causes
1. Security defaults were disabled or never enabled
2. Conditional Access policies not configured according to best practices
3. Multi-factor authentication not enforced for all users

## Remediation Steps
1. Enable security defaults in the Azure AD tenant by navigating to Azure Active Directory > Properties > Manage Security defaults and setting 'Enable Security defaults' to Yes.
2. Review and implement all security recommendations listed in the Microsoft Secure Score dashboard under 'Recommended actions'.
3. Configure Conditional Access policies to require MFA for all users and block legacy authentication as documented in 'Common Conditional Access policies'.

## Validation
Verify that the Secure Score increases after implementing the recommended actions. Use the Secure Score API or dashboard to confirm that the score reflects the changes.

## Rollback
Disable security defaults by setting 'Enable Security defaults' to No. Remove or disable any newly created Conditional Access policies.

## References
- Microsoft Learn: 'What is Microsoft Secure Score?'
- Microsoft Learn: 'Security defaults in Azure AD' - https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/security-defaults
