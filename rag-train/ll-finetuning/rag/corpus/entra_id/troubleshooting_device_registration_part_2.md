# Troubleshooting: Device Registration

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to interpret the Virtual Desktop field in dsregcmd output for VDI device metadata?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** N/A

## Symptoms
- Virtual Desktop field shows NOT SET - VDI device metadata isn't present on the device
- Virtual Desktop field shows YES - VDI device metadata is present and dsregcmd outputs associated metadata
- Virtual Desktop field shows INVALID - The VDI device metadata is present but not set correctly

## Error Codes
N/A

## Root Causes
1. VDI device metadata not present on the device
2. VDI device metadata present but not set correctly

## Remediation Steps
1. For NOT SET: No action needed if VDI is not in use
2. For YES: Review associated metadata including Provider, Type (Persistent or non-persistent), User mode (Single user or multi-user), and Extensions
3. For INVALID: Correct the VDI device metadata as dsregcmd outputs the incorrect metadata

## Validation
Virtual Desktop field shows YES with correct metadata

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-device-dsregcmd>
