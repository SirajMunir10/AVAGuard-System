# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How do I configure DLP policy actions for Exchange and non-Exchange locations?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with Exchange and other locations

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. If you select Exchange and any other single location for the policy to be applied to, the Restrict access or encrypt the content in Microsoft 365 locations and all actions for the non-Exchange location actions are available.
2. If you select two or more non-Exchange locations for the policy to be applied to, the Restrict access or encrypt the content in Microsoft 365 locations and all actions for non-Exchange locations actions are available.
3. For example, if you select the Exchange and Devices locations, these actions are available: Restrict access or encrypt the content in Microsoft 365 locations, Audit or restrict activities on Windows devices.
4. If you select Devices and Instances, these actions are available: Restrict access or encrypt the content in Microsoft 365 locations, Audit or restrict activities on Windows devices, Restrict Third Party Apps.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Open the DLP policy that was configured. 3. Under 'Locations', confirm that Exchange email and the other selected location(s) are enabled. 4. Under 'Actions', verify that the available actions match the expected set based on the location combination: for Exchange + one other non-Exchange location, 'Restrict access or encrypt the content in Microsoft 365 locations' and all actions for the non-Exchange location should appear; for two or more non-Exchange locations, the same plus all non-Exchange location actions should appear. 5. Use the 'Test' or 'Simulate' mode (if available) to send a test email or trigger a test event to confirm the policy action is applied as expected.

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Policies, select the DLP policy. 2. Under 'Locations', uncheck the location(s) that were added or change the selection to revert to the previous configuration. 3. Under 'Actions', remove any actions that were added or reset to the previous action set. 4. Save the policy. 5. If the policy was in test mode, disable test mode or revert to the previous policy state. 6. Monitor for any residual effects and confirm that the original behavior is restored.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
