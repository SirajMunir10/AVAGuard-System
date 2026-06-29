# Hardening: Microsoft Defender for Cloud

**Domain:** Azure
**Subdomain:** Microsoft Defender for Cloud
**Incident Type:** Hardening

## Scenario / Query
An Azure subscription shows a high number of unassigned critical and high severity security recommendations in Microsoft Defender for Cloud. How can an administrator systematically assign ownership and track remediation of these hardening recommendations?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Defender for Cloud enabled on the subscription; at least one recommendation with 'Unassigned' owner status

## Symptoms
- Security recommendations in Microsoft Defender for Cloud display 'Owner' as 'Unassigned'
- No progress is made on remediating critical or high severity recommendations over time
- Security team cannot identify who is responsible for fixing specific hardening issues

## Error Codes
N/A

## Root Causes
1. Recommendation owners have not been assigned in Defender for Cloud
2. No process exists to assign and track remediation responsibilities

## Remediation Steps
1. Navigate to Microsoft Defender for Cloud > Recommendations.
2. Select a recommendation that shows 'Owner: Unassigned'.
3. In the recommendation details pane, select 'Assign owner'.
4. Enter the Azure AD user or group responsible for remediation and set a due date.
5. Optionally, add a note describing the remediation plan.
6. Repeat for all critical and high severity recommendations.
7. Use the 'Owner' filter in the recommendations list to monitor assigned vs. unassigned items.

## Validation
After assignment, the recommendation's 'Owner' field displays the assigned user or group, and the recommendation appears in the assignee's 'My tasks' view in Defender for Cloud.

## Rollback
To remove an owner assignment, go to the recommendation, select 'Assign owner', and clear the owner field. This reverts the owner to 'Unassigned'.

## References
- <https://learn.microsoft.com/en-us/azure/defender-for-cloud/recommendations-assign-owner>
