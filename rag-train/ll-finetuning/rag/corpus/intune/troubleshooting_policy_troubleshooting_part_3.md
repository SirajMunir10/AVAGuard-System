# Troubleshooting: Policy Troubleshooting

**Domain:** Intune
**Subdomain:** Policy Troubleshooting
**Incident Type:** Troubleshooting

## Scenario / Query
How to interpret Intune policy states like Not Applicable, Conflict, Pending, or Errors?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Any device platform

## Symptoms
- Policy state shows Not Applicable, Conflict, Pending, or Errors

## Error Codes
N/A

## Root Causes
1. Not Applicable: Policy isn't supported on this platform (e.g., iOS/iPadOS policies on Android, Samsung KNOX policies on Windows)
2. Conflict: Existing setting on the device that Intune can't override, or two policies with the same setting using different values
3. Pending: Device hasn't checked into Intune to get the policy, or device received the policy but hasn't reported the status
4. Errors: Unknown; refer to troubleshooting documentation

## Remediation Steps
1. For Not Applicable: Verify policy platform targeting
2. For Conflict: Review and reconcile conflicting policies or device settings
3. For Pending: Ensure device syncs with Intune
4. For Errors: Look up errors and possible resolutions at Troubleshoot company resource access problems

## Validation
1. For each device showing a policy state, navigate to Microsoft Intune admin center > Devices > All devices > select the device > Device configuration. Verify the policy assignment and status. 2. For 'Not Applicable': Confirm the policy's platform targeting matches the device OS (e.g., iOS policy on Android will show Not Applicable). 3. For 'Conflict': Check if the same setting is configured by two different policies with different values; review policy assignments and settings. 4. For 'Pending': Trigger a sync from the device (Settings > Accounts > Access Work or School > Info > Sync) or from Intune (select device > Sync). 5. For 'Errors': Use the error code reference at https://learn.microsoft.com/en-us/mem/intune/configuration/troubleshoot-policies-in-microsoft-intune to identify the specific error and resolution.

## Rollback
1. For 'Not Applicable': Remove the policy assignment from the unsupported platform or adjust the policy's platform targeting. 2. For 'Conflict': Remove or modify one of the conflicting policies so that the same setting is not assigned with different values. 3. For 'Pending': No rollback needed; ensure device connectivity and retry sync. 4. For 'Errors': Refer to the troubleshooting documentation for the specific error code and follow the recommended resolution steps; if a policy change caused the error, revert that change.

## References
- <https://learn.microsoft.com/en-us/mem/intune/configuration/troubleshoot-policies-in-microsoft-intune>
