# Optimization: Device Configuration

**Domain:** Intune
**Subdomain:** Device Configuration
**Incident Type:** Optimization

## Scenario / Query
How can I optimize Intune policy deployment by reducing the number of overlapping or conflicting device configuration profiles for Windows 10/11 devices?

## Environment Context
- **Tenant Type:** Enterprise (Microsoft 365 E5)
- **Configuration:** Multiple device configuration profiles (e.g., settings catalog, administrative templates, custom OMA-URI) assigned to the same device groups, causing slow policy processing and user complaints about delayed settings enforcement.

## Symptoms
- Devices report prolonged policy check-in times (over 30 minutes)
- Intune console shows multiple profiles with conflicting settings (e.g., different password policies)
- Helpdesk tickets about settings not applying consistently

## Error Codes
N/A

## Root Causes
1. Overlapping profile assignments without proper exclusion or priority
2. Use of redundant settings across multiple profiles (e.g., same setting in Settings Catalog and Administrative Templates)
3. Lack of a structured profile design (e.g., using baseline profiles instead of granular per-setting profiles)

## Remediation Steps
1. Review existing device configuration profiles in the Intune admin center and identify overlapping assignments
2. Consolidate settings into fewer, purpose-built profiles (e.g., one security baseline profile, one user experience profile)
3. Use the Settings Catalog to manage settings in a single pane instead of mixing Administrative Templates and OMA-URI
4. Apply profiles to groups using exclusion tags to avoid double assignment
5. Monitor policy processing using the Intune reports > Device configuration > Assignment status

## Validation
Verify that devices check in within 15 minutes and that no conflicting settings appear in the Intune console under 'Device configuration > Assignment status'.

## Rollback
If consolidation causes unintended behavior, revert to the previous profile assignments by reassigning the original profiles and removing the new consolidated ones.

## References
- <https://learn.microsoft.com/en-us/mem/intune/configuration/device-profile-optimize>
