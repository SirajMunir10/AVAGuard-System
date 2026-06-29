# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
Local Autopilot Reset cannot be triggered by local administrator when network access is denied

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Intune policy setting 'Deny access to this computer from the network' for the local account

## Symptoms
- Local Windows administrator account cannot start a local Windows Autopilot Reset
- Issue occurs from Windows sign-in screen or after local sign-in

## Error Codes
N/A

## Root Causes
1. Device configured with an Intune policy that sets 'Deny access to this computer from the network' for the local account

## Remediation Steps
1. Remove the 'Deny access to this computer from the network' setting for the local account
2. Or exclude devices that require local Autopilot Reset from this policy
3. After the device syncs the updated policy, local Autopilot Reset works

## Validation
1. Confirm the current 'Deny access to this computer from the network' policy assignment: In Microsoft Intune admin center, go to Endpoint security > Attack surface reduction > Account protection policies. Check if any policy includes 'Deny access to this computer from the network' for the local account. 2. Verify the policy is no longer applied to the affected device: In Intune, select Devices > All devices > choose the device > Device configuration. Ensure the policy is removed or the device is excluded. 3. On the device, run 'gpresult /h gpresult.html' and open the report. Under 'Computer Configuration > Windows Settings > Security Settings > Local Policies > User Rights Assignment', confirm 'Deny access to this computer from the network' does not list the local account. 4. Trigger a sync: On the device, go to Settings > Accounts > Access work or school > select the MDM enrollment > Info > Sync. Alternatively, run 'dsregcmd /sync' from an elevated command prompt. 5. After sync, attempt a local Autopilot Reset: From the Windows sign-in screen, press Ctrl+Win+R, or after local sign-in, go to Settings > Update & Security > Recovery > Reset this PC > Remove everything. Verify the reset initiates without the 'access denied' error.

## Rollback
1. Reapply the 'Deny access to this computer from the network' policy: In Intune admin center, go to Endpoint security > Attack surface reduction > Account protection policies. Create or edit a policy to include 'Deny access to this computer from the network' for the local account. Assign the policy to the affected device or group. 2. If the device was excluded, remove the exclusion: In the same policy, under 'Assignments', remove the device or group from the 'Excluded groups' list. 3. Force a policy sync on the device: Run 'dsregcmd /sync' from an elevated command prompt, or use Intune remote sync (Devices > All devices > select device > Sync). 4. Verify the policy is reapplied: On the device, run 'gpresult /h gpresult.html' and confirm 'Deny access to this computer from the network' lists the local account. 5. Confirm local Autopilot Reset is blocked again: Attempt a local Autopilot Reset (Ctrl+Win+R at sign-in or via Settings) and verify the operation fails with an access denied message.

## References
- <https://learn.microsoft.com/en-us/mem/autopilot/known-issues>
