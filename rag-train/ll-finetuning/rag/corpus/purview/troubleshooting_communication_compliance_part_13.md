# Troubleshooting: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot the 'An error occurred' message when using Copilot in Microsoft Purview to summarize a communication compliance message?

## Environment Context
- **Tenant Type:** Microsoft 365 E5/A5/G5 or Compliance add-on
- **Configuration:** Copilot in Microsoft Purview must be onboarded; user must have Communication Compliance, Communication Compliance Analysts, or Communication Compliance Investigators role plus Security Copilot contributor role

## Symptoms
- Generic error message 'An error occurred' after selecting Summarize in Communication Compliance

## Error Codes
N/A

## Root Causes
1. User does not have the required license for Copilot in Microsoft Purview
2. User does not have the required Communication Compliance role (Communication Compliance, Communication Compliance Analysts, or Communication Compliance Investigators)
3. User does not have the Security Copilot contributor role
4. Internal error on Microsoft side

## Remediation Steps
1. Verify the user has the required license for Copilot in Microsoft Purview
2. Ensure the user is a member of one of the following roles: Communication Compliance, Communication Compliance Analysts, or Communication Compliance Investigators
3. Ensure the user has the Security Copilot contributor role (should be turned on by default for all users in a Microsoft Entra organization)
4. If the issue persists, check for internal errors and contact Microsoft support

## Validation
1. Confirm the user has a Microsoft 365 E5/A5/G5 or Compliance add-on license assigned in the Microsoft 365 admin center (https://admin.microsoft.com).
2. Verify the user is a member of one of the following roles in the Microsoft Purview compliance portal: Communication Compliance, Communication Compliance Analysts, or Communication Compliance Investigators.
3. Verify the user has the Security Copilot contributor role assigned in Microsoft Entra ID (https://entra.microsoft.com).
4. As a test, have the user navigate to a communication compliance message and select 'Summarize' to confirm the error no longer appears.

## Rollback
1. If the license was added, remove the Copilot in Microsoft Purview license from the user in the Microsoft 365 admin center.
2. If a Communication Compliance role was added, remove the user from that role in the Microsoft Purview compliance portal.
3. If the Security Copilot contributor role was added, remove the user from that role in Microsoft Entra ID.
4. If the issue persists after remediation, contact Microsoft support for further investigation of internal errors.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
