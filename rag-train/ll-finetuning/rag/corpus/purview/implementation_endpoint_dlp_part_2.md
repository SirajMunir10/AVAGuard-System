# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How do I configure the 'Always audit file activity for devices' setting in Microsoft Purview Endpoint DLP?

## Environment Context
- **Tenant Type:** Microsoft 365 E5/A5/G5
- **Configuration:** Endpoint DLP settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings
2. Locate the 'Always audit file activity for devices' toggle
3. Enable the setting to audit file activities for documents where a DLP Rule didn't match: File Created, File Modified, File Renamed, File created on removable media, and File created on network share
4. Disable the setting if you want to audit this activity only when onboarded devices are included in an active policy

## Validation
Review audited file activities in activity explorer

## Rollback
Toggle the 'Always audit file activity for devices' setting to the opposite state

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
