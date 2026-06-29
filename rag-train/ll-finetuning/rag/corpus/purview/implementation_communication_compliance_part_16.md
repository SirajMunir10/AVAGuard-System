# Implementation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Implementation

## Scenario / Query
How to tag a message as Compliant, Noncompliant, or Questionable in Communication Compliance?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance message review

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Tag the message as Compliant, Noncompliant, or Questionable as it relates to the policies and standards for your organization.
2. You can also create a custom tag.
3. Adding tags and tagging comments helps you micro-filter messages for escalations or as part of other internal review processes.
4. After tagging is complete, you can also choose to resolve the message to move it out of the pending queue.
5. You can filter on any tag value.

## Validation
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) with appropriate permissions. 2. Navigate to Communication Compliance > Policies > open the relevant policy. 3. Select the Pending tab and locate a message that was tagged. 4. Verify the tag value (Compliant, Noncompliant, or Questionable) is displayed in the Tag column for that message. 5. (Optional) Apply a filter on the Tag column to confirm only messages with that tag appear. 6. If a custom tag was created, confirm it appears in the tag dropdown when reviewing a message.

## Rollback
1. Sign in to the Microsoft Purview compliance portal (https://compliance.microsoft.com) with appropriate permissions. 2. Navigate to Communication Compliance > Policies > open the relevant policy. 3. Select the Pending tab and locate the incorrectly tagged message. 4. Open the message details and change the tag back to the original value (or remove the tag by selecting 'None'). 5. If a custom tag was created and needs to be removed, navigate to the policy settings and delete the custom tag from the tag list. 6. If the message was resolved after tagging, use the Resolved tab to find the message, reopen it, and adjust the tag as needed.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
