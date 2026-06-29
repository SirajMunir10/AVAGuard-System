# Troubleshooting: Password Reset Writeback (OffBoardingError)

**Domain:** Entra ID
**Subdomain:** Password Reset Writeback
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot OffBoardingError event in SSPR writeback?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** SSPR writeback configuration

## Symptoms
- On-premises service cannot communicate with password-reset web service to initiate offboarding

## Error Codes
- `OffBoardingError`

## Root Causes
1. Firewall rule blocking outbound connections
2. Problem getting an authorization token for the tenant
3. Microsoft Entra admin account used for offboarding is federated

## Remediation Steps
1. Ensure outbound connections over 443 are not blocked
2. Ensure outbound connections to https://ssprdedicatedsbprodncu.servicebus.windows.net are not blocked
3. Ensure the Microsoft Entra admin account used to offboard is not federated

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
