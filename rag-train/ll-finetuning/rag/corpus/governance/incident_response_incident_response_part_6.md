# Incident Response: Incident Response

**Domain:** Governance
**Subdomain:** Incident Response
**Incident Type:** Incident Response

## Scenario / Query
A security administrator suspects that an attacker has compromised a user account and is using it to perform unauthorized actions in the Microsoft 365 environment. How should the administrator use Microsoft Purview Compliance Manager to assess the organization's incident response readiness and identify gaps in the incident response controls?

## Environment Context
- **Tenant Type:** Microsoft 365 E5
- **Configuration:** Microsoft Purview Compliance Manager is enabled with default assessment templates for incident response controls.

## Symptoms
- Unusual sign-in activity from a user account
- Suspicious email forwarding rules created by the user
- Multiple failed sign-in attempts followed by a successful sign-in from an unfamiliar IP address

## Error Codes
N/A

## Root Causes
1. The organization has not completed or reviewed its incident response controls in Compliance Manager
2. Incident response procedures are not documented or tested
3. Lack of automated detection and response mechanisms

## Remediation Steps
1. Navigate to Microsoft Purview compliance portal > Compliance Manager > Assessments
2. Select the assessment template that includes incident response controls (e.g., Microsoft 365 baseline or a custom assessment)
3. Review the control actions under 'Incident Response' to identify which controls are not implemented or not tested
4. For each unimplemented control, assign an owner and set a target implementation date
5. Implement the missing controls according to the detailed guidance provided in Compliance Manager for each control action
6. After implementation, update the control status in Compliance Manager and provide evidence of implementation
7. Schedule regular testing of incident response procedures and update the assessment accordingly

## Validation
In Compliance Manager, verify that all incident response controls show a status of 'Implemented' and that the overall compliance score for incident response meets the organization's target.

## Rollback
If a control implementation causes issues, revert the specific configuration change and update the control status in Compliance Manager to 'Not implemented' with a note explaining the rollback.

## References
- <https://learn.microsoft.com/en-us/purview/compliance-manager-setup>
- <https://learn.microsoft.com/en-us/purview/compliance-manager-assessments>
