# Incident Response: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Incident Response

## Scenario / Query
How to take response actions on a machine in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint Plan 1 or Plan 2
- **Configuration:** Manual response actions enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. See also Take response actions on a file
2. Manual response actions in Microsoft Defender for Endpoint Plan 1
3. Report inaccuracy

## Validation
1. In Microsoft Defender for Endpoint, navigate to the device page for the target machine. 2. Confirm that the 'Actions' menu displays the expected response actions (e.g., 'Run antivirus scan', 'Initiate automated investigation', 'Collect investigation package', 'Initiate Live Response session', 'Isolate device', 'Restrict app execution', 'Run antivirus scan', 'Run full scan', 'Run quick scan'). 3. Execute a test action (e.g., 'Run quick scan') and verify that the action is accepted and appears in the device's action history with a status of 'Pending' or 'Completed'. 4. Check the Microsoft 365 Defender portal's action center to confirm the action is listed and its status is as expected.

## Rollback
1. If a response action (e.g., device isolation) was applied and causes issues, navigate to the device page in Microsoft Defender for Endpoint. 2. From the 'Actions' menu, select the corresponding rollback action (e.g., 'Release from isolation'). 3. Confirm the rollback action is accepted and monitor the device's status to ensure it returns to its previous state. 4. Verify in the action center that the rollback action completed successfully and the device is no longer in the isolated state.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
