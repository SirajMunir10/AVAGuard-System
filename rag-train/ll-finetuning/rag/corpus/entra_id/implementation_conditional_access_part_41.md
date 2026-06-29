# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to migrate from deprecated device state condition to filter for devices condition in Conditional Access policies?

## Environment Context
- **Tenant Type:** Entra ID tenant with Conditional Access policies using device state condition
- **Configuration:** Conditional Access policy configuration

## Symptoms
- Device state condition is deprecated
- Device state and filters for devices cannot be used together in the same policy

## Error Codes
N/A

## Root Causes
1. Device state condition has been deprecated by Microsoft
2. Customers need to migrate to filter for devices condition for more granular targeting

## Remediation Steps
1. Identify existing Conditional Access policies using device state condition
2. Create new policies using filter for devices condition with trustType and isCompliant properties
3. Remove device state condition from policies before adding filter for devices condition
4. Test new policies before removing old ones

## Validation
1. Run 'Get-MgIdentityConditionalAccessPolicy' to list all policies. 2. For each policy, confirm that the 'conditions.deviceStates.includeStates' and 'conditions.deviceStates.excludeStates' properties are absent or empty. 3. Verify that the 'conditions.devices.filter' property contains a valid filter rule (e.g., 'device.trustType eq "AzureAD" and device.isCompliant eq true'). 4. Use 'Test-MgIdentityConditionalAccessPolicy' to simulate sign-in with a test device and confirm the policy applies as expected.

## Rollback
1. Run 'Get-MgIdentityConditionalAccessPolicy' to identify the policy that was modified. 2. Remove the filter for devices condition by setting 'conditions.devices.filter' to $null. 3. Restore the original device state condition by setting 'conditions.deviceStates.includeStates' to the previous value (e.g., 'All') and 'conditions.deviceStates.excludeStates' to the previous value (e.g., 'Compliant'). 4. Use 'Update-MgIdentityConditionalAccessPolicy' to apply the restored configuration. 5. Re-enable the original policy if it was disabled.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-conditions>
