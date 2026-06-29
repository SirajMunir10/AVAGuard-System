# Troubleshooting: Information Barriers

**Domain:** Purview
**Subdomain:** Information Barriers
**Incident Type:** Troubleshooting

## Scenario / Query
How to check if Information Barriers policies are applied to a user and which segments they belong to?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Information Barriers policies assigned to segments

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the Get-InformationBarrierRecipientStatus cmdlet together with Identity and Identity2 parameters. This cmdlet returns information about users, such as attribute values and any Information Barriers policies that are applied.
2. Syntax Example: Get-InformationBarrierRecipientStatus -Identity <value> -Identity2 <value>
3. You can use any value that uniquely identifies each user, such as name, alias, distinguished name, canonical domain name, email address, or GUID.
4. Example: Get-InformationBarrierRecipientStatus -Identity meganb -Identity2 alexw
5. Alternatively, use Get-InformationBarrierRecipientStatus -Identity <value> for a single user.
6. Example: Get-InformationBarrierRecipientStatus -Identity jeanp
7. Review the results to learn whether Information Barriers policies are assigned, and to which segments the users belong.

## Validation
Run the following PowerShell cmdlet to confirm Information Barriers policy assignment and segment membership for a user: Get-InformationBarrierRecipientStatus -Identity <user_identity>. For example: Get-InformationBarrierRecipientStatus -Identity jeanp. Verify that the output includes the 'AssignedPolicy' and 'SegmentsAssigned' properties, indicating the policy is applied and the user belongs to the correct segments.

## Rollback
If the remediation fails or causes issues, remove the Information Barriers policy assignment from the user by running: Remove-InformationBarrierPolicy -Identity <policy_identity> -Confirm:$false. Then verify removal with: Get-InformationBarrierRecipientStatus -Identity <user_identity> and confirm that 'AssignedPolicy' is empty.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/information-barriers-troubleshooting>
