# Implementation: Compliance Policies

**Domain:** Intune
**Subdomain:** Compliance Policies
**Incident Type:** Implementation

## Scenario / Query
How to configure Configuration Manager compliance settings for co-managed Windows devices in Intune compliance policies?

## Environment Context
- **Tenant Type:** Co-managed Windows devices
- **Configuration:** Configuration Manager Compliance setting

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Set 'Require device compliance from Configuration Manager' to 'Require' to enforce all Configuration Manager configuration items for compliance.
2. Leave as 'Not configured (default)' if Intune should not check Configuration Manager settings for compliance.

## Validation
1. In the Microsoft Intune admin center, navigate to 'Devices' > 'Compliance policies' > 'Policies' and select the policy targeting co-managed Windows devices. 2. Under 'Compliance settings', verify that 'Require device compliance from Configuration Manager' is set to 'Require'. 3. On a co-managed Windows device, open the Company Portal app and confirm the device status shows as compliant. 4. In Configuration Manager console, verify the device's compliance state reflects the configuration items being enforced.

## Rollback
1. In the Microsoft Intune admin center, navigate to 'Devices' > 'Compliance policies' > 'Policies' and select the policy where the setting was changed. 2. Under 'Compliance settings', set 'Require device compliance from Configuration Manager' back to 'Not configured (default)'. 3. On a co-managed Windows device, open the Company Portal app and confirm the device status updates accordingly. 4. In Configuration Manager console, verify that compliance from Configuration Manager is no longer enforced by Intune.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-create-windows>
