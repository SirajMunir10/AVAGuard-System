# Troubleshooting: iOS Enrollment

**Domain:** Intune
**Subdomain:** iOS Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to verify WS-Trust 1.3 is enabled for enrolling ADE iOS/iPadOS devices with user affinity?

## Environment Context
- **Tenant Type:** Hybrid (on-premises AD FS with Intune)
- **Configuration:** AD FS WS-Trust 1.3 Username/Mixed endpoint

## Symptoms
- Automated Device Enrollment (ADE) iOS/iPadOS devices cannot be enrolled

## Error Codes
N/A

## Root Causes
1. WS-Trust 1.3 Username/Mixed endpoint is not enabled

## Remediation Steps
1. Use the Get-AdfsEndpoint PowerShell cmdlet to check for the trust/13/UsernameMixed endpoint
2. Example: Get-AdfsEndpoint -AddressPath "/adfs/services/trust/13/UsernameMixed"
3. If not enabled, enable WS-Trust 1.3 Username/Mixed endpoint in AD FS or contact your identity provider

## Validation
Run the following PowerShell command on the AD FS server to confirm the WS-Trust 1.3 Username/Mixed endpoint is enabled:

Get-AdfsEndpoint -AddressPath "/adfs/services/trust/13/UsernameMixed"

Verify that the output shows the endpoint with a status of 'Enabled'. If the endpoint is not listed or shows 'Disabled', the remediation has not succeeded.

## Rollback
If enabling the WS-Trust 1.3 Username/Mixed endpoint causes issues, disable it using the following PowerShell command on the AD FS server:

Set-AdfsEndpoint -TargetAddressPath "/adfs/services/trust/13/UsernameMixed" -Enabled $false

After disabling, confirm the change with:

Get-AdfsEndpoint -AddressPath "/adfs/services/trust/13/UsernameMixed"

Ensure the endpoint status now shows 'Disabled'.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-ios-enrollment-errors>
