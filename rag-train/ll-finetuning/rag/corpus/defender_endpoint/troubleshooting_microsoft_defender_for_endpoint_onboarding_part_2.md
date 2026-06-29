# Troubleshooting: Microsoft Defender for Endpoint onboarding (-2016345687)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint onboarding
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Microsoft Defender for Endpoint onboarding failures related to access control permissions and non-supported SKUs?

## Environment Context
- **Tenant Type:** Microsoft Intune managed
- **Configuration:** Microsoft Defender for Endpoint onboarding policies

## Symptoms
- SyncML(425): The requested command failed because the sender doesn't have adequate access control permissions (ACL) on the recipient
- Device is compliant by SenseIsRunning OMA-URI but non-compliant by OrgId, Onboarding and OnboardingState OMA-URIs
- Device is compliant by OrgId, Onboarding, and OnboardingState OMA-URIs but non-compliant by SenseIsRunning OMA-URI
- Device is non-compliant

## Error Codes
- `-2016345687`

## Root Causes
1. Attempt to deploy Microsoft Defender for Endpoint on non-supported SKU/Platform, particularly Holographic SKU
2. User passed OOBE after Windows installation or upgrade; during OOBE onboarding couldn't be completed but SENSE is running already
3. Sense service's startup type is set as 'Delayed Start' causing Microsoft Intune server to report device as non-compliant by SenseIsRunning when DM session occurs on system start
4. Onboarding and Offboarding policies deployed on the same device at same time

## Remediation Steps
1. Ensure deployment is on supported platforms: Enterprise, Education, and Professional
2. Wait for OOBE to complete
3. The issue should automatically be fixed within 24 hours
4. Ensure that Onboarding and Offboarding policies aren't deployed on the same device at same time
5. View the MDM event logs to troubleshoot issues that might arise during onboarding: Log name: Microsoft\Windows\DeviceManagement-EnterpriseDiagnostics-Provider, Channel name: Admin
6. Download the Cumulative Update for Windows 10, 1607

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
