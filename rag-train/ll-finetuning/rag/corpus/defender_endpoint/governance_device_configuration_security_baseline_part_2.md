# Governance: Device Configuration â€“ Security Baseline

**Domain:** Defender for Endpoint
**Subdomain:** Device Configuration â€“ Security Baseline
**Incident Type:** Governance

## Scenario / Query
A security administrator notices that several Windows 10 devices in the organization are not compliant with the Microsoft Defender for Endpoint security baseline. The devices are enrolled in Microsoft Intune, but the baseline policy appears to have been removed or not applied. How can the administrator verify the current baseline assignment and reapply the security baseline to ensure consistent protection?

## Environment Context
- **Tenant Type:** Microsoft 365 E5 with Microsoft Intune and Defender for Endpoint
- **Configuration:** Devices are managed via Intune and targeted with the 'Microsoft Defender for Endpoint Baseline' policy

## Symptoms
- Devices show 'Not compliant' status in Microsoft 365 Defender portal under Device configuration
- Security baseline settings (e.g., Attack Surface Reduction rules, Windows Defender Antivirus settings) are missing or not enforced on endpoints
- Baseline policy appears in Intune but is not assigned to the affected device groups

## Error Codes
N/A

## Root Causes
1. The security baseline policy was accidentally unassigned from the device group during a policy update
2. Devices were moved to a different group that does not have the baseline policy assigned
3. The baseline policy assignment was deleted or overwritten by another policy with lower priority

## Remediation Steps
1. In the Microsoft Intune admin center, navigate to 'Endpoint security' > 'Security baselines' and select the 'Microsoft Defender for Endpoint Baseline'.
2. Review the 'Assignments' tab to confirm which groups are targeted. If the affected device group is missing, click 'Edit' and add the group.
3. Alternatively, create a new baseline profile using the same settings and assign it to the appropriate device groups.
4. After reassignment, monitor compliance in the Microsoft 365 Defender portal under 'Device configuration' > 'Compliance'.

## Validation
Verify that affected devices show 'Compliant' status in the Microsoft 365 Defender portal under Device configuration within 24 hours of reassignment.

## Rollback
If the reassignment causes unintended changes, remove the group from the baseline assignment and reassign the previous policy version or restore from a backup of the policy configuration.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/security-baselines>
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/device-compliance>
