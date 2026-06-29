# Hardening: Hardening

**Domain:** Governance
**Subdomain:** Hardening
**Incident Type:** Hardening

## Scenario / Query
A security administrator notices that Microsoft 365 Defender for Cloud Apps is not enforcing session policies for high-risk sign-ins from non-compliant devices. How can the administrator harden the environment by configuring Conditional Access App Control to block or monitor such sessions?

## Environment Context
- **Tenant Type:** Microsoft 365 E5
- **Configuration:** Conditional Access policies are configured but session controls in Defender for Cloud Apps are not enabled for all relevant apps.

## Symptoms
- High-risk sign-ins from non-compliant devices are allowed without session monitoring or blocking
- Defender for Cloud Apps activity logs show no session policy enforcement for identified risky users

## Error Codes
N/A

## Root Causes
1. Conditional Access session controls are not configured to route traffic through Defender for Cloud Apps
2. Session policies in Defender for Cloud Apps are not created or are in report-only mode

## Remediation Steps
1. 1. Sign in to the Microsoft 365 Defender portal as a Global Administrator or Security Administrator.
2. 2. Navigate to Cloud Apps â†’ Policies â†’ Session policies.
3. 3. Create a new session policy: select 'Create policy' â†’ 'Session policy'.
4. 4. Set the policy template to 'Block download' or 'Monitor only' based on the hardening requirement.
5. 5. Under 'Session control type', choose 'Control file download (with inspection)' or 'Block activities' as needed.
6. 6. Under 'Activities matching all of the following', select the appropriate filters (e.g., 'Device tag' equals 'Non-compliant').
7. 7. Set the 'Actions' to 'Block' or 'Monitor'.
8. 8. Ensure that the corresponding Conditional Access policy includes the 'Use Conditional Access App Control' session control under 'Session' settings.
9. 9. Test the policy with a pilot user group before broad deployment.

## Validation
Confirm that the session policy appears in the Defender for Cloud Apps policy list with status 'Enabled' and that test sessions from non-compliant devices trigger the expected block or monitor action in the activity log.

## Rollback
Disable the session policy by setting its status to 'Disabled' in Defender for Cloud Apps, and remove the 'Use Conditional Access App Control' session control from the associated Conditional Access policy.

## References
- <https://learn.microsoft.com/en-us/defender-cloud-apps/session-policy>
