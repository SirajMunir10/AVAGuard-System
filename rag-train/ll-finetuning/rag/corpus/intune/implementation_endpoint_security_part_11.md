# Implementation: Endpoint Security

**Domain:** Intune
**Subdomain:** Endpoint Security
**Incident Type:** Implementation

## Scenario / Query
How do I configure and manage security settings on managed devices using Intune endpoint security policies?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Endpoint security policies

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use Intune endpoint security policies to configure and manage security settings on managed devices.
2. Endpoint security policies are purpose-built security profiles that focus on specific device security scenarios.
3. Each policy type targets specific security areas (antivirus, firewall, disk encryption, etc.) without the complexity of broader device configuration profiles.
4. Purpose-built policies designed specifically for security scenarios rather than general device management.
5. Grouped by security workload (antivirus, firewall, etc.) rather than mixed with general device management settings.
6. Built-in reporting and conflict detection to ensure security policies deploy successfully.

## Validation
1. Sign in to the Microsoft Intune admin center (https://endpoint.microsoft.com).
2. Navigate to Endpoint security > Overview and verify that the dashboard shows the expected number of devices with active endpoint security policies.
3. Go to Endpoint security > Antivirus (or the relevant security workload) and confirm the policy you created is listed with a status of 'Succeeded' or 'Compliant'.
4. Select the policy, then click 'Device status' to verify that the targeted devices show a status of 'Succeeded' or 'Compliant'.
5. On a managed device, open the Microsoft Defender for Endpoint or Windows Security app and confirm that the security settings (e.g., antivirus, firewall, disk encryption) match the policy configuration.
6. Use the Intune reporting feature: go to Reports > Endpoint security > Device compliance and verify that the device is marked as compliant for the relevant security policy.

## Rollback
1. Sign in to the Microsoft Intune admin center (https://endpoint.microsoft.com).
2. Navigate to Endpoint security > Antivirus (or the relevant security workload).
3. Select the policy you deployed, then click 'Delete' to remove the policy. Confirm the deletion.
4. If the policy was part of a group assignment, go to Endpoint security > Antivirus, select the policy, click 'Properties', then under 'Assignments' remove the assigned groups and click 'Save' to stop the policy from applying.
5. To restore previous settings, create a new endpoint security policy with the original configuration settings and assign it to the same groups.
6. Monitor the device status to ensure the rollback is applied: go to Endpoint security > Antivirus, select the new policy, and check 'Device status' for 'Succeeded' or 'Compliant'.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-policy>
