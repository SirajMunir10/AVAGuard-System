# Troubleshooting: Self-Service Password Reset

**Domain:** Entra ID
**Subdomain:** Self-Service Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
Why does an authentication method that I disabled in the Add method option still appear in combined registration?

## Environment Context
- **Tenant Type:** Entra ID tenant with combined registration enabled
- **Configuration:** SSPR and MFA policies

## Symptoms
- Disabled authentication methods appear in the Add method option during combined registration

## Error Codes
N/A

## Root Causes
1. The combined registration takes into account three policies: Self-service password reset, Authentication methods, and MFA policy
2. If app notifications are disabled in SSPR but enabled in MFA policy, that option appears in combined registration
3. If a user disables Office phone in SSPR, it's still displayed as an option if the user has the Phone/Office phone property set

## Remediation Steps
1. Review and align SSPR, Authentication methods, and MFA policies to ensure consistency
2. Check user property settings (e.g., Phone/Office phone) that may override SSPR method settings

## Validation
1. Verify SSPR policy: Navigate to Entra admin center > Protection > Password reset > Authentication methods. Confirm that 'App notification' is set to 'No'.
2. Verify MFA policy: Go to Entra admin center > Protection > Multifactor authentication > Additional cloud-based MFA settings. Under 'verification options', ensure 'Notification through mobile app' is unchecked.
3. Verify user property: For a test user, run: Get-MgUser -UserId <userUPN> -Property BusinessPhones, MobilePhone. Confirm that 'BusinessPhones' is empty or not set.
4. Perform combined registration as the test user at https://aka.ms/mfasetup. Confirm that 'App notification' and 'Office phone' do not appear in the 'Add method' list.

## Rollback
1. Re-enable SSPR method: In Entra admin center > Protection > Password reset > Authentication methods, set 'App notification' back to 'Yes'.
2. Re-enable MFA method: In Entra admin center > Protection > Multifactor authentication > Additional cloud-based MFA settings, check 'Notification through mobile app'.
3. Restore user property: If a user's Office phone was cleared, set it back using: Update-MgUser -UserId <userUPN> -BusinessPhones @("+1 425 555 0100").
4. Instruct the user to re-register at https://aka.ms/mfasetup to confirm the methods reappear.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr>
