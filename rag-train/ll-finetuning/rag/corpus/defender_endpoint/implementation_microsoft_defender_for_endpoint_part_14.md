# Implementation: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Implementation

## Scenario / Query
How to audit changes to Microsoft Defender for Endpoint general settings, such as data retention, onboarding/offboarding packages, and advanced features?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Microsoft 365 audit log enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Changed data retention: ChangeDataRetention - Edited the data retention settings for Defender for Endpoint.
2. Downloaded offboarding package: DownloadOffboardingPkg - Downloaded the package used to remove devices from Defender for Endpoint.
3. Downloaded onboarding package: DownloadOnboardingPkg - Downloaded the package used to onboard devices to Defender for Endpoint.
4. Set advanced features: SetAdvancedFeatures - Changed advanced features in Defender for Endpoint, enabling more precise controls during an incident.

## Validation
1. Verify that the Microsoft 365 audit log is enabled: Run `Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-1) -EndDate (Get-Date) -Operations ChangeDataRetention, DownloadOffboardingPkg, DownloadOnboardingPkg, SetAdvancedFeatures -ResultSize 1000` in Exchange Online PowerShell. Confirm that records for each operation appear with the correct user and timestamp. 2. For data retention changes, check current retention policy: In Microsoft 365 Defender, navigate to Settings > Endpoints > General > Data retention and confirm the retention period matches the intended change. 3. For onboarding/offboarding packages, verify that the package download event is logged with the correct package type and user. 4. For advanced features, navigate to Settings > Endpoints > Advanced features and confirm the toggles match the intended configuration.

## Rollback
1. To revert data retention: In Microsoft 365 Defender, go to Settings > Endpoints > General > Data retention and set the retention period back to the previous value. 2. To revert advanced features: In Settings > Endpoints > Advanced features, disable any features that were enabled or re-enable any that were disabled. 3. If an offboarding package was downloaded and used, re-onboard the device by downloading a new onboarding package from Settings > Endpoints > Onboarding and running it on the device. 4. If an onboarding package was downloaded and used, offboard the device by downloading the offboarding package from Settings > Endpoints > Offboarding and running it on the device. 5. Confirm rollback by re-running the validation audit log search and verifying no unintended changes remain.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
