# Troubleshooting: Multifactor Authentication

**Domain:** Entra ID
**Subdomain:** Multifactor Authentication
**Incident Type:** Troubleshooting

## Scenario / Query
How to review Microsoft Entra multifactor authentication events using sign-in logs?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** MFA deployment

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the Microsoft Entra sign-in logs which include authentication details for events when a user is prompted for MFA, and if any Conditional Access policies were in use.
2. Note that NPS extension and AD FS logs for cloud MFA activity are now included in the sign-in logs, and no longer published to the Activity report.
3. For more information, see Review Microsoft Entra multifactor authentication events.

## Validation
1. Sign in to the Microsoft Entra admin center as a Global Administrator. 2. Navigate to Identity > Monitoring & health > Sign-in logs. 3. Filter by date range and user to locate the relevant sign-in event. 4. Select a sign-in event and review the Authentication Details tab to confirm MFA requirement, result, and any Conditional Access policies applied. 5. Verify that the 'MFA requirement' field shows 'Required' or 'Not required' as expected. 6. Check that the 'Result' field indicates success or failure for the MFA challenge.

## Rollback
1. If sign-in logs do not show expected MFA events, verify that diagnostic settings are configured to stream sign-in logs to a Log Analytics workspace or storage account. 2. Ensure the user has an appropriate license (e.g., Microsoft Entra ID P1 or P2) for MFA reporting. 3. Confirm that the user is not excluded from MFA via Conditional Access policies or per-user MFA settings. 4. If using NPS extension or AD FS, verify that those components are properly configured and sending logs to Microsoft Entra ID. 5. As a last resort, re-enable per-user MFA for the affected user via the legacy MFA portal (Identity > Users > Per-user MFA) and test again.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-getstarted>
