# Incident Response: Microsoft Defender for Identity

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Identity
**Incident Type:** Incident Response

## Scenario / Query
How to audit downloads of reports and Excel files in Microsoft Defender for Identity?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Audit log enabled

## Symptoms
- Suspicious downloads of Domain Controller coverage Excel, reports, or security alert Excel files

## Error Codes
N/A

## Root Causes
1. The Domain Controller coverage Excel file was downloaded (DomainControllerCoverageExcelDownloaded)
2. A report was downloaded (ReportDownloaded)
3. The detailed Excel file of an alert was downloaded (AlertExcelDownloaded)

## Remediation Steps
1. Review the audit log for DomainControllerCoverageExcelDownloaded, ReportDownloaded, and AlertExcelDownloaded activities
2. Investigate the user and context of the downloads

## Validation
1. Sign in to the Microsoft 365 Defender portal (https://security.microsoft.com) as a user with the Audit Log or Security Reader role.
2. Navigate to 'Audit' under 'Solutions' > 'Audit'.
3. Set the 'Activities' filter to 'Downloaded Domain Controller coverage Excel file' (DomainControllerCoverageExcelDownloaded), 'Downloaded report' (ReportDownloaded), and 'Downloaded alert Excel file' (AlertExcelDownloaded).
4. Set the date range to cover the suspected incident period.
5. Click 'Search' and confirm that no entries for these activities appear for unauthorized users or unexpected contexts.
6. If entries exist, verify that the associated user, IP address, and timestamp match legitimate business activity.

## Rollback
1. If the audit log reveals unauthorized downloads, immediately:
   a. Disable the compromised user account via the Microsoft 365 admin center (https://admin.microsoft.com) or using the `Disable-AzureADUser` cmdlet.
   b. Reset the user's password and enforce MFA re-registration.
2. For any downloaded files, check Microsoft Defender for Identity's 'Sensitive groups' reports and ensure no changes were made to domain controller configurations.
3. If the downloaded files contained sensitive data, initiate a data breach response per your organization's incident response plan.
4. Review and tighten conditional access policies to restrict download capabilities for Defender for Identity reports to trusted locations and devices.
5. Enable alert policies for these activities to trigger automatic investigation and response in future.

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
