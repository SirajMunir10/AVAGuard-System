# Troubleshooting: Site Recovery (status 11)

**Domain:** Azure
**Subdomain:** Site Recovery
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve VSS writer NTDS failure with status 11 and error 0x800423F4 when enabling replication in Azure Site Recovery?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** Hyper-V host and virtual machine operating system versions

## Symptoms
- Enable replication failed as NTDS failed

## Error Codes
- `status 11`
- `0x800423F4`

## Root Causes
1. The virtual machine's operating system is Windows Server 2012 and not Windows Server 2012 R2

## Remediation Steps
1. Upgrade to Windows Server R2 with 4072650 applied
2. Ensure that Hyper-V Host is also Windows 2016 or higher

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/site-recovery/hyper-v-azure-troubleshoot>
