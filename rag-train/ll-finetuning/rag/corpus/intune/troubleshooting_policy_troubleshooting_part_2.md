# Troubleshooting: Policy Troubleshooting

**Domain:** Intune
**Subdomain:** Policy Troubleshooting
**Incident Type:** Troubleshooting

## Scenario / Query
How to check if Intune policies are applied correctly on iOS/iPadOS or Windows devices?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** iOS/iPadOS or Windows devices enrolled in Intune

## Symptoms
- Expected policies not shown under Device Compliance or Device Configuration in Company Portal or Settings

## Error Codes
N/A

## Root Causes
1. Policies not targeted correctly to the user or device

## Remediation Steps
1. On the iOS/iPadOS device, open the Company portal app > Devices > Choose the device from list > Check Settings
2. On a Windows device, open Settings > Accounts > Access Work or School > Select the account or MDM enrollment > Info > Sync
3. Select the device to see policy-specific information
4. If the expected policies aren't shown under Device Compliance or Device Configuration, open the policy and assign the policy to this user or device

## Validation
1. On the iOS/iPadOS device, open the Company Portal app, tap Devices, select the device, and check Settings. Verify that the expected policies appear under Device Compliance or Device Configuration. 2. On a Windows device, open Settings > Accounts > Access Work or School, select the account or MDM enrollment, click Info, then Sync. After sync, check that the expected policies are listed under Device Compliance or Device Configuration. 3. If policies are still missing, confirm in the Microsoft Intune admin center that the policy is assigned to the user or device by navigating to the policy and reviewing its assignments.

## Rollback
1. If the remediation causes unintended policy application, remove the user or device from the policy assignment in the Microsoft Intune admin center: navigate to the policy, select Assignments, and remove the user or device. 2. On the iOS/iPadOS device, open Company Portal, select the device, and tap Remove Device to unenroll if needed. 3. On a Windows device, go to Settings > Accounts > Access Work or School, select the account, and click Disconnect to remove MDM enrollment. Re-enroll the device if necessary.

## References
- <https://learn.microsoft.com/en-us/mem/intune/configuration/troubleshoot-policies-in-microsoft-intune>
