# Hardening: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Hardening

## Scenario / Query
How to ensure advanced classification scanning works for Office and PDF files on Windows endpoints?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Advanced classification file type support

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Support for advanced classification is available for Office (Word, Excel, PowerPoint) and PDF file types
2. Ensure devices meet the Windows version requirements: all Windows 11 versions, Windows 10 versions 20H1/21H1 or higher (KB 5006738), or Windows 10 RS5 (KB 5006744)
3. Install KB5016688 for Windows 10 devices or KB5016691 for Windows 11 devices
4. Enable advanced classification

## Validation
1. Verify that the Windows version meets the requirement: run 'winver' and confirm the build is Windows 11 (any version) or Windows 10 20H1/21H1 or higher (with KB 5006738) or Windows 10 RS5 (with KB 5006744).
2. Check that KB5016688 (Windows 10) or KB5016691 (Windows 11) is installed: run 'wmic qfe list brief /format:texttable' and look for the corresponding KB number.
3. Confirm advanced classification is enabled in the endpoint DLP policy: navigate to Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP policy > Settings > Advanced classification and verify the toggle is turned on.
4. Test scanning by copying a sensitive Office or PDF file to the device and triggering a DLP policy; check the DLP alerts or activity explorer for a match.

## Rollback
1. Disable advanced classification: in the endpoint DLP policy settings, turn off the 'Advanced classification' toggle.
2. If the issue is caused by a specific KB update, uninstall the update: go to Settings > Update & Security > Windows Update > View update history > Uninstall updates, select KB5016688 or KB5016691, and click Uninstall.
3. Reboot the device if prompted.
4. Revert any policy changes made during remediation by restoring the previous endpoint DLP policy configuration from backup or by manually resetting the advanced classification setting to its original state.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
