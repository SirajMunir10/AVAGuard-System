# Implementation: Endpoint Security

**Domain:** Intune
**Subdomain:** Endpoint Security
**Incident Type:** Implementation

## Scenario / Query
How to create and assign a compliance policy in Intune that uses Microsoft Defender for Endpoint device risk level to automatically mark devices as noncompliant?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Microsoft Defender for Endpoint integration

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create a compliance policy in the Microsoft Intune admin center that sets a device risk level threshold.
2. Assign the compliance policy to the target device groups (Android, iOS/iPadOS, Windows).
3. Devices exceeding the configured risk threshold are automatically marked as noncompliant.
4. Conditional Access policies can then block noncompliant devices from corporate resources.

## Validation
1. In the Microsoft Intune admin center, navigate to 'Endpoint security' > 'Device compliance' and confirm the new compliance policy appears in the list with the correct risk level threshold (e.g., Medium, High).
2. Select the policy and review the 'Assignments' tab to verify it is assigned to the intended device groups (Android, iOS/iPadOS, Windows).
3. On a test device enrolled in Intune and integrated with Microsoft Defender for Endpoint, trigger a high-risk alert (e.g., by running a simulated threat).
4. In the Intune admin center, go to 'Devices' > 'All devices', select the test device, and check its compliance status. It should show as 'Noncompliant' with a reason related to Defender for Endpoint risk level.
5. Verify that Conditional Access policies (if configured) block the device from accessing corporate resources, such as Exchange Online or SharePoint.

## Rollback
1. In the Microsoft Intune admin center, navigate to 'Endpoint security' > 'Device compliance' and select the newly created compliance policy.
2. Click 'Properties' and change the 'Device risk level' threshold to a less restrictive setting (e.g., from 'Medium' to 'High') or set it to 'Not configured' to disable the risk check.
3. Alternatively, remove the policy assignment by going to the 'Assignments' tab, selecting the assigned groups, and clicking 'Remove'.
4. If the policy is no longer needed, select the policy and click 'Delete' to remove it entirely.
5. For devices already marked noncompliant, trigger a compliance re-evaluation by selecting the device in 'Devices' > 'All devices' and clicking 'Sync' or 'Check compliance'.
6. Confirm that devices return to a compliant state and Conditional Access policies no longer block access.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
