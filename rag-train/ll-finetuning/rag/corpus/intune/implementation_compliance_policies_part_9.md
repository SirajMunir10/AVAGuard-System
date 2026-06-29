# Implementation: Compliance Policies

**Domain:** Intune
**Subdomain:** Compliance Policies
**Incident Type:** Implementation

## Scenario / Query
How to create a compliance policy for Windows devices in Intune?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** Windows compliance policy creation

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Add actions for noncompliant devices and use scope tags to filter policies.
2. Monitor your compliance policies.
3. See the compliance policy settings for Windows 8.1 devices.

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Device compliance > Policies. Confirm the new Windows compliance policy appears in the list with the correct name and assigned scope tags. 2. Select the policy and review the 'Properties' pane to verify all configured settings (e.g., password requirements, encryption, OS version) match the intended configuration. 3. Under 'Monitor' for the policy, check the 'Device compliance' and 'Noncompliant devices' reports to ensure devices are reporting the expected compliance state. 4. On a test Windows device enrolled in Intune, run 'dsregcmd /status' and verify the 'AzureAdJoined' status is 'YES'. Then open Settings > Accounts > Access work or school > Info and confirm the compliance status shows as 'Compliant' or 'Noncompliant' as expected based on the policy.

## Rollback
1. In the Microsoft Intune admin center, go to Endpoint security > Device compliance > Policies. Select the problematic Windows compliance policy and choose 'Delete'. Confirm deletion when prompted. 2. If the policy was assigned to groups, remove those assignments before deletion to avoid any lingering enforcement. 3. If a previous compliant state is needed, re-create the policy using the original settings or restore from a backup of the policy configuration (if available). 4. After deletion, monitor the 'Device compliance' reports to confirm devices return to their previous compliance state (e.g., no longer showing as noncompliant due to the deleted policy).

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-create-windows>
