# Incident Response: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Incident Response

## Scenario / Query
How do I stop and quarantine a malicious file in my network using Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint tenant
- **Configuration:** Devices must run Windows 10 version 1703 or later, Windows 11, or Windows Server 2012 R2 or later. Microsoft Defender Antivirus must be at least in Passive mode.

## Symptoms
- Malicious process running on a device
- File observed on a device within the last 30 days

## Error Codes
N/A

## Root Causes
1. File does not belong to trusted non-Microsoft publishers or is not signed by Microsoft

## Remediation Steps
1. Ensure the device is running Windows 10 version 1703 or later, Windows 11, or Windows Server 2012 R2 or later.
2. Verify that Microsoft Defender Antivirus is at least running in Passive mode.
3. Confirm the file does not belong to trusted non-Microsoft publishers or is not signed by Microsoft.
4. Initiate the Stop and Quarantine File action from the Microsoft Defender for Endpoint portal.
5. The action will stop running processes, quarantine the files, and delete persistent data such as registry keys.

## Validation
The file is quarantined and can be restored from quarantine at any time.

## Rollback
You'll be able to restore the file from quarantine at any time.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-file-alerts>
