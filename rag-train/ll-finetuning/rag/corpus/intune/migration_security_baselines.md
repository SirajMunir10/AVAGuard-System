# Migration: Security Baselines

**Domain:** Intune
**Subdomain:** Security Baselines
**Incident Type:** Migration

## Scenario / Query
How to migrate from on-premises Active Directory group policies to a pure cloud solution using Microsoft Entra ID with Microsoft Intune?

## Environment Context
- **Tenant Type:** Hybrid or on-premises Active Directory with Microsoft Intune
- **Configuration:** Security Compliance Toolkit

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the various tools from the Security Compliance Toolkit
2. Identify cloud-based options from security baselines that can replace on-premises GPO configurations

## Validation
1. Verify that the Intune security baseline policies are assigned to the correct Microsoft Entra ID groups (e.g., all devices or pilot devices).
2. On a test device, run 'dsregcmd /status' to confirm the device is Microsoft Entra joined or hybrid joined.
3. On the same device, open the Microsoft Intune Company Portal or use the Settings app to confirm the policy is applied (e.g., navigate to Accounts > Access work or school > Info to see 'Intune' as the MDM).
4. Use the Intune admin center: go to 'Endpoint security' > 'Security baselines' > select the baseline > 'Monitor' > 'Device status' to confirm the device shows 'Succeeded' or 'Compliant'.
5. Compare the device's local security settings (e.g., via 'secpol.msc' or 'gpresult /h report.html') against the baseline settings to ensure the cloud policy has overridden any conflicting on-premises GPO.

## Rollback
1. In the Intune admin center, navigate to 'Endpoint security' > 'Security baselines' > select the baseline you deployed.
2. Under 'Assignments', remove the Microsoft Entra ID groups that were assigned the baseline policy.
3. Wait for the next Intune sync (or force a sync on the device via Settings > Accounts > Access work or school > Info > Sync).
4. On the affected devices, run 'gpupdate /force' to reapply the on-premises GPO settings if the device is still hybrid joined.
5. Verify that the device's security settings revert to the on-premises GPO values using 'gpresult /h report.html' or 'secpol.msc'.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/security-baselines>
