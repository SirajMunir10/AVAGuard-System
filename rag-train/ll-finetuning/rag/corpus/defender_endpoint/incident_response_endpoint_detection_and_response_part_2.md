# Incident Response: Endpoint Detection and Response

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Detection and Response
**Incident Type:** Incident Response

## Scenario / Query
How to collect an investigation package from a device in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Device page with response actions enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Collect investigation package from the row of response actions at the top of the device page.
2. Specify in the text box why you want to perform this action.
3. Select Confirm.
4. The zip file downloads.
5. Alternatively: Select Collect Investigation Package from the response actions section of the device page.
6. Add comments and then select Confirm.
7. Select Action center from the response actions section of the device page.
8. Select Package collection package available to download the collection package.

## Validation
1. Navigate to the device page in Microsoft Defender for Endpoint. 2. Verify that the 'Collect investigation package' action is available in the response actions row. 3. Initiate the collection by selecting the action, providing a reason, and confirming. 4. Check the Action center for a 'Package collection package available' status. 5. Download the zip file and confirm it is a valid, non-empty archive containing expected investigation data (e.g., event logs, registry hives, memory dump).

## Rollback
1. If the investigation package download fails or is corrupted, delete the downloaded zip file. 2. In the Action center, if the action is still pending, cancel the 'Collect investigation package' action if the cancel option is available. 3. Re-initiate the collection from the device page, ensuring the device is online and response actions are enabled. 4. If the issue persists, verify device connectivity and that the device is not in an error state by checking the device timeline and health status.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
