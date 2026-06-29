# Incident Response: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Incident Response

## Scenario / Query
How to handle threat-informed remediation actions taken by Microsoft on your behalf in Microsoft Entra ID?

## Environment Context
- **Tenant Type:** Microsoft Entra tenant
- **Configuration:** Identity Protection enabled

## Symptoms
- Microsoft Threat Intelligence identifies accounts, sessions, or resources being actively used in attack campaigns targeting Microsoft Entra tenants
- Microsoft has high-confidence evidence of compromise that poses an active risk to your organization
- Microsoft might take remediation action on your behalf to help contain the threat

## Error Codes
N/A

## Root Causes
1. Microsoft Threat Intelligence identifies accounts, sessions, or resources being actively used in attack campaigns targeting Microsoft Entra tenants
2. Microsoft has high-confidence evidence of compromise that poses an active risk to your organization

## Remediation Steps
1. Review the Microsoft Entra audit logs to see actions recorded with Microsoft listed as the initiator
2. Administrators retain full control of their tenant and can reverse any action taken through this process after completing their own investigation

## Validation
N/A

## Rollback
Administrators retain full control of their tenant and can reverse any action taken through this process after completing their own investigation

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock>
