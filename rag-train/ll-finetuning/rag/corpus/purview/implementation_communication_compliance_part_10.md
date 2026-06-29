# Implementation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Implementation

## Scenario / Query
How do I use Copilot to summarize a flagged message in Communication Compliance?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Copilot in Microsoft Purview

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select one of the suggested prompts at the bottom of the panel to use Copilot to create the summary. For example, if the classifier that flagged a message is Stock manipulation, select 'Summarize this message and supported attachments in the context of Stock manipulation category detected'
2. You can also enter an open-ended question in the 'Ask a question' box

## Validation
1. Open the Microsoft Purview compliance portal and navigate to Communication Compliance > Cases. 2. Select a case containing a flagged message. 3. Open the flagged message details. 4. In the Copilot panel, verify that the suggested prompts appear at the bottom (e.g., 'Summarize this message and supported attachments in the context of Stock manipulation category detected'). 5. Click one of the suggested prompts and confirm that a summary is generated. 6. Alternatively, type an open-ended question in the 'Ask a question' box and verify that Copilot returns a relevant response.

## Rollback
1. If the Copilot summary is incorrect or not helpful, close the Copilot panel by clicking the 'X' or 'Close' button. 2. Manually review the flagged message and attachments without using Copilot. 3. If Copilot fails to load or respond, refresh the page and try again. 4. If the issue persists, verify that the user has the required license and role (e.g., Communication Compliance Admin) as per Microsoft documentation. 5. If necessary, disable Copilot for Communication Compliance via the Purview settings (if available) and rely on manual investigation.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
