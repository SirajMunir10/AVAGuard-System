# Troubleshooting: Self-Service Password Reset (SSPR_0029)

**Domain:** Entra ID
**Subdomain:** Self-Service Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
A user receives SSPR_0029 error: 'We're unable to reset your password due to an error in your on-premises configuration' or 'OnPremisesAdminActionRequired = 29' with message about a problem with the organization's password reset configuration. How to resolve?

## Environment Context
- **Tenant Type:** Entra ID with on-premises synchronization
- **Configuration:** Password writeback enabled

## Symptoms
- User sees error SSPR_0029
- User sees error code OnPremisesAdminActionRequired = 29
- Message: 'We're sorry, we can't reset your password at this time because of a problem with your organization's password reset configuration.' or 'We can't reset your password at this time because of a problem with your organization's password reset configuration.'

## Error Codes
- `SSPR_0029`
- `OnPremisesAdminActionRequired = 29`

## Root Causes
1. Error in on-premises configuration related to password reset

## Remediation Steps
1. Contact your admin and ask them to investigate
2. Admin should review 'Troubleshoot password writeback' for more information about the potential problem

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr>
