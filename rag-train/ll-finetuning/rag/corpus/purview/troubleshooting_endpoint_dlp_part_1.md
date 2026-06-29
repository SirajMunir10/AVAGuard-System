# Troubleshooting: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Troubleshooting

## Scenario / Query
Why is advanced classification not scanning files larger than 64 MB for text or 50 MB for images even though bandwidth is set to unlimited?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Advanced classification file scanning size limits

## Symptoms
- Advanced classification does not work for text files larger than 64 MB
- Advanced classification does not work for image files larger than 50 MB when OCR is enabled
- Bandwidth limit set to 'Do not limit bandwidth. Unlimited' but scanning still fails for large files

## Error Codes
N/A

## Root Causes
1. There is a 64-MB limit on text files for advanced classification scanning
2. There is a 50-MB limit on image files when Optical Character Recognition (OCR) is enabled
3. Advanced classification doesn't work for text files larger than 64 MB, even if the bandwidth limit is set to 'Do not limit bandwidth. Unlimited'

## Remediation Steps
1. Ensure files to be scanned are within the size limits: text files ≤ 64 MB, image files ≤ 50 MB (when OCR is enabled)
2. For Windows 10 devices, install KB5016688 to support advanced classification
3. For Windows 11 devices, install KB5016691 to support advanced classification
4. Enable advanced classification before Activity explorer displays contextual text for DLP rule-matched events

## Validation
Check that files are within the size limits and that required KB updates are installed on Windows 10 (KB5016688) or Windows 11 (KB5016691) devices

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
