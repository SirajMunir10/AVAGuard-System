# Implementation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Implementation

## Scenario / Query
What conditions can be set for a Communication Compliance policy to capture meeting transcripts?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance policy conditions for meeting transcripts

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. If you don't set any conditions, the policy captures transcripts for all meetings
2. You can set one or more of the following policy conditions: Content matches any of these classifiers, Content contains any of these sensitive info types, Message contains any of these words, Message contains none of these words
3. Any other policy conditions are ignored
4. Only sensitive info types, keyword lists, and regulatory Microsoft provided trainable classifiers are detected
5. Regulatory trainable classifiers include: Corporate sabotage, Gifts and entertainment, Money laundering, Regulatory collusion, Stock manipulation, Unauthorized disclosure
6. All other classifiers, including business conduct classifiers, aren't detected

## Validation
1. Confirm the Communication Compliance policy is configured with the desired conditions (e.g., no conditions, or specific classifiers, sensitive info types, or keywords).
2. Verify that meeting transcripts are being captured by checking the policy's reported items in the Microsoft 365 Compliance Center.
3. Run the following PowerShell command to list policy conditions: Get-CommunicationCompliancePolicy -Identity "PolicyName" | Select-Object Conditions
4. Ensure that only supported conditions (sensitive info types, keyword lists, regulatory trainable classifiers) are set; other classifiers should not be present.

## Rollback
1. Remove any unsupported conditions from the policy by editing the policy in the Microsoft 365 Compliance Center.
2. If the policy is capturing unintended transcripts, modify the policy to add a condition (e.g., 'Message contains none of these words') to exclude specific meetings.
3. To revert to capturing all transcripts, remove all conditions from the policy.
4. Use PowerShell to reset conditions: Set-CommunicationCompliancePolicy -Identity "PolicyName" -Conditions @()

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
