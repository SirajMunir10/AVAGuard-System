# Troubleshooting: Endpoint Detection and Response

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Detection and Response
**Incident Type:** Troubleshooting

## Scenario / Query
How to submit a file for deep analysis in Microsoft Defender for Endpoint when the file is not available in the backend sample collection?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Windows 10, Windows 11, Windows Server 2012 R2+ devices

## Symptoms
- Submit for deep analysis button is not enabled
- File is not available in the Defender for Endpoint backend sample collection

## Error Codes
N/A

## Root Causes
1. File was not observed on a Windows 10, Windows 11, or Windows Server 2012 R2+ device
2. File has not been automatically collected by the backend

## Remediation Steps
1. Submit a sample through the Microsoft Defender portal if the file wasn't observed on a Windows 10 device (or Windows 11 or Windows Server 2012 R2+)
2. Wait for the Submit for deep analysis button to become available after submission

## Validation
Check that the Deep Analysis tab updates to display a summary and the date and time of the latest available results

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-file-alerts>
