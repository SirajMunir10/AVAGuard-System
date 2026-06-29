# Implementation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Implementation

## Scenario / Query
How to use Copilot in Microsoft Purview to summarize a message in Communication Compliance?

## Environment Context
- **Tenant Type:** Microsoft 365 E5/A5/G5 or Compliance add-on
- **Configuration:** Copilot in Microsoft Purview must be onboarded; user must have Communication Compliance, Communication Compliance Analysts, or Communication Compliance Investigators role plus Security Copilot contributor role

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In Communication Compliance, go to the Policies page and open any policy to view policy matches
2. Select a message in the list (parent or child item, but parent is easier)
3. Select Summarize below the message details
4. The Copilot panel opens on the right side and displays a summary of the message

## Validation
1. Confirm the user has the required roles: Communication Compliance, Communication Compliance Analysts, or Communication Compliance Investigators plus Security Copilot contributor role. 2. Navigate to Microsoft Purview > Communication Compliance > Policies page. 3. Open any policy that has policy matches. 4. Select a parent message in the list. 5. Verify that the 'Summarize' button appears below the message details. 6. Click 'Summarize' and confirm the Copilot panel opens on the right side displaying a summary of the message.

## Rollback
1. If the Copilot panel does not open or the summary is not displayed, verify the user has the required roles and that Copilot in Microsoft Purview is onboarded. 2. If the issue persists, close the Copilot panel and refresh the page. 3. If the 'Summarize' button is missing, ensure the policy has at least one message match and that the user is assigned the correct roles. 4. If the summary is incorrect or incomplete, contact Microsoft support for further investigation.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
