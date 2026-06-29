# Hardening: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Hardening

## Scenario / Query
How to block credential stealing from LSASS using ASR rule?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** ASR rule for LSASS protection; LSA protection and Credential Guard recommended

## Symptoms
- Many processes make unnecessary calls to LSASS for access rights that aren't needed.
- Google Chrome updates unnecessarily access LSASS, generating ASR rule noise but not blocking functionality.

## Error Codes
N/A

## Root Causes
1. LSASS authenticates users who sign in on Windows computers.
2. Credential Guard in Windows typically prevents attempts to extract credentials from LSASS, but the ASR rule provides additional protection.

## Remediation Steps
1. Enable Local Security Authority (LSA) protection (recommended, along with Credential Guard).
2. If LSA protection is enabled, this ASR rule is not required and is classified as not applicable in Defender for Endpoint management settings.
3. Activate the ASR rule to block processes like Chrome updates from accessing LSASS (note: this does not block Chrome from updating).

## Validation
1. Confirm LSA protection is enabled: run 'reg query HKLM\SYSTEM\CurrentControlSet\Control\Lsa /v RunAsPPL' and verify the value is 1 or 2. 2. Confirm Credential Guard is running: run 'msinfo32.exe' and check 'Device Guard & Credential Guard' status. 3. Verify ASR rule state: in Microsoft 365 Defender portal, go to Endpoints > Configuration management > Attack surface reduction rules, locate 'Block credential stealing from the Windows local security authority subsystem (lsass.exe)' and confirm it is set to 'Block' or 'Audit' as intended. 4. Test Chrome update: launch Chrome and trigger an update (chrome://settings/help) and verify no LSASS access block event is generated in Microsoft 365 Defender (Advanced Hunting > DeviceEvents with ActionType 'AsrLsassCredentialTheft').

## Rollback
1. Disable the ASR rule: in Microsoft 365 Defender portal, navigate to Endpoints > Configuration management > Attack surface reduction rules, find 'Block credential stealing from the Windows local security authority subsystem (lsass.exe)', set it to 'Off' or 'Audit' (if previously 'Block'). 2. If LSA protection was enabled and caused issues, disable it: run 'reg add HKLM\SYSTEM\CurrentControlSet\Control\Lsa /v RunAsPPL /t REG_DWORD /d 0 /f' and restart the device. 3. If Credential Guard was enabled and needs removal, use 'gpedit.msc' or a registry edit to disable it (Computer Configuration > Administrative Templates > System > Device Guard > Turn on Virtualization Based Security > Disabled) and restart. 4. Verify rollback: repeat validation steps to confirm the ASR rule is off and LSA protection/Credential Guard are disabled as needed.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
