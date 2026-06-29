# Troubleshooting: Threat Intelligence

**Domain:** Sentinel
**Subdomain:** Threat Intelligence
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve a failed bulk export operation of threat intelligence objects in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Warning when opening the Export side panel
- System pauses subsequent operations

## Error Codes
N/A

## Root Causes
1. A known issue exists where the bulk operation sometimes fails

## Remediation Steps
1. Open the Export side panel
2. Remove the failed action from the bulk operations history view

## Validation
1. Open the Export side panel in Microsoft Sentinel. 2. In the bulk operations history view, confirm that the failed action is no longer listed. 3. Attempt a new bulk export operation and verify that no warning appears and the operation completes without error.

## Rollback
1. If the issue persists or reoccurs, open the Export side panel. 2. In the bulk operations history view, check for any remaining failed actions. 3. If a failed action is present, remove it again. 4. If the problem continues, contact Microsoft Support for further assistance.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/work-with-threat-indicators>
