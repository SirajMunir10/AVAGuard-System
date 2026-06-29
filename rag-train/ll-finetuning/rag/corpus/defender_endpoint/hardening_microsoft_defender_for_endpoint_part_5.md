# Hardening: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Hardening

## Scenario / Query
How to contain a user in Microsoft Defender for Endpoint to block compromised identities on protected devices?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Onboarded Windows 10/11 devices (Sense version 8740+), Windows Server 2019+, Windows Server 2012R2/2016 with modern agent

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Trigger the contain user action from the Microsoft Defender for Endpoint portal.
2. When triggered by predictive shielding, the action applies restrictions more selectively, focusing on high-risk users identified through prediction logic.
3. The contain user action prevents new sessions rather than terminating existing ones when triggered by predictive shielding.
4. Once enforced on a domain controller, it starts a GPO update on the Default Domain Controller policy, which syncs across domain controllers.

## Validation
1. Confirm the user containment action was triggered: In Microsoft Defender for Endpoint portal, navigate to Incidents > select the relevant incident > check the 'Actions' tab for 'Contain user' status (Pending, In progress, or Completed).
2. Verify the user is blocked on protected devices: On a domain-joined Windows 10/11 device, run 'gpresult /r' and confirm the 'Default Domain Controller Policy' is applied. Check local security policy for 'Deny log on locally' or 'Deny log on through Remote Desktop Services' containing the user account.
3. Validate new session prevention: Attempt to log on interactively or via RDP with the contained user account on a protected device. The logon should be denied.
4. Confirm existing sessions are not terminated (if triggered by predictive shielding): Use 'query user' on the device to list active sessions; the contained user's session should remain active if it existed before containment.

## Rollback
1. Remove the user containment: In Microsoft Defender for Endpoint portal, go to Settings > Endpoints > Automated investigations > select the relevant investigation > choose 'Contain user' action and select 'Remove containment'.
2. Force Group Policy update on domain controllers: Run 'gpupdate /force' on a domain controller to revert the Default Domain Controller Policy changes.
3. Verify the user can log on again: On a protected device, attempt to log on with the user account; the logon should succeed.
4. Confirm no residual restrictions: Check local security policy on a device for any remaining deny logon entries for the user and remove if necessary.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
