# Implementation: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Implementation

## Scenario / Query
How to isolate a device from the network using Microsoft Defender for Endpoint on Windows 10 version 1709 or later, including selective isolation and enabling Outlook/Teams connectivity?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Windows 10 version 1709 or later

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Isolate device on the device page.
2. Type a comment and select Confirm.

## Validation
The Action center shows the scan information and the device timeline includes a new event.

## Rollback
Select Release from isolation on the device page and follow the same steps as isolating the device.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
