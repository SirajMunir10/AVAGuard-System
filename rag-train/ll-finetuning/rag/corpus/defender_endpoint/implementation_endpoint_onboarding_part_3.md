# Implementation: Endpoint onboarding

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint onboarding
**Incident Type:** Implementation

## Scenario / Query
How to link a Group Policy Object to an Organization Unit for onboarding devices to Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Group Policy Management

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Right-click the Organization Unit (OU) and select 'Link an existing GPO'.
2. In the dialog box, select the Group Policy Object that you wish to link.
3. Click OK.

## Validation
Run 'Get-GPResultantSetOfPolicy -User <username> -Computer <computername> -ReportType Html -Path C:\GPReport.html' on a test device in the OU to confirm the GPO is applied. Then verify the device appears in Microsoft Defender for Endpoint portal under Devices > Onboarding.

## Rollback
In Group Policy Management Console, right-click the OU, select 'Link an existing GPO', uncheck the linked GPO, click OK. Then delete the GPO link from the OU.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-gp>
