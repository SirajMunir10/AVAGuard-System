# Implementation: Endpoint Data Loss Prevention (DLP)

**Domain:** Purview
**Subdomain:** Endpoint Data Loss Prevention (DLP)
**Incident Type:** Implementation

## Scenario / Query
How to configure DLP policy to detect copying protected files to a removable USB device?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP settings, removable USB device groups

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the 'Copy to a removable device' condition in DLP policy to detect when protected files are copied or moved from an onboarded device to a removable USB device.
2. For more information, see Removable USB device groups.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy configured for endpoint devices. 3. Under 'Locations', confirm 'Devices' is selected and includes the appropriate device groups. 4. Under 'Rules', verify a rule exists with the condition 'Copy to a removable device' (or 'Copy to a removable USB device' depending on policy builder version). 5. Confirm the action 'Audit or restrict' is set to 'Block' or 'Block with override' as required. 6. On a test Windows 10/11 device onboarded to Endpoint DLP, copy a protected file to a removable USB drive. 7. Verify that the copy is blocked and an end-user notification appears. 8. Check DLP activity explorer for the matching event.

## Rollback
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Policies. 2. Select the DLP policy that was modified. 3. Under 'Rules', locate the rule containing the 'Copy to a removable device' condition. 4. Either disable the rule by toggling it off, or delete the rule entirely. 5. If the policy was newly created, delete the entire policy. 6. On a test device, confirm that copying a protected file to a removable USB drive is no longer blocked. 7. Verify in DLP activity explorer that no new matching events are generated for that rule.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
