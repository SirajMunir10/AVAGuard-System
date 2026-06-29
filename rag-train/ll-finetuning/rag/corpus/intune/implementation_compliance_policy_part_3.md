# Implementation: Compliance Policy

**Domain:** Intune
**Subdomain:** Compliance Policy
**Incident Type:** Implementation

## Scenario / Query
How to configure Antispyware compliance check in Intune?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** DeviceStatus CSP - DeviceStatus/Antispyware/Status

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Set Antispyware to 'Not configured' (default) to skip antispyware check
2. Set Antispyware to 'Require' to check compliance using antispyware solutions registered with Windows Security Center (e.g., Symantec, Microsoft Defender); device with antimalware software disabled or out of date is noncompliant

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Antivirus > Windows 10 and later compliance policies. Select the policy that was modified and verify that the 'Antispyware' setting is set to either 'Not configured' or 'Require' as intended. 2. On a test Windows device enrolled in Intune, open Settings > Accounts > Access work or school > click the Intune enrollment entry > Info. Verify that the compliance status shows 'Compliant' when 'Require' is set and antispyware is enabled and up to date, or 'Noncompliant' when antispyware is disabled or out of date. 3. Run the following command on the device as an administrator to check the Antispyware status: 'Get-CimInstance -Namespace root\cimv2\mdm\dmmap -ClassName MDM_DeviceStatus_Antispyware01'. Confirm the 'Status' property matches the expected compliance state (e.g., 1 for enabled, 0 for disabled).

## Rollback
1. In the Microsoft Intune admin center, navigate to Endpoint security > Antivirus > Windows 10 and later compliance policies. Select the policy and change the 'Antispyware' setting back to 'Not configured' (default). 2. On the affected devices, force a sync by going to Settings > Accounts > Access work or school > click the Intune enrollment entry > Sync. 3. Verify the compliance policy no longer evaluates antispyware status by checking the device compliance status in the admin center or by running the command: 'Get-CimInstance -Namespace root\cimv2\mdm\dmmap -ClassName MDM_DeviceStatus_Antispyware01' and confirming the policy does not enforce a specific value.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-create-windows>
