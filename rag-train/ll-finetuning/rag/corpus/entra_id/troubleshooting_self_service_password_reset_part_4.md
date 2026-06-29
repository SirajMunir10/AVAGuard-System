# Troubleshooting: Self-Service Password Reset (SSPR_0030)

**Domain:** Entra ID
**Subdomain:** Self-Service Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
A user receives SSPR_0030 error: 'We can't reset your password due to a poor connection with your on-premises environment' or 'OnPremisesConnectivityError = 30' with message about connectivity issues. How to resolve?

## Environment Context
- **Tenant Type:** Entra ID with on-premises synchronization
- **Configuration:** Password writeback connectivity

## Symptoms
- User sees error SSPR_0030
- User sees error code OnPremisesConnectivityError = 30
- Message: 'We're sorry, we can't reset your password at this time because of connectivity issues to your organization.' or 'We can't reset your password due to a poor connection with your on-premises environment.'

## Error Codes
- `SSPR_0030`
- `OnPremisesConnectivityError = 30`

## Root Causes
1. Connectivity issues between Entra ID and on-premises environment

## Remediation Steps
1. Try again later as the problem might be resolved if you try again later
2. If the problem persists, contact your admin and ask them to investigate
3. Admin should review 'Troubleshoot password writeback connectivity' for more information about connectivity issues

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr>
