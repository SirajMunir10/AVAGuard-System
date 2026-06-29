# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
How to configure Conditional Access policy exceptions for Microsoft Intune Enrollment and Microsoft Intune cloud apps to complete Windows Autopilot enrollment?

## Environment Context
- **Tenant Type:** Microsoft Entra ID with Intune
- **Configuration:** Restrictive Conditional Access policies: Policy 1 blocks all apps except those on an exclusion list; Policy 2 requires a compliant device for apps on the exclusion list

## Symptoms
- Windows Autopilot enrollment cannot complete due to restrictive Conditional Access policies

## Error Codes
N/A

## Root Causes
1. Conditional Access policies block all apps except those on an exclusion list, and require compliant devices for apps on the exclusion list

## Remediation Steps
1. Include Microsoft Intune Enrollment and Microsoft Intune in the exclusion list of Conditional Access policy 1 (Block all apps except those on an exclusion list)
2. Note: If a policy requires all cloud apps to be compliant (no exclusion list), Microsoft Intune Enrollment is excluded by default to allow device registration and enrollment

## Validation
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a Conditional Access administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate Policy 1 (the policy that blocks all apps except those on an exclusion list). 4. Under 'Cloud apps or actions', confirm that 'Microsoft Intune Enrollment' and 'Microsoft Intune' are listed in the 'Exclude' tab. 5. Locate Policy 2 (the policy that requires a compliant device for apps on the exclusion list). 6. Under 'Conditions', confirm that 'Device platforms' and 'Client apps' are configured appropriately to allow Autopilot enrollment (e.g., Windows and browser/device registration). 7. Perform a test Windows Autopilot enrollment on a fresh device and verify that the enrollment completes successfully without being blocked by Conditional Access.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Locate Policy 1. 4. Under 'Cloud apps or actions', in the 'Exclude' tab, remove 'Microsoft Intune Enrollment' and 'Microsoft Intune' from the exclusion list. 5. If Policy 2 was modified, revert any changes made to 'Conditions' (e.g., device platforms or client apps) to their original state. 6. Verify that the original restrictive policies are re-enabled and enforced. 7. Confirm that Windows Autopilot enrollment is again blocked, matching the pre-remediation state.

## References
- <https://learn.microsoft.com/en-us/mem/autopilot/known-issues>
