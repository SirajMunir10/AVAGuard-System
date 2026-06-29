# Remediation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Remediation

## Scenario / Query
How to escalate a message for eDiscovery (Premium) investigation in Communication Compliance?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance policy

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use Escalate for investigation to create a new eDiscovery (Premium) case for single or multiple messages.
2. Provide a name and notes for the new case.
3. The custodian is automatically filled in for you.
4. You don't need any additional permissions to manage the case.
5. Creating a case doesn't resolve or create a new tag for the message.
6. You can select a total of 100 messages when creating an eDiscovery (Premium) case during the remediation process.
7. Messages in all communication channels included in Communication Compliance are supported. For example, you could select 50 Microsoft Teams chats, 25 Exchange Online email messages, and 25 Viva Engage messages when you open a new eDiscovery (Premium) case for a user.

## Validation
1. Navigate to Microsoft Purview compliance portal > Communication Compliance > Policies. 2. Open the policy that was used for remediation. 3. Go to the 'Pending' or 'Resolved' tab and locate the message(s) that were escalated. 4. Confirm that the 'Escalate for investigation' action was taken and that a new eDiscovery (Premium) case was created. 5. In the eDiscovery (Premium) solution, verify the new case exists with the name and notes provided. 6. Check that the custodian field is automatically populated with the user associated with the message. 7. Ensure the message(s) are included in the case and that the total number of messages does not exceed 100. 8. Confirm that the original message in Communication Compliance still retains its existing tag (e.g., 'Pending' or 'Resolved') and that no new tag was created.

## Rollback
1. In Microsoft Purview compliance portal, navigate to eDiscovery (Premium) > Cases. 2. Locate the case created during the escalation. 3. Delete the case by selecting it and choosing 'Delete case'. 4. Confirm deletion when prompted. 5. Return to Communication Compliance > Policies > the relevant policy. 6. Verify that the message(s) are no longer associated with an eDiscovery case and that their tag remains unchanged. 7. If needed, re-tag the message(s) manually to the appropriate status (e.g., 'Pending' or 'Resolved').

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
