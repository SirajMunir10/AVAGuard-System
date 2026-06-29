# Remediation: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Remediation

## Scenario / Query
How does a user self-remediate sign-in risk in Entra ID Identity Protection?

## Environment Context
- **Tenant Type:** Entra ID tenant with risk-based policies configured
- **Configuration:** Risk-based policy requiring MFA for sign-in risk

## Symptoms
- User is prompted to perform multifactor authentication (MFA) due to sign-in risk reaching the level set by risk-based policy

## Error Codes
N/A

## Root Causes
1. Sign-in risk reached the level set by the risk-based policy

## Remediation Steps
1. User performs multifactor authentication (MFA) when prompted
2. Upon successful MFA challenge, sign-in risk is remediated

## Validation
Risk state changes from 'At risk' to 'Remediated'; Risk detail changes from '-' to 'User passed multifactor authentication'

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-remediate-unblock>
