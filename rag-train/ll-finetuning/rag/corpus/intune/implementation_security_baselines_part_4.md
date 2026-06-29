# Implementation: Security Baselines

**Domain:** Intune
**Subdomain:** Security Baselines
**Incident Type:** Implementation

## Scenario / Query
How to handle default settings conflicts between different security baseline types (e.g., MDM security baseline for Windows and Microsoft Defender baseline) in Intune?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Multiple security baseline types assigned to same devices

## Symptoms
- Default values for the same setting differ between baseline types
- Potential conflicts between baseline recommendations and other policy settings

## Error Codes
N/A

## Root Causes
1. Separate baseline types (e.g., MDM security baseline for Windows and Microsoft Defender baseline) include the same settings with different default values
2. Intune cannot determine which configuration is best for a given environment or scenario

## Remediation Steps
1. Review each setting to understand its intent based on the configuration service provider details and larger scope of the two products
2. Modify each baseline to fit organizational needs
3. Confirm that default settings don't conflict with other policy settings or features in the environment
4. Validate firewall configuration default settings, as they might not merge connection security rules and local policy rules with MDM rules
5. If using delivery optimization, validate these configurations before assigning the security baseline

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Security baselines and select each assigned baseline (e.g., MDM security baseline for Windows and Microsoft Defender baseline).
2. For each baseline, review the 'Settings' list and identify any settings that appear in both baselines. Compare the configured values to ensure they are consistent and aligned with organizational requirements.
3. On a test device that receives both baselines, open the 'Settings' app > Accounts > Access work or school > click the connected account > Info > 'Sync' to force a policy refresh.
4. On the same test device, run 'dsregcmd /status' and verify that the 'AzureAdJoined' status is 'YES' and 'DomainJoined' is 'NO' (or as appropriate).
5. Run 'Get-MpComputerStatus' in PowerShell to confirm Microsoft Defender settings (e.g., RealTimeProtectionEnabled, AntivirusEnabled) match the intended baseline values.
6. Run 'Get-NetFirewallProfile' in PowerShell to validate firewall rules are applied as expected and that no connection security rules or local policy rules conflict with MDM rules.
7. If delivery optimization is used, run 'Get-DeliveryOptimizationStatus' in PowerShell to confirm settings are applied correctly.
8. Check the Intune admin center for any policy conflict alerts under 'Troubleshoot + support' > 'Troubleshoot' for the test device.

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint security > Security baselines.
2. For each baseline that was modified, select the baseline profile and click 'Properties'.
3. Under 'Configuration settings', revert any changed settings back to their original default values or to the previously known working values.
4. If a baseline assignment was changed, reassign the original baseline profile to the affected device groups.
5. On affected devices, force a policy sync by going to Settings > Accounts > Access work or school > select the connected account > Info > Sync.
6. Alternatively, from an elevated PowerShell prompt on a test device, run 'Start-Process -FilePath "ms-settings:workplace" -PassThru' and then click 'Sync'.
7. Verify that the device reports success in the Intune admin center under 'Devices' > 'All devices' > select the device > 'Device configuration'.
8. If conflicts persist, remove one of the conflicting baseline assignments from the device group by editing the assignment in the baseline's 'Properties' > 'Assignments' and setting the assignment to 'Not assigned'.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/security-baselines>
