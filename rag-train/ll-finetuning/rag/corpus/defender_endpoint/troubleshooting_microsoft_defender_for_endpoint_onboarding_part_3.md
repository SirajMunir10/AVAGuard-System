# Troubleshooting: Microsoft Defender for Endpoint onboarding

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint onboarding
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot when the SENSE service fails to start during Microsoft Defender for Endpoint onboarding?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Failed to start SENSE service

## Error Codes
N/A

## Root Causes
1. The SENSE Feature on Demand (FoD) may not be installed

## Remediation Steps
1. Determine whether the SENSE FoD is installed by entering the following command from an Admin CMD/PowerShell prompt: DISM.EXE /Online /Get-CapabilityInfo /CapabilityName:Microsoft.Windows.Sense.Client~~~~
2. If it returns an error or the state is not 'Installed,' then the SENSE FoD must be installed. See Available Features on Demand: SENSE Client for Microsoft Defender for Endpoint for installation instructions.

## Validation
Run the following command from an elevated Command Prompt or PowerShell: DISM.EXE /Online /Get-CapabilityInfo /CapabilityName:Microsoft.Windows.Sense.Client~~~~. Confirm that the output shows 'State : Installed' and no errors are returned. Then verify the SENSE service status by running 'sc query sense' or 'Get-Service sense' and ensure the service is running (StartType should be Automatic and Status should be Running).

## Rollback
If the SENSE FoD installation causes issues, remove the capability by running from an elevated Command Prompt or PowerShell: DISM.EXE /Online /Remove-Capability /CapabilityName:Microsoft.Windows.Sense.Client~~~~. After removal, reboot the device and verify the SENSE service is no longer present by running 'sc query sense' (should return 'service does not exist' or similar).

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
