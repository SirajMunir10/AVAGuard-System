# Implementation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Implementation

## Scenario / Query
How to assign required permissions to investigate and remediate communication compliance alerts?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance policies configured

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Assign users the Communication Compliance Analysts or the Communication Compliance Investigators role group
2. Assign users the Reviewer role in the policy that is associated with the alert

## Validation
1. In the Microsoft 365 Defender portal, go to Roles & scopes > Roles > Microsoft Entra roles and verify that the user is a member of either the Communication Compliance Analysts or Communication Compliance Investigators role group. 2. In the Communication Compliance solution, open the specific policy associated with the alert, go to the Reviewers section, and confirm the user is listed as a Reviewer. 3. As the user, navigate to the Communication Compliance alerts page and confirm they can view and act on the alert.

## Rollback
1. In the Microsoft 365 Defender portal, go to Roles & scopes > Roles > Microsoft Entra roles, select the Communication Compliance Analysts or Communication Compliance Investigators role group, and remove the user from the group. 2. In the Communication Compliance solution, open the policy associated with the alert, go to the Reviewers section, and remove the user from the list of reviewers.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
