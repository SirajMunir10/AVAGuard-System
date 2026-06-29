# Troubleshooting: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Troubleshooting

## Scenario / Query
How to view the detected language classification for a message in Communication Compliance?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance policy

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select a message.
2. Select View message details.
3. Scroll to the EmailDetectedLanguage field.

## Validation
1. In the Microsoft 365 Purview compliance portal, navigate to Communication Compliance > Policies and select the relevant policy.
2. Open the policy and locate a message that was classified under the policy.
3. Select the message and click 'View message details'.
4. Scroll to the 'EmailDetectedLanguage' field and confirm it displays the expected language classification (e.g., 'en' for English).
5. Verify that the language classification matches the actual language of the message content.

## Rollback
1. If the 'EmailDetectedLanguage' field is missing or incorrect, verify that the Communication Compliance policy is correctly configured to include language detection (e.g., ensure the policy is assigned to appropriate users and includes conditions for language classification).
2. If the issue persists, review the message's raw properties using the Microsoft 365 Defender portal or Exchange admin center to check for any transport rule or data classification conflicts.
3. As a last resort, remove and recreate the Communication Compliance policy with default language detection settings, then reassign it to the same users and groups.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
