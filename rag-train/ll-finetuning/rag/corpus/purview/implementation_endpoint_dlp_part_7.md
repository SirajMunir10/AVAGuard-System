# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How do I configure file path exclusions for macOS devices in Endpoint DLP?

## Environment Context
- **Tenant Type:** macOS
- **Configuration:** Endpoint DLP settings for macOS

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. File path definitions are case insensitive, so User is the same as user.
2. Wildcard values are supported. So a path definition can contain an asterisk (*) in the middle of the path or at the end of the path. Example: /Users/*/Library/Application Support/Microsoft/Teams/*
3. If you set the Include recommended file path exclusions for Mac toggle to On, the following paths are also excluded: /Applications, /Users/*/Library/Logs, /Users/*/Library/Containers, /Users/*/Library/Application Support, /Users/*/Library/Group Containers, /Users/*/Library/Caches, /Users/*/Library/Developer
4. Keep this toggle set to On. However, you can stop excluding these paths by setting the toggle to Off.

## Validation
1. Verify that the 'Include recommended file path exclusions for Mac' toggle is set to 'On' in the Microsoft Purview compliance portal under Endpoint DLP settings for macOS. 2. Confirm that the custom file path exclusion list includes the desired paths (e.g., /Users/*/Library/Application Support/Microsoft/Teams/*) and that they are case-insensitive. 3. Use a macOS test device to attempt DLP actions on files within the excluded paths and confirm that no policy violations are triggered.

## Rollback
1. Set the 'Include recommended file path exclusions for Mac' toggle to 'Off' to stop excluding the default paths. 2. Remove any custom file path exclusions that were added by editing the exclusion list in the Endpoint DLP settings. 3. Re-test DLP actions on previously excluded paths to confirm that policy enforcement resumes.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
