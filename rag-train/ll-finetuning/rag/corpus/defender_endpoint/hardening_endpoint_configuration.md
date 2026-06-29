# Hardening: Endpoint configuration

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint configuration
**Incident Type:** Hardening

## Scenario / Query
How to configure sample collection settings for Microsoft Defender for Endpoint using Configuration Manager compliance rules?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** System Center Configuration Manager (SCCM) with Microsoft Defender for Endpoint

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Set a compliance rule for configuration item in Configuration Manager to change the sample share setting on a device.
2. The rule should be a remediating compliance rule configuration item that sets the value of a registry key on targeted devices to make sure they're compliant.
3. Configure the following registry key entry: Path: 'HKLM\SOFTWARE\Policies\Microsoft\Windows Advanced Threat Protection', Name: 'AllowSampleCollection', Value: 0 or 1, Key type: D-WORD.
4. Possible values: 0 (doesn't allow sample sharing from this device), 1 (allows sharing of all file types from this device). Default value if registry key doesn't exist is 1.

## Validation
1. On a targeted device, open Registry Editor and navigate to HKLM\SOFTWARE\Policies\Microsoft\Windows Advanced Threat Protection. Verify that the DWORD value 'AllowSampleCollection' exists and is set to the expected value (0 or 1).
2. In Configuration Manager console, go to Assets and Compliance > Compliance Settings > Configuration Items. Select the configuration item used for this rule, then click 'Evaluate' to run a manual compliance evaluation against a collection containing the device. Confirm the device shows as 'Compliant'.
3. On the device, open PowerShell as Administrator and run: Get-MpPreference | Select-Object -Property SubmitSamplesConsent. Verify the output matches the expected sample sharing behavior (e.g., 0 for never send, 1 for send safe samples automatically, 2 for send all samples automatically).

## Rollback
1. In Configuration Manager console, navigate to Assets and Compliance > Compliance Settings > Configuration Items. Locate the configuration item that sets the AllowSampleCollection registry value. Edit the configuration item and remove or disable the remediating compliance rule for that registry setting.
2. Alternatively, create a new configuration baseline that sets the registry key to the original default value (1) and deploy it to the affected devices.
3. On each affected device, open Registry Editor and navigate to HKLM\SOFTWARE\Policies\Microsoft\Windows Advanced Threat Protection. Delete the 'AllowSampleCollection' DWORD value (or set it to 1) to restore default behavior.
4. After remediation, run a manual compliance evaluation to confirm devices are no longer enforced by the removed rule.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-sccm>
