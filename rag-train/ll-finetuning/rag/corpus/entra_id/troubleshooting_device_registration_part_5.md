# Troubleshooting: Device Registration (0x801c001d)

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to diagnose pre-join failures for a domain-joined device that cannot Microsoft Entra hybrid join?

## Environment Context
- **Tenant Type:** Microsoft Entra hybrid joined
- **Configuration:** Device is domain-joined and unable to Microsoft Entra hybrid join

## Symptoms
- Device is domain-joined but unable to Microsoft Entra hybrid join
- Join failures in pre-check phase
- Join errors in discover phase with error code 0x801c001d

## Error Codes
- `0x801c001d`

## Root Causes
1. AD Connectivity Test failure: connectivity issue to domain controller
2. AD Configuration Test failure: Service Connection Point (SCP) object not configured properly in on-premises Active Directory forest
3. DRS Discovery Test failure: unable to get DRS endpoints from discovery metadata endpoint or perform user realm request
4. DRS Connectivity Test failure: basic connectivity issue to DRS endpoint
5. Token Acquisition Test failure: unable to get Microsoft Entra authentication token for federated tenant

## Remediation Steps
1. Run dsregcmd /status from an elevated command prompt to run diagnostics in SYSTEM context
2. Check the error phase, error code, server request ID, server response HTTP status, and server response error message from the diagnostics section
3. Resolve AD Connectivity Test errors by ensuring connectivity to the domain controller
4. Resolve AD Configuration Test errors by verifying and properly configuring the Service Connection Point (SCP) object in on-premises Active Directory forest
5. Resolve DRS Discovery Test errors by ensuring DRS endpoints are reachable and user realm request succeeds
6. Resolve DRS Connectivity Test errors by ensuring basic connectivity to the DRS endpoint
7. Resolve Token Acquisition Test errors by troubleshooting Microsoft Entra authentication token acquisition for federated tenants

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-device-dsregcmd>
