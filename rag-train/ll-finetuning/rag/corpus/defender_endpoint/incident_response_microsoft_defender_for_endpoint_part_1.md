# Incident Response: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Incident Response

## Scenario / Query
How do I contain a compromised unmanaged device from the network in Microsoft Defender for Endpoint to prevent lateral movement?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Onboarded devices running Windows 10 or Windows Server 2019+

## Symptoms
- Identified an unmanaged device that is compromised or potentially compromised
- Potential attack moving laterally across the network

## Error Codes
N/A

## Root Causes
1. Compromised or potentially compromised unmanaged device on the network

## Remediation Steps
1. Contain the device from the network to block incoming and outgoing communication with that device
2. Investigate and remediate the threat on the contained devices as soon as possible
3. After remediation, remove the devices from containment

## Validation
N/A

## Rollback
Remove the devices from containment after remediation

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
