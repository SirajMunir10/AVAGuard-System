# Troubleshooting: Incident Management

**Domain:** Sentinel
**Subdomain:** Incident Management
**Incident Type:** Troubleshooting

## Scenario / Query
How to search for a specific incident in Microsoft Sentinel when it is not appearing in the default results?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace

## Symptoms
- Incident not found in the incidents grid using basic search
- Search results do not include the expected incident

## Error Codes
N/A

## Root Causes
1. Search parameters are limited to default fields: Incident ID, Title, Tags, Owner, and Product name
2. Advanced search parameters may not be selected
3. Search string may be case sensitive
4. Cross-workspace views do not support advanced searches
5. Only 50 results are displayed at a time when using advanced search parameters

## Remediation Steps
1. Enter a search string in the search box above the incidents grid and press Enter
2. If the incident is not included, select the Search button to modify search parameters
3. In the search pane, scroll down to select one or more additional parameters to search
4. Select Apply to update the search parameters
5. If too many results appear, add more filters to narrow down
6. If unable to find the incident, remove search parameters to expand the search
7. To reset to default parameters, select Set to default

## Validation
The search button color changes: grey when only default parameters are selected, blue when advanced parameters are selected

## Rollback
Select Set to default to reset the selected parameters to the default option

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/investigate-cases>
