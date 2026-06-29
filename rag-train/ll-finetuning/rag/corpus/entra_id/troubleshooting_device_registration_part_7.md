# Troubleshooting: Device Registration

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Cloud Kerberos trust deployment using dsregcmd /status?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Cloud Kerberos trust deployment, CertEnrollment state is none

## Symptoms
- Issues accessing on-premises resources with Cloud Kerberos

## Error Codes
N/A

## Root Causes
1. Device does not have a Cloud Kerberos ticket to access on-premises resources

## Remediation Steps
1. Run dsregcmd /status
2. Check OnPremTGT setting (named CloudTGT prior to Windows 11 version 23H2)
3. Verify OnPremTGT is set to YES

## Validation
OnPremTGT set to YES indicates device has a Cloud Kerberos ticket for on-premises access

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-device-dsregcmd>
