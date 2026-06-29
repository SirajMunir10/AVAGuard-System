# Troubleshooting: Password Reset (OnBoardingServiceError)

**Domain:** Entra ID
**Subdomain:** Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve OnBoardingServiceError during SSPR writeback?

## Environment Context
- **Tenant Type:** Entra ID
- **Configuration:** SSPR writeback

## Symptoms
- On-premises service couldn't properly communicate with the password-reset web service to initiate the onboarding process

## Error Codes
- `OnBoardingServiceError`

## Root Causes
1. Firewall rule blocking outbound connections
2. Problem getting an authentication token for your tenant

## Remediation Steps
1. Ensure that you're not blocking outbound connections over TCP 443 and TCP 9350-9354 or to https://ssprdedicatedsbprodncu.servicebus.windows.net
2. Ensure that the Microsoft Entra admin account you're using to onboard isn't federated

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
