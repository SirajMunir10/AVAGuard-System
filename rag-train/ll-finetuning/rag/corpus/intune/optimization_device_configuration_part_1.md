# Optimization: Device Configuration

**Domain:** Intune
**Subdomain:** Device Configuration
**Incident Type:** Optimization

## Scenario / Query
How can I optimize Intune device compliance policies to reduce unnecessary re-evaluation and improve performance for Windows 10/11 devices?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** Intune device compliance policies configured with multiple non-remediable settings (e.g., OS version, TPM presence) that trigger frequent re-evaluation even when device state has not changed.

## Symptoms
- Devices show high compliance policy evaluation counts in Intune reporting
- Users experience delayed device check-in or policy application
- Increased load on Intune service for compliance evaluation

## Error Codes
N/A

## Root Causes
1. Compliance policies include settings that are non-remediable (e.g., required OS version, device encryption status) which cause re-evaluation on every check-in even if the device state is unchanged
2. Lack of use of compliance policy for non-remediable settings that could be evaluated less frequently

## Remediation Steps
1. Review each compliance policy setting and identify those that are non-remediable (e.g., Minimum OS version, Device encryption, TPM presence). For these settings, consider moving them to a configuration profile or using a separate compliance policy with a longer evaluation interval if supported.
2. Use the 'Noncompliance action' settings to set appropriate grace periods and avoid immediate blocking for non-remediable settings.
3. Implement a compliance policy that focuses on remediable settings (e.g., password length, firewall state) and use a separate policy for non-remediable checks with a less frequent evaluation schedule.
4. Monitor compliance policy evaluation reports in Intune to identify policies with high evaluation counts and adjust accordingly.

## Validation
After changes, verify that compliance policy evaluation counts decrease in Intune reporting and that device check-in performance improves without compromising security posture.

## Rollback
Restore original compliance policy settings by reverting any changes made to policy assignments, grace periods, or evaluation intervals.

## References
- Microsoft Learn: 'Monitor Intune device compliance' - https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-monitor
