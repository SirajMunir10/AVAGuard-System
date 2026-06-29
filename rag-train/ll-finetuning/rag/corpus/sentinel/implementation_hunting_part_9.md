# Implementation: Hunting

**Domain:** Sentinel
**Subdomain:** Hunting
**Incident Type:** Implementation

## Scenario / Query
How to use Jupyter Notebooks in Microsoft Sentinel for complex hunting and investigations?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel Notebooks page

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use Jupyter Notebooks to save queries and data as you go, use variables to rerun queries with different values or dates, or save your queries to rerun on future investigations.
2. Use Jupyter Notebooks to add programming to your queries, including declarative languages like Kusto Query Language (KQL) or SQL, and procedural programming languages to run logic in a series of steps.
3. Link to external data such as data in external services, sensitive data stored within your organization, or data not yet migrated to the cloud.
4. Use Jupyter Notebooks for more visualizations, machine learning libraries, and data processing and transformation features.

## Validation
1. Open Microsoft Sentinel in the Azure portal. 2. Navigate to Threat Management > Notebooks. 3. Confirm that the Notebooks page loads without errors and displays the list of available notebooks. 4. Select a notebook and click 'Launch Notebook' to verify it opens in a new browser tab with the Jupyter environment. 5. In the notebook, run a simple KQL query (e.g., `SecurityEvent | take 10`) and confirm results are returned. 6. Create a new cell with a Python variable and rerun a query using that variable to confirm variable reuse works. 7. Save the notebook and close it, then reopen it from the Notebooks page to confirm persistence.

## Rollback
1. If the Notebooks page fails to load, verify that the Microsoft Sentinel workspace is in a supported region and that the user has the required permissions (Microsoft Sentinel Contributor or Reader). 2. If a notebook fails to launch, check that the underlying Azure Machine Learning workspace is provisioned and accessible. 3. If queries fail, ensure the workspace's Log Analytics workspace is active and that the user has read access to the relevant tables. 4. If variable reuse or saving fails, clear the browser cache and retry, or use an incognito/private browsing session. 5. If issues persist, disable any browser extensions that might interfere with Jupyter and retry.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/hunting>
