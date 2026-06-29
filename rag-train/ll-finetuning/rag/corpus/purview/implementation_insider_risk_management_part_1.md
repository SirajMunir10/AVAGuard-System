# Implementation: Insider Risk Management

**Domain:** Purview
**Subdomain:** Insider Risk Management
**Incident Type:** Implementation

## Scenario / Query
How do I create and manage cases in Microsoft Purview Insider Risk Management?

## Environment Context
- **Tenant Type:** Microsoft 365 with Purview Insider Risk Management licensed
- **Configuration:** Role-based access controls and audit logs enabled; policies configured to generate alerts

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create cases manually from alerts when you need to take extra steps to address a compliance-related issue for a user.
2. Each case focuses on one user. You can add multiple alerts for that user to an existing case or start a new case.
3. After investigating the details of a case, take action by: Sending the user a notice; Resolving the case as benign; Sharing the case with your ServiceNow instance or with an email recipient; Escalating the case for an eDiscovery (Premium) investigation.

## Validation
1. Confirm that the user has the 'Insider Risk Management' role group assigned (e.g., 'Insider Risk Management Admins' or 'Insider Risk Management Analysts').
2. Navigate to Microsoft Purview compliance portal > Insider Risk Management > Cases. Verify that the newly created case appears in the list with the correct user and associated alerts.
3. Open the case and confirm that the alerts linked to the user are displayed under the 'Alerts' tab.
4. Test each action: Send a notice to the user and verify the notice is recorded in the case history; Resolve the case as benign and confirm the status changes to 'Resolved'; Share the case via email or ServiceNow and verify the sharing action is logged; Escalate the case for eDiscovery (Premium) and confirm the case appears in Microsoft Purview eDiscovery (Premium).
5. Review the audit log for actions taken on the case (e.g., 'CaseCreated', 'NoticeSent', 'CaseResolved', 'CaseShared', 'CaseEscalated').

## Rollback
1. If a case was created in error, navigate to the case in Insider Risk Management > Cases, select the case, and choose 'Delete case' from the actions menu. Confirm deletion.
2. If a notice was sent in error, there is no direct recall. Instead, send a follow-up notice to the user clarifying the error, and document the correction in the case notes.
3. If a case was resolved as benign incorrectly, reopen the case by selecting 'Reopen case' from the case actions menu.
4. If a case was shared incorrectly, remove the sharing configuration: For email sharing, no automated removal exists; contact the recipient to disregard. For ServiceNow, remove the case reference from the ServiceNow connector settings in Purview.
5. If a case was escalated to eDiscovery (Premium) in error, remove the case from eDiscovery (Premium) by navigating to eDiscovery (Premium) > Cases, selecting the case, and choosing 'Close case' or 'Delete case' as appropriate.

## References
- <https://learn.microsoft.com/en-us/purview/insider-risk-management-cases>
