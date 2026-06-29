# Implementation: Security Copilot Integration

**Domain:** Defender for Endpoint
**Subdomain:** Security Copilot Integration
**Incident Type:** Implementation

## Scenario / Query
How can SOC analysts use the Defender Chat experience (preview) to investigate threats without writing complex queries?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 or Defender for Endpoint Plan 2
- **Configuration:** Security Copilot provisioned and Defender Chat experience (preview) enabled.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the open prompt chat assistant built into Microsoft Defender.
2. Ask security questions in plain language to investigate threats, explore incidents, and answer security questions.

## Validation
1. Confirm that Security Copilot is provisioned and the Defender Chat experience (preview) is enabled: In the Microsoft 365 Defender portal, navigate to Settings > Microsoft 365 Defender > Security Copilot. Verify that the toggle for 'Security Copilot' is set to On and that the 'Defender Chat experience (preview)' is enabled. 2. Validate that a SOC analyst can access the chat assistant: Open the Microsoft 365 Defender portal (https://security.microsoft.com) and ensure the chat icon (speech bubble) is visible in the top-right corner. Click the icon to open the Defender Chat pane. 3. Test plain-language query functionality: In the chat pane, type a natural language question such as 'Show me all high-severity incidents from the last 24 hours' and press Enter. Confirm that the assistant returns relevant incident data without requiring KQL or complex syntax. 4. Verify investigation capabilities: Ask a follow-up question like 'What is the status of incident 123?' and confirm that the assistant provides details including affected devices, alerts, and recommended actions. 5. Check that responses include source references: Ensure that any data returned by the chat assistant includes citations or links to the underlying Microsoft Defender data (e.g., incident pages, device timelines).

## Rollback
1. Disable the Defender Chat experience (preview): In the Microsoft 365 Defender portal, go to Settings > Microsoft 365 Defender > Security Copilot. Set the toggle for 'Security Copilot' to Off, or uncheck 'Enable Defender Chat experience (preview)' if the option is separate. 2. Remove Security Copilot provisioning (if necessary): In the Microsoft 365 admin center, navigate to Billing > Licenses, select the Security Copilot add-on, and remove the license assignment from affected users. 3. Verify that the chat icon is no longer visible: Log out of the Microsoft 365 Defender portal and log back in. Confirm that the chat icon (speech bubble) is absent from the top-right corner. 4. Test that plain-language queries are disabled: Attempt to open the chat pane (e.g., by pressing Ctrl+Shift+C or clicking where the icon was). Confirm that no chat interface appears or that an error message indicates the feature is unavailable. 5. If rollback is due to performance or data issues, contact Microsoft Support to report the problem and request further assistance.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/security-copilot-in-microsoft-365-defender>
