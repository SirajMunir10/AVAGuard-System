# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to create a network share group in Microsoft Purview for endpoint DLP settings?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Open Microsoft Purview portal and go to Data Loss Prevention > Overview > settings gear icon in the upper right corner > Data Loss Prevention > Endpoint DLP settings > Network share groups.
2. Select + Create network share group.
3. Enter a Group name.
4. Add the file path to the share.
5. Select Add.
6. Add other share paths to the group as needed.
7. Select Save and then Close.

## Validation
1. In the Microsoft Purview portal, navigate to Data Loss Prevention > Settings > Endpoint DLP settings > Network share groups. 2. Confirm the newly created network share group appears in the list with the correct name and file paths. 3. Optionally, use the 'Test' feature (if available) to verify that the group is recognized in DLP policy evaluation.

## Rollback
1. In the Microsoft Purview portal, navigate to Data Loss Prevention > Settings > Endpoint DLP settings > Network share groups. 2. Select the network share group you created. 3. Click 'Delete' and confirm the deletion. 4. Verify the group is removed from the list.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
