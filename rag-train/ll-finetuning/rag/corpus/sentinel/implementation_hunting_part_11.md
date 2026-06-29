# Implementation: Hunting

**Domain:** Sentinel
**Subdomain:** Hunting
**Incident Type:** Implementation

## Scenario / Query
How to use MSTICPy for security investigations and hunting in Jupyter Notebooks within Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with Jupyter Notebooks enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Query log data from multiple sources using MSTICPy.
2. Enrich the data with threat intelligence, geolocations, and Azure resource data.
3. Extract Indicators of Activity (IoA) from logs, and unpack encoded data.
4. Perform sophisticated analyses such as anomalous session detection and time series decomposition.
5. Visualize data using interactive timelines, process trees, and multi-dimensional Morph Charts.
6. Use time-saving notebook tools such as widgets that set query time boundaries, select and display items from lists, and configure the notebook environment.

## Validation
1. Open the Jupyter Notebook in Microsoft Sentinel and run the MSTICPy initialization cell: `import msticpy; msticpy.init_notebook(namespace=globals())`. Verify no errors. 2. Execute a query against a log source (e.g., `query = 'SecurityEvent | take 10'; data = msticpy.query(query)`). Confirm data is returned. 3. Enrich data with threat intelligence: `data = data.mp_tilookup()`. Check that enrichment columns appear. 4. Run an anomaly detection function (e.g., `msticpy.anomalous_session(data)`). Verify output includes flagged sessions. 5. Generate a visualization (e.g., `data.mp_timelineplot()`) and confirm an interactive timeline renders. 6. Use a notebook widget (e.g., `msticpy.widgets.QueryTime(units='day')`) and verify the widget displays and updates query boundaries.

## Rollback
1. If MSTICPy import fails, reinstall the package: `!pip install msticpy --upgrade` and restart the kernel. 2. If queries fail, verify the workspace connection: `msticpy.settings.get_config('WorkspaceId')` and ensure the correct workspace ID is set. 3. If enrichment fails, check threat intelligence provider settings: `msticpy.settings.get_config('TIProviders')` and reconfigure if needed. 4. If anomaly detection errors, revert to a simpler analysis (e.g., `data.describe()`) and review function parameters. 5. If visualizations do not render, downgrade Plotly: `!pip install plotly==5.9.0` and restart kernel. 6. If widgets malfunction, reset the notebook environment: `%reset -f` and re-run initialization cells.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/hunting>
- <https://msticpy.readthedocs.io/en/latest/>
- <https://learn.microsoft.com/en-us/azure/sentinel/notebooks>
- <https://learn.microsoft.com/en-us/azure/sentinel/notebooks-msticpy-advanced>
