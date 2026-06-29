# Troubleshooting: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Troubleshooting

## Scenario / Query
How do I filter and sort messages in Communication Compliance to investigate policy matches?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance policy configured

## Symptoms
- Messages with policy matches are difficult to review without sorting
- Need to narrow down messages by specific criteria like date, sender, or keywords

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. From the Policy details page, use multilevel filtering for several message fields to investigate and review messages with policy matches.
2. Filter pending and resolved items for each configured policy.
3. Configure filter queries for a policy or configure and save custom and default filter queries for use in each specific policy.
4. After configuring fields for a filter, the filter fields display on the top of the message queue for configuring specific filter values.
5. Key filters (Body/Subject, Date, Sender, and Tags filters) always display on the Pending and Resolved tabs.
6. For the Date filter, note that date and time for events are listed in Coordinated Universal Time (UTC). When filtering, the requesting user's local date/time determines results based on conversion to UTC.
7. To save a filter or filter set as a saved filter query, configure one or more values as filter selections.
8. Use the following filter details: Body/Subject (search for keywords or keyword phrases), Classifiers (built-in and custom classifiers like Targeted Harassment, Profanity, Threat), Date (filter for a single day by selecting a date range starting with the desired day and ending with the following day), Escalated To (user name of person included in escalation action), Message Class (class based on message type: message or attachment), Has Attachment (attachment presence), Source (source based on message type: email, Microsoft Teams chat, Bloomberg, etc.), Language (detected language of text in the message, classified according to language of most message text).

## Validation
1. Navigate to the Microsoft 365 Purview compliance portal > Communication Compliance > Policies. 2. Select the policy you want to investigate. 3. On the Policy details page, verify that the Pending and Resolved tabs are visible. 4. Confirm that the key filters (Body/Subject, Date, Sender, Tags) appear at the top of the message queue. 5. Apply a filter, e.g., set Date to a specific range (start with desired day, end with next day) and verify messages are filtered accordingly. 6. Use the Body/Subject filter to search for a keyword or phrase and confirm results narrow down. 7. Check that you can save a filter set as a saved filter query by configuring one or more values and selecting save. 8. Verify that saved filter queries appear in the policy for reuse.

## Rollback
1. Remove any custom filter queries by deleting the saved filter query from the policy. 2. Clear all active filter fields on the Pending and Resolved tabs to return to the default unfiltered view. 3. If a filter was saved, delete the saved filter query via the filter management option. 4. Reset any date range filters to show all messages (e.g., set a wide date range covering the policy's entire scope). 5. Confirm that the message queue displays all policy matches without any applied filters.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
