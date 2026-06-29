# Troubleshooting: Information Barriers

**Domain:** Purview
**Subdomain:** Information Barriers
**Incident Type:** Troubleshooting

## Scenario / Query
How to check the status of an Information Barriers policy application and troubleshoot failures?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Information Barriers policies applied via Start-InformationBarrierPoliciesApplication

## Symptoms
- Policy application is not started, failed, or in progress

## Error Codes
N/A

## Root Causes
1. Policy definitions contain errors
2. Application didn't start for some other reason
3. Users assigned to more than one segment
4. Segments assigned more than one policy

## Remediation Steps
1. Run Get-InformationBarrierPoliciesApplicationStatus to view the status of the most recent policy application
2. Run Get-InformationBarrierPoliciesApplicationStatus -All $true to view all policy applications
3. If status is 'Not started' and more than 45 minutes have passed since Start-InformationBarrierPoliciesApplication was run, review the audit log to see whether policy definitions contain any errors or the application didn't start for some other reason
4. If status is 'Failed', review the audit log, review segments and policies to check if any users are assigned to more than one segment or any segments are assigned more than one policy, then edit segments or edit policies and run Start-InformationBarrierPoliciesApplication again
5. If status is 'In progress', allow more time for it to finish; if several days have passed, gather audit logs and contact Microsoft Support

## Validation
Run Get-InformationBarrierPoliciesApplicationStatus to check the status of the most recent policy application. If the status is 'Complete', the remediation succeeded. Optionally, run Get-InformationBarrierPoliciesApplicationStatus -All $true to confirm all applications are in a completed state.

## Rollback
If the remediation fails or causes issues, review the audit log to identify errors in policy definitions or application failures. Check segments and policies to ensure no user is assigned to more than one segment and no segment is assigned more than one policy. Edit segments or policies as needed, then run Start-InformationBarrierPoliciesApplication again to reapply the corrected policies.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/information-barriers-troubleshooting>
