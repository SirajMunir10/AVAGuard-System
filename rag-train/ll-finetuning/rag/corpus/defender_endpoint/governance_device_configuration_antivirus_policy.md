# Governance: Device Configuration â€“ Antivirus Policy

**Domain:** Defender for Endpoint
**Subdomain:** Device Configuration â€“ Antivirus Policy
**Incident Type:** Governance

## Scenario / Query
A security administrator notices that some devices in the tenant are not receiving the expected Microsoft Defender Antivirus policy settings. How can the administrator verify and enforce the correct policy assignment using Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Defender for Endpoint Plan 2
- **Configuration:** Antivirus policy assigned via Microsoft Intune security baselines

## Symptoms
- Devices show 'Not evaluated' or 'Conflict' status for Antivirus policy in the Microsoft 365 Defender portal
- Some endpoints are running with default AV settings instead of the organization's hardened policy

## Error Codes
N/A

## Root Causes
1. Antivirus policy not assigned to the correct Azure AD group
2. Multiple conflicting policies applied to the same device
3. Device not enrolled in Intune or not communicating with the service

## Remediation Steps
1. In the Microsoft 365 Defender portal, navigate to Endpoints > Configuration management > Endpoint security policies and verify the Antivirus policy assignment
2. Ensure the policy is assigned to the correct Azure AD device group and that the group membership is up-to-date
3. Check for policy conflicts by reviewing the deviceâ€™s policy report in Microsoft Intune admin center
4. If conflicts exist, remove duplicate or overlapping policies and keep only the intended baseline
5. Force a policy sync on the affected device using the Microsoft 365 Defender portal or by running 'Sync-M365Device' in PowerShell (if documented in your environment)

## Validation
After remediation, verify that the device shows 'Compliant' status for the Antivirus policy in the Microsoft 365 Defender portal and that the local Defender for Endpoint client reflects the expected settings.

## Rollback
If the policy assignment change causes issues, reassign the original policy or restore the previous group membership via Azure AD.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/manage-endpoint-security-policies>
