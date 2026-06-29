# Implementation: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Implementation

## Scenario / Query
How to respond to detected attacks by stopping and quarantining files or blocking a file in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint Plan 2
- **Configuration:** File detailed profile page with new page layout toggle

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the file's detailed profile page.
2. Toggle to the new page layout if needed using the 'new File page' option.
3. Use response actions available at the top of the file page: Stop and quarantine file, Manage indicator, Download file, Collect file, Ask Defender Experts, Manual actions, Deep analysis.
4. For deep analysis, select the Deep analysis action to submit the file for analysis in a secure cloud sandbox.
5. Check activity details in the Action center after taking action.

## Validation
1. Navigate to the file's detailed profile page and confirm the new page layout is active (if toggled).
2. Verify that the 'Stop and quarantine file' action was successfully executed by checking the Action center (https://security.microsoft.com/action-center) for a completed action with status 'Succeeded'.
3. Confirm the file is no longer accessible on the affected device by attempting to access or execute the file (should be blocked/quarantined).
4. If a file indicator was added (block/allow), verify the indicator appears in the Indicators list under Settings > Endpoints > Indicators.
5. For deep analysis, check the Deep analysis report in the file's profile page to confirm the analysis completed and results are available.

## Rollback
1. If the file was incorrectly quarantined, restore it from quarantine: In the Action center, find the 'Stop and quarantine file' action and select 'Undo' (if available) or manually restore the file from quarantine via the device's local quarantine or using Microsoft Defender for Endpoint's 'Restore file from quarantine' action.
2. If a file indicator was added and needs to be removed, go to Settings > Endpoints > Indicators, locate the indicator, and delete it.
3. If the new page layout caused issues, toggle back to the old page layout using the 'new File page' toggle.
4. If deep analysis was submitted and needs to be canceled, note that deep analysis cannot be canceled once submitted; wait for completion and disregard results if not needed.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-file-alerts>
