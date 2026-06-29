# Troubleshooting: Microsoft Defender Antivirus

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot and remediate threats detected by Microsoft Defender Antivirus based on the action taken (Clean, Quarantine, Allow)?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Threat detected with action: Clean
- Threat detected with action: Quarantine
- Threat detected with action: Allow

## Error Codes
N/A

## Root Causes
1. Outdated definitions
2. User lacks permission to access necessary resources

## Remediation Steps
1. Update the definitions then verify that the remediation was successful.
2. Update the definitions and verify that the user has permission to access the necessary resources.
3. Verify that the user has permission to access the necessary resources.
4. If this event persists: Run the scan again.
5. If it fails in the same way, go to the Microsoft Support site, enter the error number in the Search box to look for the error code.
6. Contact Microsoft Technical Support.

## Validation
1. Open Windows Security app > Virus & threat protection > Protection history. Verify that the threat with action 'Clean' shows status 'Removed' or 'Cleaned'. 2. For 'Quarantine' action, confirm the threat appears in Quarantine list and can be viewed. 3. For 'Allow' action, check that the file is listed in Allowed threats and is no longer blocked. 4. Run 'Get-MpThreatDetection' in PowerShell to list recent detections and confirm the specific threat is resolved. 5. Verify Microsoft Defender Antivirus definitions are up to date by running 'Get-MpComputerStatus' and checking 'AntivirusSignatureVersion' against latest version.

## Rollback
1. If a threat was cleaned but should not have been, restore the file from quarantine: Open Windows Security > Virus & threat protection > Protection history, select the threat, and choose 'Restore'. 2. If a threat was quarantined incorrectly, restore it via PowerShell: 'Restore-MpThreatDetection -ThreatID <ThreatID>'. 3. If a threat was allowed in error, remove the allow entry: Open Windows Security > Virus & threat protection > Protection history > Allowed threats, select the item, and click 'Remove'. 4. If definitions update caused issues, roll back to previous definitions: Run 'Get-MpComputerStatus' to find previous signature version, then use 'Update-MpSignature -Rollback' to revert. 5. If user permission changes caused access issues, restore original permissions via Group Policy or local security settings.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
