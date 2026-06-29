# Troubleshooting: Security Baselines

**Domain:** Intune
**Subdomain:** Security Baselines
**Incident Type:** Troubleshooting

## Scenario / Query
How to identify and resolve configuration conflicts when using multiple security baselines or combining baselines with device configuration profiles in Intune?

## Environment Context
- **Tenant Type:** Intune-managed enterprise
- **Configuration:** Multiple security baseline instances with different customizations, or coexistence of security baselines and device configuration profiles

## Symptoms
- Devices exhibit unexpected behavior due to conflicting policy settings
- Security baseline deployment reports show errors or warnings for specific settings
- Devices fail to apply intended configuration from one baseline due to override by another baseline or profile

## Error Codes
N/A

## Root Causes
1. Using multiple security baselines designed for different intents simultaneously
2. Deploying multiple instances of the same baseline with different customizations
3. Security baselines managing the same settings as device configuration profiles or other policy types

## Remediation Steps
1. Review the settings in each deployed security baseline to identify conflicting values for the same setting
2. Investigate and resolve configuration conflicts by adjusting baseline customizations or removing redundant baselines
3. Consider other policies and profiles for settings when seeking to avoid or resolve conflicts

## Validation
1. In the Intune admin center, navigate to Endpoint security > Security baselines and review each deployed baseline instance. For each baseline, select 'Properties' and then 'Settings' to export the current configuration. Compare the exported settings across all baselines to identify any conflicting values for the same setting. 2. Go to Devices > All devices, select a test device, and choose 'Device configuration' to view the effective settings. Verify that the intended setting value from the desired baseline is applied and not overridden by another baseline or profile. 3. Use the 'Troubleshoot + support' blade to run a policy report for a device that exhibited errors. Confirm that the report no longer shows conflicts or errors for the settings in question.

## Rollback
1. If a conflict is introduced by modifying a baseline, revert the baseline to its previous configuration by selecting the baseline instance, choosing 'Properties', and restoring the original settings from backup or documentation. 2. If a redundant baseline was removed and caused unintended changes, redeploy the baseline by going to Endpoint security > Security baselines, selecting 'Create profile', and re-creating the baseline with the same settings as before. 3. If a device configuration profile was adjusted, navigate to Devices > Configuration profiles, select the profile, and restore the previous setting values. Then force a sync on affected devices using Devices > All devices > select device > Sync.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/security-baselines>
- <https://learn.microsoft.com/en-us/mem/intune/protect/troubleshoot-policies-in-microsoft-intune>
