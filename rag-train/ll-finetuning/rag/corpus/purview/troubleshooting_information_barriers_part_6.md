# Troubleshooting: Information Barriers

**Domain:** Purview
**Subdomain:** Information Barriers
**Incident Type:** Troubleshooting

## Scenario / Query
How do I determine whether users are affected by an Information Barriers policy?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Information Barriers policies configured

## Symptoms
- Users may be unable to communicate with certain other users

## Error Codes
N/A

## Root Causes
1. Information Barriers policy may be blocking communication as intended
2. Policy may need refinement

## Remediation Steps
1. Use the Get-InformationBarrierRecipientStatus cmdlet together with the Identity parameter. Syntax: Get-InformationBarrierRecipientStatus -Identity <identity value>. You can use any identity value that uniquely identifies each recipient, such as Name, Alias, Distinguished name (DN), Canonical DN, Email address, or GUID.
2. Example: Get-InformationBarrierRecipientStatus -Identity meganb (using an alias for the Identity parameter). This cmdlet returns information that indicates whether the user is affected by an Information Barriers policy. Look for *ExoPolicyId: <GUID>.
3. If the users aren't included in Information Barriers policies, contact Microsoft Support. Otherwise, go to the next step.

## Validation
Run the following PowerShell command to confirm whether a specific user is affected by an Information Barriers policy: Get-InformationBarrierRecipientStatus -Identity <user alias or email>. Verify that the output includes an ExoPolicyId field with a GUID value. If ExoPolicyId is present, the user is affected by a policy. Repeat for each user in question.

## Rollback
If the remediation (e.g., policy refinement) causes unintended blocking or unblocking, revert the policy changes using the Set-InformationBarrierPolicy cmdlet to restore the previous policy configuration. For example: Set-InformationBarrierPolicy -Identity <PolicyId> -State Inactive. Then run Start-InformationBarrierPoliciesApplication to apply the rollback. If the original policy state is unknown, contact Microsoft Support for assistance.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/information-barriers-troubleshooting>
