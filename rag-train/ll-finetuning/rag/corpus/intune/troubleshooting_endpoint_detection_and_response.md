# Troubleshooting: Endpoint Detection and Response

**Domain:** Intune
**Subdomain:** Endpoint Detection and Response
**Incident Type:** Troubleshooting

## Scenario / Query
How to monitor device onboarding status for Microsoft Defender for Endpoint in Intune?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** Endpoint security > Endpoint detection and response

## Symptoms
- Devices not appearing in Defender portal under Endpoints > Device inventory
- EDR Onboarding Status does not show 'Successfully onboarded'
- Risk levels missing from device compliance reports

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In the Intune admin center, go to Endpoint security > Endpoint detection and response > EDR Onboarding Status tab.
2. Review the onboarding status for all platforms.
3. Ensure your account has Read permission for Microsoft Defender Advanced Threat Protection in Intune RBAC.

## Validation
Devices appear in the Defender portal under Endpoints > Device inventory. EDR Onboarding Status shows 'Successfully onboarded'. Risk levels appear in device compliance reports.

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
