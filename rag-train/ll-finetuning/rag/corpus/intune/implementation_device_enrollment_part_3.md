# Implementation: Device Enrollment

**Domain:** Intune
**Subdomain:** Device Enrollment
**Incident Type:** Implementation

## Scenario / Query
When configuring automatic enrollment for Windows devices in Microsoft Intune, users report that devices are not automatically enrolled even though the MDM user scope is set to 'All'. What configuration step is missing?

## Environment Context
- **Tenant Type:** Microsoft Entra ID (Azure AD) with Intune
- **Configuration:** MDM user scope set to 'All' in Microsoft Entra ID > Mobility (MDM and MAM) > Microsoft Intune

## Symptoms
- Windows devices are not automatically enrolled in Intune during Azure AD join or domain join
- No enrollment errors appear in the user or device logs
- The MDM user scope is correctly set to 'All'

## Error Codes
N/A

## Root Causes
1. The MAM user scope is not configured or is set to 'None' while the MDM user scope is set to 'All'
2. The MDM terms of use URL, MDM discovery URL, or MDM compliance URL are not correctly populated in the Microsoft Entra ID Mobility configuration

## Remediation Steps
1. Navigate to Microsoft Entra admin center > Identity > Devices > Device settings > MDM and MAM
2. Ensure the MAM user scope is also set to 'All' or 'Some' as appropriate for your environment
3. Verify that the MDM terms of use URL, MDM discovery URL, and MDM compliance URL are correctly filled with the Intune service endpoints (e.g., https://enrollment.manage.microsoft.com/enrollmentserver/discovery.svc)
4. Save the configuration and allow up to one hour for propagation

## Validation
After configuration, perform a fresh Azure AD join on a test Windows device and confirm it appears in Microsoft Intune admin center under Devices > All devices within 15 minutes.

## Rollback
Set the MDM user scope to 'None' and clear the MAM user scope to 'None' to disable automatic enrollment.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/windows-enroll>
