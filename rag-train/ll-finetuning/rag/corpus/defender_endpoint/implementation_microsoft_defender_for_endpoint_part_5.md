# Implementation: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Implementation

## Scenario / Query
How to configure Microsoft Defender Antivirus policies using Group Policy for endpoint deployment?

## Environment Context
- **Tenant Type:** On-premises Active Directory with Group Policy
- **Configuration:** Group Policy Management Console (GPMC)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create a new Group Policy or group these settings in with the other policies. This is dependent upon the customer's environment and how they would like to roll out the service by targeting different organizational units (OUs).
2. After you choose the GP, or create a new one, edit the GP.
3. Browse to Computer Configuration > Policies > Administrative Templates > Windows Components > Microsoft Defender Antivirus > Real-time Protection.
4. In the Quarantine folder, configure removal of items from Quarantine folder.
5. In the Scan folder, configure the scan settings.

## Validation
1. Open Group Policy Management Console (GPMC).
2. Locate the Group Policy Object (GPO) that was configured for Microsoft Defender Antivirus.
3. Right-click the GPO and select 'Edit'.
4. Navigate to Computer Configuration > Policies > Administrative Templates > Windows Components > Microsoft Defender Antivirus.
5. Verify that the following policy settings are configured as intended:
   - Real-time Protection: Ensure the 'Turn off real-time protection' policy is set to 'Disabled' or 'Not Configured' (as per desired state).
   - Quarantine: Under 'Quarantine', confirm the 'Configure removal of items from Quarantine folder' policy is set to the desired number of days (e.g., '30').
   - Scan: Under 'Scan', verify scan settings such as 'Specify the scan type to use for scheduled scans' and 'Check for the latest virus and spyware definitions before running a scheduled scan' are configured as required.
6. Run 'gpupdate /force' on a test machine in the targeted OU.
7. On the test machine, open PowerShell as Administrator and run 'Get-MpPreference' to confirm the applied settings match the GPO configuration (e.g., check DisableRealtimeMonitoring, QuarantinePurgeItemsAfterDelay, ScanParameters).
8. Confirm that Microsoft Defender Antivirus is running and real-time protection is active by running 'Get-MpComputerStatus' and verifying 'AMRunningMode' is 'Normal'.

## Rollback
1. Open Group Policy Management Console (GPMC).
2. Locate the GPO that was modified for Microsoft Defender Antivirus.
3. Right-click the GPO and select 'Edit'.
4. Navigate to Computer Configuration > Policies > Administrative Templates > Windows Components > Microsoft Defender Antivirus.
5. For each policy setting that was changed (Real-time Protection, Quarantine, Scan), set the policy to 'Not Configured' to revert to default behavior.
6. Alternatively, if a new GPO was created, delete the GPO or unlink it from the targeted OU.
7. Run 'gpupdate /force' on affected machines to apply the rollback.
8. On a test machine, run 'Get-MpPreference' to confirm that the reverted settings are applied (e.g., DisableRealtimeMonitoring should be False, QuarantinePurgeItemsAfterDelay should be default).
9. Verify Microsoft Defender Antivirus is functioning correctly by running 'Get-MpComputerStatus' and checking 'AMRunningMode' is 'Normal'.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-gp>
