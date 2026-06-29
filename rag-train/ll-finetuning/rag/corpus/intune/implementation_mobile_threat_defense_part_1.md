# Implementation: Mobile Threat Defense

**Domain:** Intune
**Subdomain:** Mobile Threat Defense
**Incident Type:** Implementation

## Scenario / Query
How do I connect Defender for Endpoint to Intune for a service-to-service integration?

## Environment Context
- **Tenant Type:** single tenant
- **Configuration:** One-time setup per tenant

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure admin access to the Microsoft Intune admin center with the Endpoint Security Manager role or equivalent permissions for Mobile Threat Defense settings.
2. Custom roles require Read and Modify rights for the Mobile Threat Defense permission.
3. Ensure admin access to the Microsoft Defender portal with the Security Administrator role in Microsoft Entra ID, or Manage security settings in Windows Security Center permission in Defender for Endpoint.

## Validation
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com) with an account that has the Endpoint Security Manager role or equivalent permissions. 2. Navigate to Endpoint security > Mobile Threat Defense. 3. Confirm that Microsoft Defender for Endpoint is listed as a connector and its status shows 'Enabled' or 'Connected'. 4. In the Microsoft Defender portal (https://security.microsoft.com), go to Settings > Endpoints > Advanced features. 5. Verify that 'Microsoft Intune connection' is toggled On. 6. Optionally, run the PowerShell cmdlet Get-MobileThreatDefenseConnector from the Microsoft Graph PowerShell module to confirm the connector state.

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint security > Mobile Threat Defense. 2. Select the Microsoft Defender for Endpoint connector and choose 'Disable' or 'Delete' to remove the connection. 3. In the Microsoft Defender portal, go to Settings > Endpoints > Advanced features and toggle 'Microsoft Intune connection' to Off. 4. If the integration was never fully established, simply do not complete the setup steps; no further action is required. 5. Verify that no Intune compliance policies or conditional access policies reference Defender for Endpoint as a threat level requirement.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
