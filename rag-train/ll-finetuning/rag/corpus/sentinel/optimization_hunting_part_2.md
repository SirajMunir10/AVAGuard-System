# Optimization: Hunting

**Domain:** Sentinel
**Subdomain:** Hunting
**Incident Type:** Optimization

## Scenario / Query
How are out-of-the-box hunting queries in Microsoft Sentinel developed and maintained to detect new attacks?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with hunting queries

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Microsoft security researchers continuously develop new hunting queries and fine-tune existing ones.
2. New queries are added to security solutions to provide an entry point for looking for new detections and attacks.

## Validation
1. In the Microsoft Sentinel workspace, navigate to the 'Hunting' blade. 2. Review the list of queries and note the presence of any newly added out-of-the-box queries (e.g., queries with recent timestamps or version updates). 3. Select a sample of new queries and run them against sample data to confirm they execute without errors and return expected results. 4. Compare the current query list with a baseline (e.g., from a previous export) to verify that new queries have been added and existing ones updated as per Microsoft's continuous development.

## Rollback
1. If newly added queries cause performance issues or false positives, identify the specific queries by name or ID. 2. For each problematic query, either disable it by setting its 'Enabled' property to 'false' via Azure Resource Graph or PowerShell (e.g., using the 'Update-AzSentinelHuntingQuery' cmdlet), or delete it using 'Remove-AzSentinelHuntingQuery'. 3. If fine-tuned existing queries need to be reverted, restore the previous version from a backup or re-import the original query definition from a saved JSON file. 4. Verify that the rollback actions have taken effect by re-running the validation steps and confirming the query list matches the pre-remediation state.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/hunting>
