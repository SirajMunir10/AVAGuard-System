# Implementation: Hunting

**Domain:** Sentinel
**Subdomain:** Hunting
**Incident Type:** Implementation

## Scenario / Query
How to use Jupyter Notebooks with Python capabilities for threat hunting in Microsoft Sentinel?

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
1. Use pandas for data processing, cleanup, and engineering
2. Use Matplotlib, HoloViews, and Plotly for visualization
3. Use NumPy and SciPy for advanced numerical and scientific processing
4. Use scikit-learn for machine learning
5. Use TensorFlow, PyTorch, and Keras for deep learning
6. Use magics to mix languages within the same notebook, allowing execution of individual cells using another language (e.g., retrieve data using a PowerShell script cell, process data in Python, and use JavaScript to render a visualization)

## Validation
1. Open the Jupyter Notebook in Microsoft Sentinel and run a cell that imports pandas, matplotlib, numpy, scikit-learn, and tensorflow. Verify no import errors occur.
2. Execute a cell that uses pandas to load sample data from the workspace (e.g., using the msticpy library) and perform a data cleanup operation. Confirm the output shows the expected cleaned DataFrame.
3. Create a visualization using matplotlib or plotly within a notebook cell and render it inline. Ensure the chart displays correctly.
4. Run a cell that uses a magic command (e.g., %%powershell) to retrieve data, then process it in Python, and render it with JavaScript. Verify the cell executes without errors and the final output is displayed.

## Rollback
1. If a notebook fails to open or run, close the notebook without saving changes and reopen it from the Sentinel workspace.
2. If a specific library import fails, remove or comment out the import line and restart the kernel (Kernel > Restart & Clear Output).
3. If a visualization does not render, check that the notebook is trusted (File > Trust Notebook) and that the output is not suppressed. If needed, re-run the cell with explicit display commands (e.g., plt.show()).
4. If a magic command causes an error, delete the cell containing the magic command and recreate it using only Python cells. Restart the kernel and re-run the notebook.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/hunting>
