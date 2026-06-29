# Troubleshooting: Device Configuration

**Domain:** Intune
**Subdomain:** Device Configuration
**Incident Type:** Troubleshooting

## Scenario / Query
How do I confirm a configuration profile is correctly applied to a device in Microsoft Intune?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Device configuration profiles

## Symptoms
- Device configuration profile status is not Conforms
- Profile status shows Not applicable or Pending

## Error Codes
N/A

## Root Causes
1. Profile setting is not applicable to the device platform (e.g., iOS email settings on Android)
2. Profile has been sent to the device but the device has not yet reported the status to Intune (e.g., encryption on Android requires user action)

## Remediation Steps
1. Sign in to the Microsoft Intune admin center
2. Select Devices > All devices > select the device > Device configuration
3. Review the Status for each profile: Conforms (device received and conforms), Not applicable (setting not applicable), Pending (profile sent but not yet reported)

## Validation
Check that the profile status shows Conforms after following the steps

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/configuration/troubleshoot-policies-in-microsoft-intune>
