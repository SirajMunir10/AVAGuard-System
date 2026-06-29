# Implementation: Compliance Policies

**Domain:** Intune
**Subdomain:** Compliance Policies
**Incident Type:** Implementation

## Scenario / Query
How do I configure Microsoft Defender for Endpoint rules in a Windows compliance policy to require a specific machine risk score?

## Environment Context
- **Tenant Type:** Intune-managed Windows devices
- **Configuration:** Microsoft Defender for Endpoint integration with Conditional Access

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the setting 'Require the device to be at or under the machine risk score' to take the risk assessment from your defense threat services as a condition for compliance.
2. Choose the maximum allowed threat level from the following options: Not configured (default), Clear, Low, Medium, High.
3. Clear - This option is the most secure, as the device can't have any threats. If the device is detected as having any level of threats, it's evaluated as noncompliant.
4. Low - The device is evaluated as compliant if only low-level threats are present. Anything higher puts the device in a noncompliant status.
5. Medium - The device is evaluated as compliant if existing threats on the device are low or medium level. If the device is detected to have high-level threats, it's determined to be noncompliant.
6. High - This option is the least secure, and allows all threat levels. It may be useful if you're using this solution only for reporting purposes.
7. To set up Microsoft Defender for Endpoint as your defense threat service, see Enable Microsoft Defender for Endpoint with Conditional Access.

## Validation
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to Endpoint security > Device compliance > Policies.
3. Select the Windows compliance policy you configured.
4. Under Compliance settings > Microsoft Defender for Endpoint, verify that 'Require the device to be at or under the machine risk score' is set to 'Require'.
5. Confirm the selected maximum allowed threat level matches your intended value (e.g., Clear, Low, Medium, High).
6. On a test Windows device that is enrolled in Intune and has Microsoft Defender for Endpoint onboarded, trigger a compliance evaluation by going to Settings > Accounts > Access work or school > Info > Sync.
7. In the Intune admin center, go to Devices > Monitor > Device compliance and verify the device shows as 'Compliant' if its risk score is at or below the configured level, or 'Noncompliant' if above.
8. Optionally, use Microsoft Graph API to query the compliance policy status: GET https://graph.microsoft.com/beta/deviceManagement/deviceCompliancePolicies/{policyId}/deviceStatuses

## Rollback
1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to Endpoint security > Device compliance > Policies.
3. Select the Windows compliance policy where the risk score setting was configured.
4. Under Compliance settings > Microsoft Defender for Endpoint, set 'Require the device to be at or under the machine risk score' to 'Not configured'.
5. Alternatively, change the maximum allowed threat level to a less restrictive value (e.g., from 'Clear' to 'Low' or 'Medium') if the original setting is too strict.
6. Select Review + save to apply the changes.
7. On affected devices, force a sync by going to Settings > Accounts > Access work or school > Info > Sync.
8. Monitor device compliance status in Intune admin center under Devices > Monitor > Device compliance to confirm devices return to expected compliance state.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-create-windows>
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
