# Implementation: Endpoint Security

**Domain:** Intune
**Subdomain:** Endpoint Security
**Incident Type:** Implementation

## Scenario / Query
How to configure Microsoft Defender for Endpoint risk threshold in Intune compliance policy?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Microsoft Defender for Endpoint integration

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. On the Compliance settings tab, expand Microsoft Defender for Endpoint and configure Require the device to be at or under the machine risk score.
2. Select a risk level option: Clear (Most Secure) allows no threats and blocks any detected threats; Low allows low-level threats only and blocks medium and high threats; Medium allows low and medium threats and blocks high-level threats only; High (Least Secure) allows all threat levels and blocks none (reporting only).
3. Recommended setting: Low provides the best balance of security and user productivity for most organizations.
4. Configure Actions for noncompliance: Configure notifications and grace periods.
5. Assignments: Select device or user groups to receive this policy.
6. Review + create: Verify settings and create the policy.

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint Security > Compliance policies. 2. Select the policy you configured and go to Properties. 3. Under Compliance settings, confirm that Microsoft Defender for Endpoint is expanded and that 'Require the device to be at or under the machine risk score' is set to your chosen risk level (e.g., Low). 4. Verify that the policy is assigned to the correct groups and that the 'Actions for noncompliance' are configured as intended. 5. On a test device that is a member of the assigned group, run the command: 'dsregcmd /status' and confirm the device is Azure AD joined and enrolled in Intune. 6. On the same device, open the Microsoft Defender for Endpoint security center and verify the device risk score is at or below the configured threshold. 7. In the Intune admin center, go to Devices > Monitor > Compliance policies and confirm the test device shows as 'Compliant'.

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint Security > Compliance policies. 2. Select the policy you created or modified and go to Properties. 3. Under Compliance settings, expand Microsoft Defender for Endpoint and set 'Require the device to be at or under the machine risk score' to 'Not configured' or revert to the previous risk level. 4. If the policy was newly created, delete the policy entirely. 5. If the policy was assigned to groups, remove those assignments. 6. On any test devices, run 'dsregcmd /status' to confirm they are no longer subject to the policy. 7. Verify in the Intune admin center under Devices > Monitor > Compliance policies that the device status returns to its previous state.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
