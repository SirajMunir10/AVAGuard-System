# Troubleshooting: Incident Management

**Domain:** Sentinel
**Subdomain:** Incident Management
**Incident Type:** Troubleshooting

## Scenario / Query
How does Microsoft Sentinel calculate incident similarity and why might the similar incidents list change between sessions?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with incident investigation enabled

## Symptoms
- Similar incidents list shows different results when revisiting an incident details page
- Incidents are unexpectedly grouped or not grouped as similar

## Error Codes
N/A

## Root Causes
1. Incident similarity is recalculated every time you enter the incident details page
2. Similarity calculation is based on data from the 14 days prior to the last activity in the incident (end time of the most recent alert)
3. New incidents created or updated between sessions can change similarity results

## Remediation Steps
1. Review the Similarity reason column to understand why an incident is listed as similar
2. Hover over the info icon to show common items (entities, rule name, or details)

## Validation
Check the Similarity reason column and hover over the info icon to confirm common entities, rule name, or details

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/investigate-cases>
