# Implementation: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Implementation

## Scenario / Query
How to configure on-premises password reset to remediate user risks in a hybrid environment using Microsoft Entra ID Protection?

## Environment Context
- **Tenant Type:** hybrid
- **Configuration:** password hash synchronization enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign in to the Microsoft Entra admin center as at least a Security Operator.
2. Browse to Protection > Identity Protection > Settings.
3. Check the box to Allow on-premises password change to reset user risk and select Save.

## Validation
1. Sign in to the Microsoft Entra admin center as a Security Operator or higher. 2. Navigate to Protection > Identity Protection > Settings. 3. Confirm that the checkbox 'Allow on-premises password change to reset user risk' is checked and the Save button is visible. 4. Optionally, trigger a test user risk event and verify that after an on-premises password reset, the user's risk level resets to 'None' in the Identity Protection user risk report.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Security Operator or higher. 2. Navigate to Protection > Identity Protection > Settings. 3. Uncheck the checkbox 'Allow on-premises password change to reset user risk'. 4. Select Save to apply the change. 5. Verify that the setting is now disabled by refreshing the page and confirming the checkbox is unchecked.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock>
