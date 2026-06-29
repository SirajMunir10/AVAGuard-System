# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to configure Conditional Access to require a device to be marked as compliant using Intune compliance policies?

## Environment Context
- **Tenant Type:** Microsoft Entra ID with Intune
- **Configuration:** Conditional Access policy with grant control 'Require device to be marked as compliant'

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Deploy Intune compliance policies to identify devices that meet specific policy compliance requirements.
2. Ensure devices are registered in Microsoft Entra ID before they can be marked as compliant.
3. Configure Conditional Access policy to use the 'Require device to be marked as compliant' grant control.
4. For agent user scenarios, combine this control with scoping conditions so the policy applies only to endpoint-based sessions.
5. Use the Microsoft Defender for Endpoint app with the approved client app policy in Intune to set the device compliance policy to Conditional Access policies.

## Validation
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies and select the policy you configured. 3. Under Grant, confirm that 'Require device to be marked as compliant' is selected and no other conflicting grant controls are enabled. 4. Use the 'What If' tool (https://learn.microsoft.com/en-us/entra/identity/conditional-access/what-if-tool) to simulate a sign-in from a compliant device and verify the policy applies as expected. 5. On a test device that is Intune-enrolled and compliant, attempt to access a protected resource (e.g., Exchange Online) and confirm access is granted. 6. On a non-compliant or non-enrolled device, attempt the same access and confirm access is blocked with a message indicating the device is not compliant.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies and select the policy you configured. 3. Under Grant, change the control from 'Require device to be marked as compliant' to 'Require multifactor authentication' or another appropriate control, or set the policy to 'Off' to disable it. 4. If the policy was set to 'Report-only', switch it to 'Off' to fully disable. 5. Verify that users can access resources without the device compliance requirement by testing access from a non-compliant device. 6. If the issue was caused by Intune compliance policies, review and adjust those policies in the Microsoft Intune admin center (https://intune.microsoft.com) under Devices > Compliance policies.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant>
