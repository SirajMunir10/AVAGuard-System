# Troubleshooting: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Troubleshooting

## Scenario / Query
How can I determine if a device is connected to a Corporate network for Endpoint DLP?

## Environment Context
- **Tenant Type:** Microsoft 365 with Purview
- **Configuration:** Endpoint DLP network restrictions

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Run the Get-NetConnectionProfile cmdlet as an administrator.
2. Check the NetworkCategoryId in the output. If it is DomainAuthenticated, the machine is connected to the Corporate network. If the output is anything else, the machine isn't.

## Validation
Run the Get-NetConnectionProfile cmdlet as an administrator on the device. Confirm that the NetworkCategoryId in the output is DomainAuthenticated. If it is, the device is connected to the Corporate network as required for Endpoint DLP.

## Rollback
If the remediation fails or causes issues, verify the device's network connection status using the same Get-NetConnectionProfile cmdlet. If the NetworkCategoryId is not DomainAuthenticated, ensure the device is joined to the corporate domain and connected to the corporate network. No specific rollback command is provided in the source documentation; consult the network administrator to resolve domain connectivity.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
