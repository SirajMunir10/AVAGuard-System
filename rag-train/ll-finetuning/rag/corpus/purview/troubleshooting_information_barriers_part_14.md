# Troubleshooting: Information Barriers

**Domain:** Purview
**Subdomain:** Information Barriers
**Incident Type:** Troubleshooting

## Scenario / Query
Information Barriers policy is not applied to all designated users after defining segments and policies

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Information Barriers policies and segments

## Symptoms
- Policy is applied to some recipients but not to others

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Run the Get-InformationBarrierPoliciesApplicationStatus cmdlet
2. Search the output for text that resembles: Identity: <application guid> Total Recipients: 81527 Failed Recipients: 2 Failure Category: None Status: Complete <application guid>

## Validation
Run the Get-InformationBarrierPoliciesApplicationStatus cmdlet in Exchange Online PowerShell. Examine the output for each policy application entry. Confirm that the 'Status' field is 'Complete', the 'Failure Category' is 'None', and the 'Failed Recipients' count is 0. Additionally, verify that the 'Total Recipients' count matches the expected number of users in the designated segments. If any entry shows a non-zero 'Failed Recipients' or a 'Failure Category' other than 'None', further investigation is needed.

## Rollback
If the policy application fails or causes unintended access issues, run the Remove-InformationBarrierPolicy cmdlet for each policy that was applied. Then, use Remove-InformationBarrierSegment to delete the associated segments. After removal, run Get-InformationBarrierPoliciesApplicationStatus to confirm that the policy application status shows no active policies. Finally, re-create the segments and policies using New-InformationBarrierSegment and New-InformationBarrierPolicy, ensuring correct attribute definitions and user assignments before applying the policy again with Start-InformationBarrierPoliciesApplication.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/information-barriers-troubleshooting>
