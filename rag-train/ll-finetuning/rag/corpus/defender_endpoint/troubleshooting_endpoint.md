# Troubleshooting: Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
Why can't I download a quarantined file from Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** commercial
- **Configuration:** Sample submission setting, user consent configuration

## Symptoms
- Download file button is unavailable or fails.
- Users are prompted to provide explicit consent before backing up the quarantined file.

## Error Codes
N/A

## Root Causes
1. Sample submission is turned off.
2. Automatic sample submission is set to request permission from the user and the user did not agree to send the sample.

## Remediation Steps
1. Ensure sample submission is turned on.
2. If automatic sample submission is set to request permission from the user, ensure the user agrees to send the sample.

## Validation
1. Verify sample submission is enabled: Navigate to Microsoft 365 Defender > Settings > Endpoints > Advanced features. Ensure 'Sample submission' is set to 'On'.
2. Check user consent configuration: In the same Advanced features page, confirm 'Automatic sample submission' is not set to 'Request permission from the user' unless the user has explicitly consented. If set to 'Request permission', verify the user has agreed to submit samples.
3. Test file download: Go to the file's page in Microsoft 365 Defender (e.g., from an alert or device timeline) and click 'Download file'. Confirm the download button is available and the download succeeds without prompts for consent.

## Rollback
1. Disable sample submission: In Microsoft 365 Defender > Settings > Endpoints > Advanced features, set 'Sample submission' to 'Off'.
2. Revert user consent configuration: If automatic sample submission was changed, set it back to 'Request permission from the user' (or the previous setting).
3. Notify users: Inform users that they may again be prompted for consent when attempting to download quarantined files.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-file-alerts>
