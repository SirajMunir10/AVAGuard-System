# Incident Response: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Incident Response

## Scenario / Query
How do I investigate and remediate a DLP policy match in Microsoft Purview where sensitive data was shared externally via email?

## Environment Context
- **Tenant Type:** Microsoft 365 E5
- **Configuration:** DLP policy configured to detect and block sharing of credit card numbers via email; policy mode set to 'Test with notifications'

## Symptoms
- User receives a DLP policy tip notification that their email contains sensitive information
- DLP incident appears in the Microsoft 365 Defender portal under Incidents & alerts
- Activity Explorer shows a DLP rule match for 'Credit Card Number' with action 'Block'

## Error Codes
N/A

## Root Causes
1. A user attempted to send an email containing credit card numbers to an external recipient
2. The DLP policy was configured to block such sharing but was in test mode, so the email was not actually blocked

## Remediation Steps
1. 1. In the Microsoft 365 Defender portal, go to Incidents & alerts > Incidents and select the DLP incident
2. 2. Review the alert details to identify the user, the sensitive information type, and the action taken
3. 3. Use Activity Explorer to view the full audit record of the DLP rule match
4. 4. If the email was not blocked, use Microsoft Purview eDiscovery to search for and delete the message from the user's mailbox
5. 5. Update the DLP policy to change the mode from 'Test' to 'Enforce' to prevent future occurrences
6. 6. Notify the user about the policy and provide training on handling sensitive data

## Validation
Confirm that the DLP policy is now in 'Enforce' mode by running Get-DlpCompliancePolicy in Exchange Online PowerShell and verifying the Mode parameter is set to 'Enforce'.

## Rollback
If the policy change causes unintended blocks, revert the mode to 'Test with notifications' using Set-DlpCompliancePolicy -Identity 'PolicyName' -Mode TestWithNotifications

## References
- <https://learn.microsoft.com/en-us/purview/dlp-investigate-incidents>
- <https://learn.microsoft.com/en-us/powershell/module/exchange/get-dlpcompliancepolicy>
