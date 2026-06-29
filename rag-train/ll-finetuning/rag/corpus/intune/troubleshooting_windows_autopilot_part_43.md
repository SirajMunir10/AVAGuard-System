# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
Why does the hybrid compliance state display as N/A for Windows Autopilot devices in the Azure portal, and how does this affect Conditional Access policies?

## Environment Context
- **Tenant Type:** Microsoft Entra ID (Azure AD) with Intune
- **Configuration:** Hybrid Azure AD joined devices, Windows Autopilot deployment, Conditional Access policies requiring device compliance

## Symptoms
- Hybrid compliance state shows as N/A in the devices list in the Azure portal
- Device-based Conditional Access policies block access based on compliance

## Error Codes
N/A

## Root Causes
1. Intune only syncs with the Hybrid device ID after a successful user sign-in
2. Until the device is rebooted, the status of BitLocker and Secure Boot are not captured, so they cannot be used as part of the Compliance Policy

## Remediation Steps
1. A user must sign in to the device to trigger Intune sync with the Hybrid device ID
2. Alternatively, the device-based policy must be modified to address the compliance state
3. Configure a grace period for Conditional Access policies such as BitLocker compliance, which can be as short as 0.25 days

## Validation
1. Sign in to the device with a user account that has an Intune license assigned.
2. Wait for the next Intune sync cycle (typically 15 minutes) or trigger a manual sync from the device: open Settings > Accounts > Access work or school > select the connected account > click Info > click Sync.
3. In the Azure portal, navigate to Microsoft Entra ID > Devices > All devices, locate the device, and verify that the 'Hybrid Azure AD joined' column shows 'Yes' and the 'Compliance' column shows a status other than 'N/A' (e.g., 'Compliant' or 'Noncompliant').
4. Confirm that the device now appears in Intune as a compliant device: go to Microsoft Intune admin center > Devices > All devices, select the device, and check the 'Compliance' status.
5. Test Conditional Access by accessing a resource protected by a policy that requires compliant devices; the user should be granted access.

## Rollback
1. If the compliance state remains 'N/A' after user sign-in and sync, modify the Conditional Access policy to include a grace period for BitLocker compliance: in the Microsoft Entra admin center, go to Protection > Conditional Access > Policies, select the relevant policy, under 'Grant' choose 'Require compliant device' and set 'For multiple controls' to 'Require all the selected controls', then add a session control with 'Use Conditional Access App Control' and configure a grace period of 0.25 days (6 hours) for BitLocker compliance.
2. Alternatively, temporarily disable the device compliance requirement in the Conditional Access policy by editing the policy and removing the 'Require device to be marked as compliant' grant control, or set the policy to 'Report-only' mode to monitor impact without blocking access.
3. If the issue persists, review the device's enrollment status in Intune: in the Microsoft Intune admin center, go to Devices > Enroll devices > Windows enrollment > Windows Autopilot Deployment Program, locate the device profile, and ensure it is assigned correctly. Reassign the profile if needed.
4. As a last resort, reset the device using Windows Autopilot reset and redeploy, ensuring a user signs in immediately after the Out-of-Box Experience (OOBE) completes.

## References
- <https://learn.microsoft.com/en-us/mem/autopilot/known-issues>
- <https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/concept-conditional-access-policy-common#require-compliant-or-microsoft-entra-hybrid-joined-device>
