# Implementation: Compliance Policy

**Domain:** Intune
**Subdomain:** Compliance Policy
**Incident Type:** Implementation

## Scenario / Query
How do I configure compliance policy settings for Windows Subsystem for Linux (WSL) in Intune?

## Environment Context
- **Tenant Type:** Intune-managed Windows devices
- **Configuration:** Windows Subsystem for Linux (WSL) plug-in required

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure the Windows Subsystem for Linux (WSL) plug-in is installed.
2. In the compliance policy, under 'Windows Subsystem for Linux', enter at least one Linux distribution name.
3. Optionally, enter a minimum or maximum OS version for the distribution.
4. If no distribution is provided, all distributions are allowed (default behavior).
5. If only distribution names are provided, all installed versions of that distribution are allowed.
6. If a distribution name and a minimum OS version are provided, all installed distributions with the provided name and minimum version or later are allowed.
7. If a distribution name and a maximum OS version are provided, all installed distributions with the provided name and maximum version or earlier are allowed.
8. If a distribution name, a minimum OS version, and a maximum OS version are provided, all installed distributions and OS versions within the provided range are allowed.

## Validation
1. Verify that the Windows Subsystem for Linux (WSL) plug-in is installed on the target device by running: 'wsl --status' or checking for the presence of the plug-in in 'Add or remove programs'. 2. In the Microsoft Intune admin center, navigate to 'Endpoint security' > 'Device compliance' > 'Policies' and select the compliance policy. 3. Under 'Compliance settings', expand 'Windows Subsystem for Linux' and confirm that at least one Linux distribution name is entered. 4. If optional version constraints were configured, verify that the 'Minimum OS version' and/or 'Maximum OS version' fields contain the expected values. 5. On a test device, run 'wsl --list --verbose' to list installed distributions and confirm that the policy enforcement matches the configured settings (e.g., allowed distributions and version ranges).

## Rollback
1. In the Microsoft Intune admin center, navigate to 'Endpoint security' > 'Device compliance' > 'Policies' and select the compliance policy. 2. Under 'Compliance settings', expand 'Windows Subsystem for Linux' and remove all entered distribution names and version constraints to revert to default behavior (all distributions allowed). 3. Alternatively, if the policy should be disabled entirely, change the 'Windows Subsystem for Linux' setting to 'Not configured'. 4. Save the policy changes and allow time for the policy to sync to devices. 5. On a test device, run 'wsl --list --verbose' to confirm that no compliance restrictions are applied to WSL distributions.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-create-windows>
