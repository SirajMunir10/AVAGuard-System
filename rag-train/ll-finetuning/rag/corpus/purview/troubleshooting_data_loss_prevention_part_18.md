# Troubleshooting: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Troubleshooting

## Scenario / Query
What happens when a user overrides a DLP block action for copying to a removable USB device or network share?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policy with user overrides enabled for activities: Copy to a removable USB device, Copy to a network share

## Symptoms
- User selects Allow option to override a block action for copy to USB or network share
- Activity is allowed to continue within 30 seconds of popup notification showing
- If user does not select Allow within 30 seconds, activity is blocked

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Within 30 seconds of the popup notification showing, the activity is allowed to continue
2. If the user doesn't select the Allow option within 30 seconds, the activity is blocked

## Validation
1. Simulate a DLP policy with user overrides enabled for 'Copy to a removable USB device' and 'Copy to a network share'. 2. As a user, attempt to copy a sensitive file to a USB device. 3. Observe the popup notification. 4. Select the 'Allow' option within 30 seconds. 5. Confirm the file copy completes successfully. 6. Repeat steps 2-5 for a network share. 7. As a user, attempt to copy a sensitive file to a USB device. 8. Do not select any option within 30 seconds. 9. Confirm the file copy is blocked. 10. Repeat steps 7-9 for a network share.

## Rollback
1. In the Microsoft Purview compliance portal, navigate to Data Loss Prevention > Policies. 2. Locate the DLP policy that has user overrides enabled. 3. Edit the policy and disable user overrides for 'Copy to a removable USB device' and 'Copy to a network share'. 4. Save the policy. 5. Test that users are now blocked from copying sensitive files to USB devices and network shares without an override option.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
