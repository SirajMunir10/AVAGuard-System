# Implementation: Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint
**Incident Type:** Implementation

## Scenario / Query
How to download quarantined files from Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** commercial
- **Configuration:** Sample submission configurations, geo settings (EU, UK, US)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the file's detail page and click the 'Download file' button.
2. Ensure the 'Download quarantined files' setting is turned on (default). To adjust, go to Settings > Endpoints > Advanced features > Download quarantined files.
3. Ensure sample submission is turned on.
4. If automatic sample submission is set to request permission from the user, only samples that the user agrees to send are collected.

## Validation
1. Navigate to the file's detail page in Microsoft Defender for Endpoint and confirm the 'Download file' button is visible and clickable.
2. Go to Settings > Endpoints > Advanced features and verify 'Download quarantined files' is toggled On.
3. Check that sample submission is enabled under Settings > Endpoints > Advanced features > Sample submission.
4. If sample submission is set to 'Request permission from the user', confirm that the user has consented to sample collection for the specific file.

## Rollback
1. If the 'Download file' button is missing or disabled, re-enable 'Download quarantined files' under Settings > Endpoints > Advanced features.
2. If sample submission is off, turn it on under Settings > Endpoints > Advanced features > Sample submission.
3. If sample submission is set to 'Request permission from the user' and no consent was given, change the setting to 'Automatically submit samples' or ensure user consent is obtained.
4. If the file still cannot be downloaded, verify geo settings (EU, UK, US) do not restrict download; adjust if necessary.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-file-alerts>
