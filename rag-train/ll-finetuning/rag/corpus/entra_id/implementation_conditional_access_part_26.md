# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to configure Conditional Access to require device compliance using Microsoft Defender for Endpoint and Intune?

## Environment Context
- **Tenant Type:** Microsoft Entra ID with Intune and Microsoft Defender for Endpoint
- **Configuration:** Conditional Access policy with 'Require device to be marked as compliant' and approved client app policy

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the Microsoft Defender for Endpoint app with the approved client app policy in Intune to set the device compliance policy to Conditional Access policies.
2. No exclusion is required for the Microsoft Defender for Endpoint app while setting up Conditional Access.
3. Note that Microsoft Defender for Endpoint on Android and iOS (app ID dd47d17a-3194-4d86-bfd5-c6ae6f5651e3) is not an approved app but has permission to report device security posture, enabling compliance information flow to Conditional Access.

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies and select the policy that was configured. 3. Under 'Assignments', confirm that the policy targets the intended users, groups, or workloads. 4. Under 'Access controls > Grant', verify that 'Require device to be marked as compliant' is selected and that 'Require approved client app' is also selected. 5. In the 'Grant' blade, confirm that 'Require all the selected controls' is chosen. 6. Use the 'What If' tool to simulate a sign-in from a test user on a device that is compliant and has the Microsoft Defender for Endpoint app (app ID dd47d17a-3194-4d86-bfd5-c6ae6f5651e3) installed; confirm the policy is applied and access is granted. 7. Repeat the simulation with a non-compliant device or without the approved app; confirm access is blocked. 8. In Intune, verify that the device compliance policy is assigned to the test device and that the device reports as compliant. 9. In Microsoft Defender for Endpoint, confirm the device security posture is being reported to Entra ID.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies and select the policy that was configured. 3. Under 'Access controls > Grant', deselect 'Require device to be marked as compliant' and/or 'Require approved client app' as needed. 4. Alternatively, set the policy to 'Off' under 'Enable policy' to disable it entirely. 5. If the policy was created new, delete the policy by selecting it and clicking 'Delete'. 6. In Intune, remove or modify the device compliance policy that was linked to Conditional Access if it was created solely for this purpose. 7. Verify that users can access resources without the device compliance requirement by testing sign-in with a non-compliant device.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant>
