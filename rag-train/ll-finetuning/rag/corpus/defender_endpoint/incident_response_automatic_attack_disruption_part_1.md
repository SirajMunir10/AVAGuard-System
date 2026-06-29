# Incident Response: Automatic Attack Disruption

**Domain:** Defender for Endpoint
**Subdomain:** Automatic Attack Disruption
**Incident Type:** Incident Response

## Scenario / Query
How does automatic attack disruption contain a user based on Microsoft Defender for Endpoint's capability?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Microsoft Defender for Endpoint onboarded devices

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Contain user - based on Microsoft Defender for Endpoint's capability, this response action automatically contains suspicious identities temporarily to help block any lateral movement and remote encryption related to incoming communication with Defender for Endpoint's onboarded devices.
2. Defender for Endpoint enforces user containment at the endpoint layer and doesn't disable the account in the identity provider.
3. Defender for Endpoint blocks attacker use of compromised identities on protected devices and limits authentication-based access, file system access, and network communication paths.
4. This action applies controls at a granular level, so Microsoft can target attack-related activity and preserve normal business communication where possible.

## Validation
1. In Microsoft 365 Defender (https://security.microsoft.com), navigate to Incidents & alerts > Incidents and select the relevant incident. 2. Under the 'Attack story' tab, verify that an automatic action of type 'Contain user' is listed with status 'Completed' or 'Succeeded'. 3. In the same incident, go to the 'Actions & submissions' tab and confirm the 'Contain user' action shows a successful completion timestamp. 4. On a Defender for Endpoint onboarded device, run the following PowerShell command as administrator to confirm the user is contained: `Get-MpPreference | Select-Object -ExpandProperty ExclusionIpAddress` (this will show IP exclusions; containment blocks the user's network access). Alternatively, check the device's local security policy or use `Get-MpComputerStatus` to verify the containment state. 5. Verify that the user can still authenticate to non-protected resources (e.g., Microsoft Entra ID) but is blocked from accessing Defender for Endpoint onboarded devices by attempting to access a shared folder on a protected device from the contained user's account – access should be denied.

## Rollback
1. In Microsoft 365 Defender, navigate to Incidents & alerts > Incidents and select the relevant incident. 2. Under the 'Actions & submissions' tab, locate the 'Contain user' action. 3. If the action is still pending or failed, no rollback is needed; if it succeeded and you need to release the user, select the action and choose 'Undo' or 'Release user' (if available). 4. If the 'Undo' option is not present, manually release the user by running the following PowerShell command on a Defender for Endpoint onboarded device: `Remove-MpPreference -ExclusionIpAddress <contained_user_IP>` (replace with the actual IP). 5. Verify the user's access is restored by having the user attempt to access a protected resource – access should be granted. 6. If the user remains blocked, check for any remaining containment policies in Microsoft 365 Defender under Settings > Endpoints > Advanced features > Automatic attack disruption and ensure the feature is not still enforcing containment.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption>
