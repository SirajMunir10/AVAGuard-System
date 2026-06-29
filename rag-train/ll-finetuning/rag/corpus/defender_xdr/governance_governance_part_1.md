# Governance: Governance

**Domain:** Defender XDR
**Subdomain:** Governance
**Incident Type:** Governance

## Scenario / Query
A security administrator notices that some devices in the tenant are not reporting to Microsoft Defender for Endpoint. How can the administrator use Microsoft 365 Defender advanced hunting to identify devices that have not sent any data in the last 30 days?

## Environment Context
- **Tenant Type:** Microsoft 365 E5
- **Configuration:** Microsoft Defender for Endpoint onboarded devices

## Symptoms
- Devices missing from the device inventory
- Incomplete coverage in threat analytics

## Error Codes
N/A

## Root Causes
1. Devices may be offboarded, decommissioned, or have lost connectivity
2. Devices may have been removed from the tenant without proper governance tracking

## Remediation Steps
1. Run the advanced hunting query documented in 'Find devices with missing or incomplete sensor data' to list devices with no recent data
2. Review the device inventory in Microsoft 365 Defender to confirm device status
3. Re-onboard devices that are still active but missing, following the onboarding guidance in 'Onboard devices to Microsoft Defender for Endpoint'

## Validation
Run the advanced hunting query and verify that the returned list matches devices that are expected to be active but are not reporting.

## Rollback
If re-onboarding causes duplicate entries, remove the old device record from the portal and ensure the new onboarding package is used.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/advanced-hunting-find-missing-sensor-data>
