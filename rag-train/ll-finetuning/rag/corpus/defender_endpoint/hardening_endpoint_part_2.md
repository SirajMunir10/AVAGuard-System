# Hardening: Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint
**Incident Type:** Hardening

## Scenario / Query
What are the requirements for downloading quarantined files in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** commercial
- **Configuration:** Microsoft Defender Antivirus active mode, antivirus engine version, cloud-based protection, sample submission

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Your organization uses Microsoft Defender Antivirus in active mode.
2. Antivirus engine version is 1.1.17300.4 or later.
3. Cloud-based protection is enabled.
4. Sample submission is turned on.
5. Client devices must be running Windows 11 or Windows 10, version 1703 or later.
6. Server devices must be running Windows Server 2016 and later or Azure Stack HCI OS, version 23H2 and later.

## Validation
1. Verify Microsoft Defender Antivirus is in active mode: Run 'Get-MpComputerStatus | Select-Object AMRunningMode' on a client device. Confirm output is 'Active'.
2. Check antivirus engine version: Run 'Get-MpComputerStatus | Select-Object AntivirusEngineVersion' and ensure it is 1.1.17300.4 or later.
3. Confirm cloud-based protection is enabled: Run 'Get-MpPreference | Select-Object CloudBlockLevel' and verify it is not '0' (disabled).
4. Confirm sample submission is turned on: Run 'Get-MpPreference | Select-Object SubmitSamplesConsent' and verify it is set to 1 (Send safe samples automatically) or 2 (Send all samples automatically).
5. Verify client OS version: Run 'Get-ComputerInfo | Select-Object WindowsVersion' and confirm it is 1703 or later for Windows 10, or Windows 11.
6. Verify server OS version: Run 'Get-ComputerInfo | Select-Object WindowsVersion' and confirm it is Windows Server 2016 or later, or Azure Stack HCI OS version 23H2 or later.

## Rollback
1. If Microsoft Defender Antivirus is not in active mode, set it to active mode: Run 'Set-MpPreference -DisableRealtimeMonitoring $false' and ensure no other antivirus is installed.
2. If antivirus engine version is below 1.1.17300.4, update Microsoft Defender Antivirus via Windows Update or by downloading the latest platform update from Microsoft.
3. If cloud-based protection is disabled, enable it: Run 'Set-MpPreference -CloudBlockLevel 2' (or appropriate level).
4. If sample submission is turned off, enable it: Run 'Set-MpPreference -SubmitSamplesConsent 1' (or 2 for all samples).
5. If client OS version is below Windows 10 version 1703 or not Windows 11, upgrade the OS to a supported version.
6. If server OS version is below Windows Server 2016 or not Azure Stack HCI OS version 23H2, upgrade the OS to a supported version.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-file-alerts>
