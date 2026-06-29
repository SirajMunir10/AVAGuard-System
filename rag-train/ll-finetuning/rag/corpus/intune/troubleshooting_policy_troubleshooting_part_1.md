# Troubleshooting: Policy Troubleshooting

**Domain:** Intune
**Subdomain:** Policy Troubleshooting
**Incident Type:** Troubleshooting

## Scenario / Query
How to use the built-in Troubleshoot pane in Microsoft Intune to review compliance and configuration statuses for a user's device?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Intune admin center

## Symptoms
- User is having an issue with compliance or configuration policies

## Error Codes
N/A

## Root Causes
1. Device not enrolled (Managed not set to MDM or EAS/MDM)
2. Device not registered in Microsoft Entra join (Not Registered)
3. Device non-compliant (Intune compliant or Microsoft Entra compliant shows No)
4. Device not checking in (Last check in more than 24 hours)

## Remediation Steps
1. In the Microsoft Intune admin center, select Troubleshooting + support > Troubleshoot.
2. Choose Select user > select the user having an issue > Select.
3. Confirm that Intune license shows the green check.
4. Under Devices, find the device having an issue.
5. Review the different columns: Managed, Microsoft Entra join Type, Intune compliant, Microsoft Entra compliant, Last check in.
6. If Managed isn't set to MDM or EAS/MDM, the device isn't enrolled; enroll the device.
7. If Microsoft Entra join Type is Not Registered, unenroll and re-enroll the device.
8. If Intune compliant or Microsoft Entra compliant shows No, check compliance policies or device connectivity (e.g., device turned off or no network connection).
9. If Last check in is more than 24 hours, force check-in: On Android, open Company Portal app > Devices > Choose device > Check Device Settings. On iOS/iPadOS, open Company Portal app > Devices > Choose device > Check Settings. On Windows, open Settings > Accounts > Access Work or School > Select account or MDM enrollment > Info > Sync.
10. Select the device to see policy-specific information.

## Validation
Confirm that Managed shows MDM or EAS/MDM, Microsoft Entra join Type shows Workplace or AzureAD, Intune compliant and Microsoft Entra compliant show Yes, and Last check in is recent.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/configuration/troubleshoot-policies-in-microsoft-intune>
