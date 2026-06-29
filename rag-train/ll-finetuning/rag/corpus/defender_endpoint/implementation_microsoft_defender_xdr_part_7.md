# Implementation: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Implementation

## Scenario / Query
How do I start a pilot of Microsoft Defender XDR in my existing production Microsoft 365 tenant?

## Environment Context
- **Tenant Type:** production
- **Configuration:** Microsoft 365 subscription with Defender XDR

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Start your pilot in your existing production subscription of Microsoft 365 to gain real-world insights immediately.
2. Tune settings to work against current threats in your Microsoft 365 tenant.
3. After gaining experience and being comfortable with the platform, expand the use of each component, one at a time, to full deployment.

## Validation
1. Confirm that Microsoft Defender XDR is enabled in the Microsoft 365 Defender portal (https://security.microsoft.com) by navigating to Settings > Endpoints > General > Advanced features and verifying that 'Microsoft Defender XDR' is set to On.
2. Verify that the required licenses (e.g., Microsoft 365 E5, Microsoft Defender for Endpoint Plan 2) are assigned to pilot users in the Microsoft 365 admin center (https://admin.microsoft.com) under Billing > Licenses.
3. Run a test detection by simulating an attack using the Microsoft 365 Defender evaluation and training simulator (https://security.microsoft.com/training/simulations) and confirm that alerts appear in the Incidents queue.
4. Check that email notifications for alerts are being sent to the pilot group by reviewing the alert notification settings under Settings > Endpoints > General > Alert notifications.

## Rollback
1. Disable Microsoft Defender XDR for the pilot group by navigating to Settings > Endpoints > General > Advanced features in the Microsoft 365 Defender portal and toggling 'Microsoft Defender XDR' to Off.
2. Remove pilot users from any assigned Defender for Endpoint licenses by going to the Microsoft 365 admin center, selecting Users > Active users, choosing each pilot user, and under the Licenses and apps tab, unchecking the relevant Defender license.
3. Delete any test incidents or alerts generated during the pilot by using the 'Delete' option in the Incidents queue (note: this may not be reversible; ensure no real incidents are affected).
4. Restore any modified security policies to their pre-pilot state by reviewing the audit log in the Microsoft 365 Defender portal under Auditing and reverting changes to settings such as attack surface reduction rules or automated investigation and response.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/eval-overview>
