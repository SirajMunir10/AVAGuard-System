# Hardening: Endpoint Security - Antivirus

**Domain:** Intune
**Subdomain:** Endpoint Security - Antivirus
**Incident Type:** Hardening

## Scenario / Query
How do I harden Microsoft Defender Antivirus settings in Intune to block potentially unwanted applications (PUA) and ensure real-time protection is enabled?

## Environment Context
- **Tenant Type:** Enterprise (Microsoft 365 E5)
- **Configuration:** Intune endpoint security policies for Antivirus are not configured; default Windows Security settings are in use.

## Symptoms
- Users can install potentially unwanted applications without warning or block.
- Real-time protection is disabled on some Windows 10/11 devices.
- Security compliance reports show devices missing required Defender settings.

## Error Codes
N/A

## Root Causes
1. No Intune Antivirus policy deployed to enforce PUA protection and real-time monitoring.
2. Devices are not receiving required security baselines from Intune.

## Remediation Steps
1. Create an Intune Antivirus policy (Settings Catalog > Windows > Microsoft Defender Antivirus) and set 'Real-time monitoring' to 'Enabled'.
2. Set 'Potentially unwanted application protection' to 'Block' (or 'Audit' for testing) under 'Microsoft Defender Antivirus > PUA Protection'.
3. Assign the policy to the appropriate device groups and wait for sync or force sync via Intune portal.
4. Verify policy application by running 'Get-MpPreference' on a target device to confirm 'PUAProtection' is 1 (block) and 'DisableRealtimeMonitoring' is false.

## Validation
On a managed device, open Windows Security > App & browser control > Reputation-based protection and confirm 'Potentially unwanted app blocking' is turned on. Also verify real-time protection is active in Virus & threat protection settings.

## Rollback
In Intune, change the Antivirus policy settings to 'Not configured' or delete the policy assignment. Devices will revert to default Windows Defender settings after the next policy sync.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/antivirus-microsoft-defender-settings-windows>
- <https://www.cisecurity.org/benchmark/microsoft_365>
