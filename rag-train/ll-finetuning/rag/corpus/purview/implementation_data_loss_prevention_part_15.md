# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to implement the default DLP policy for devices to detect credit card numbers in files?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Default DLP policy for devices

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. The default policy for devices detects the presence of credit card numbers in files on devices when users perform specific activities (such as printing a file).
2. When detected, the activity is only audited (not blocked).
3. Admins will receive an alert, but policy tips won't be displayed to users.
4. You can edit these actions at any time.

## Validation
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) as a user with DLP compliance admin permissions.
2. Navigate to Data Loss Prevention > Policies.
3. Locate the policy named 'Default DLP policy for devices' and verify its status is 'On'.
4. Select the policy and review the configured actions: confirm that 'Audit only' is set for activities such as 'Print' and 'Copy to removable media'.
5. Check the policy scope: ensure it applies to 'All devices' or the intended device groups.
6. Use a test device with Microsoft 365 Apps for Enterprise and create a file containing a valid credit card number (e.g., 4111-1111-1111-1111).
7. Attempt to print the file from the device.
8. In the Microsoft Purview compliance portal, go to Data Loss Prevention > Alerts and verify that an alert is generated for the detected activity.
9. Confirm that no policy tip is displayed to the user during the print attempt.
10. Optionally, use the DLP Activity Explorer to confirm the event is logged with 'Audit' action.

## Rollback
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) as a user with DLP compliance admin permissions.
2. Navigate to Data Loss Prevention > Policies.
3. Locate the policy named 'Default DLP policy for devices'.
4. To disable the policy entirely, toggle the policy status to 'Off'.
5. Alternatively, to modify actions without disabling the policy: select the policy, click 'Edit policy', then under 'Actions' change the action for each activity (e.g., from 'Audit only' to 'Block with override' or 'Block').
6. If the policy was customized, restore the default actions by setting all activities back to 'Audit only'.
7. Save the policy changes.
8. Verify the rollback by repeating validation steps 3-5 to confirm the policy is disabled or actions are reverted.
9. If alerts were generated, clear or dismiss them as needed in the Alerts section.
10. Notify affected users that the policy has been adjusted.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference#default-policy-for-devices>
