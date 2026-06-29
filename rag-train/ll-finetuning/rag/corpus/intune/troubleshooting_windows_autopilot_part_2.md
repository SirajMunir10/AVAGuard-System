# Troubleshooting: Windows Autopilot (HRESULT=[error code])

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
What do the different Event IDs mean in the Windows Autopilot event log entries in Event Viewer?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Windows Autopilot profile configuration

## Symptoms
- Autopilot policy [name] not found
- AutopilotGetPolicyDwordByName succeeded: policy name = [setting name]; policy value = [value]
- AutopilotGetPolicyStringByName succeeded: policy name = [name]; value = [value]
- AutopilotGetOobeSettingsOverride succeeded: OOBE setting [setting name]; state = [state]
- AutopilotRetrieveSettings succeeded
- AutopilotManager reported the state changed from [original state] to [new state]
- AutopilotRetrieveSettings beginning acquisition
- AutopilotManager retrieve settings succeeded
- AutopilotManager determined download isn't required and the device is already provisioned
- AutopilotManager determined Internet is available to attempt policy download
- AutopilotManager failed to set TPM identity confirmed. HRESULT=[error code]
- AutopilotManager failed to set Autopilot profile as available. HRESULT=[error code]
- ZtdDeviceIsNotRegistered
- ZtdDeviceHasNoAssignedProfile - Assigned profile does not exist
- ZtdDeviceHasNoAssignedProfile - No profile assigned to the device, and no default profile found in the tenant

## Error Codes
- `HRESULT=[error code]`

## Root Causes
1. Temporary problem while the device is waiting for a Windows Autopilot profile to be downloaded
2. TPM attestation issue needed to complete the self-deploying mode process
3. Windows Autopilot profile assigned to the device was deleted without first getting cleaned up
4. Windows Autopilot profile wasn't found assigned to the device

## Remediation Steps
1. Clean or reset the device to change the provisioned state
2. Validate that the device's hardware hash is properly uploaded to Intune and that the device is assigned to a deployment profile
3. Assign a different Windows Autopilot profile to the device and then attempt to re-enroll the device

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
