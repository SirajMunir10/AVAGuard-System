# Troubleshooting: Site Recovery (70094)

**Domain:** Azure
**Subdomain:** Site Recovery
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve error 70094 when enabling replication for a Hyper-V virtual machine that is not highly available?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Hyper-V replication with Azure Site Recovery, VMM server

## Symptoms
- Cannot enable replication for a virtual machine
- Error message stating replication cannot be enabled as the machine is not highly available

## Error Codes
- `70094`

## Root Causes
1. Virtual machine is not highly available

## Remediation Steps
1. Restart the VMM service on the VMM server
2. Remove the virtual machine from the cluster and add it again

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/site-recovery/hyper-v-azure-troubleshoot>
