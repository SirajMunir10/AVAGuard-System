# Implementation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Implementation

## Scenario / Query
How to configure the Policy Match Preservation setting in Communication Compliance to specify how long to save policy matches?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance global settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign in to the Microsoft Purview portal with credentials for an admin account in your Microsoft 365 organization.
2. Select the Settings button in the upper-right corner of the page, then select Communication Compliance to go to the Communication Compliance global settings.
3. Select the Policy Match Preservation setting, then select a new time period.
4. Select Confirm in the confirmation dialog box.

## Validation
1. Sign in to the Microsoft Purview portal (https://compliance.microsoft.com) with admin credentials.
2. Select the Settings button (gear icon) in the upper-right corner, then select Communication Compliance.
3. Under Policy Match Preservation, verify that the displayed time period matches the newly configured value.
4. Optionally, use the Get-CommunicationCompliancePolicy cmdlet in Security & Compliance PowerShell to confirm the RetentionDuration property: Get-CommunicationCompliancePolicy | Format-List Name,RetentionDuration.

## Rollback
1. Sign in to the Microsoft Purview portal with admin credentials.
2. Select Settings > Communication Compliance.
3. Under Policy Match Preservation, select the previous time period (e.g., the original default or prior setting).
4. Select Confirm in the confirmation dialog box.
5. Verify the change by checking the displayed value or using Get-CommunicationCompliancePolicy to confirm the RetentionDuration property has been restored.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
