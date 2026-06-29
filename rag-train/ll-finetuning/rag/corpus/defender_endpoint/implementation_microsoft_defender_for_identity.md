# Implementation: Microsoft Defender for Identity

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Identity
**Incident Type:** Implementation

## Scenario / Query
How to audit sensor management activities in Microsoft Defender for Identity?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log enabled

## Symptoms
- New sensors added or removed unexpectedly

## Error Codes
N/A

## Root Causes
1. A new sensor was added (SensorCreated)
2. A sensor was deleted (SensorDeleted)
3. The sensors access key was regenerated (SensorDeploymentAccessKeyUpdated)
4. The sensors access key was retrieved (SensorDeploymentAccessKeyReceived)

## Remediation Steps
1. Review the audit log for SensorCreated, SensorDeleted, SensorDeploymentAccessKeyUpdated, and SensorDeploymentAccessKeyReceived activities
2. Verify sensor changes against authorized administrators

## Validation
1. Sign in to the Microsoft 365 Defender portal (https://security.microsoft.com) as a user with the Audit Log or Security Reader role.
2. Navigate to 'Audit' under 'Solutions' > 'Audit'.
3. Set the date range to cover the period of suspected unauthorized sensor changes.
4. In the 'Activities' filter, search for and select the following activities:
   - 'SensorCreated' (under 'Microsoft Defender for Identity')
   - 'SensorDeleted' (under 'Microsoft Defender for Identity')
   - 'SensorDeploymentAccessKeyUpdated' (under 'Microsoft Defender for Identity')
   - 'SensorDeploymentAccessKeyReceived' (under 'Microsoft Defender for Identity')
5. Click 'Search' and review the results. Confirm that only authorized administrator actions appear, and that no unexpected sensor additions, deletions, or key changes are present.
6. If any unexpected activities are found, verify the user who performed the action and ensure it aligns with approved change requests.

## Rollback
1. If an unauthorized sensor was added (SensorCreated):
   - In the Microsoft 365 Defender portal, go to 'Settings' > 'Identities' > 'Sensors'.
   - Select the unauthorized sensor and click 'Delete' to remove it.
2. If an authorized sensor was incorrectly deleted (SensorDeleted):
   - Reinstall the sensor on the affected domain controller or AD FS server using the original deployment package or a newly generated access key.
   - Ensure the sensor appears in the 'Sensors' list and shows a healthy status.
3. If the sensor access key was regenerated (SensorDeploymentAccessKeyUpdated) without authorization:
   - In 'Settings' > 'Identities' > 'Sensors', click 'Regenerate key' to create a new access key.
   - Update the sensor configuration on all deployed sensors with the new key.
4. If the sensor access key was retrieved (SensorDeploymentAccessKeyReceived) by an unauthorized user:
   - Immediately regenerate the access key as described in step 3.
   - Review and revoke any unnecessary permissions for users who retrieved the key.
5. After rollback, re-run the validation steps to confirm the environment is secure and only authorized sensors are active.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
