# Governance: Compliance Policies

**Domain:** Intune
**Subdomain:** Compliance Policies
**Incident Type:** Governance

## Scenario / Query
An Intune administrator notices that a compliance policy for Windows 10/11 devices is not being applied to all targeted devices, and some devices show a status of 'Not evaluated' even though they are enrolled and active. What steps should be taken to identify and resolve the governance gap?

## Environment Context
- **Tenant Type:** Enterprise (Microsoft Intune standalone)
- **Configuration:** Compliance policy for Windows 10/11 with device health attestation settings enabled; devices are Azure AD joined and enrolled via automatic enrollment.

## Symptoms
- Devices show compliance status 'Not evaluated' in the Microsoft Intune admin center
- Compliance policy reports indicate fewer devices evaluated than expected
- No errors or conflicts visible in the policy assignment overview

## Error Codes
N/A

## Root Causes
1. The compliance policy requires device health attestation (e.g., BitLocker, Secure Boot, Code Integrity) but the devices do not have the required attestation data reported
2. The policy assignment is not correctly scoped to all device groups, or group membership has changed
3. Devices are not checking in to Intune frequently enough to receive the policy evaluation

## Remediation Steps
1. Verify that the compliance policy is assigned to the correct Azure AD groups and that all targeted devices are members of those groups
2. Ensure devices have the latest Intune management extension and are checking in; instruct users to sync devices from the Company Portal or remotely trigger a sync from the admin center
3. Check device health attestation settings: confirm that the device meets the minimum OS version (Windows 10 1809 or later) and that the TPM is enabled and attested
4. Review the compliance policy settings for any conflicting or overlapping policies that might take precedence

## Validation
After remediation, confirm that affected devices show a compliance status of 'Compliant' or 'Noncompliant' in the Intune admin center and that the policy evaluation count matches the number of targeted devices.

## Rollback
If the issue persists, temporarily remove the device health attestation requirements from the compliance policy and reassign to isolate the root cause.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-monitor>
