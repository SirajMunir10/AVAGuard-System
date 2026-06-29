# Troubleshooting: Site Recovery

**Domain:** Azure
**Subdomain:** Site Recovery
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot performance issues related to network bandwidth limitations affecting Hyper-V replication to Azure?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Hyper-V replication to Azure using Site Recovery

## Symptoms
- Network bandwidth limitations affecting replication

## Error Codes
N/A

## Root Causes
1. Bandwidth or throttling constraints in the environment
2. High data churn on a VM
3. HRL log files exceed 50% of available disk space
4. Replication is paused, causing continued writes to the hrl file

## Remediation Steps
1. Check if there are bandwidth or throttling constraints in your environment
2. Run the Deployment Planner profiler
3. After running the profiler, follow the bandwidth and storage recommendations
4. Check data churn limitations
5. If high data churn is seen on a VM, check if the VM is marked for resynchronization
6. Follow steps to investigate the source of the churn
7. If HRL log files exceed 50% of available disk space, provision more storage space for all VMs on which the issue occurs
8. Check that replication isn't paused; if it is, it continues writing changes to the hrl file, which can contribute to its increased size

## Validation
1. Run the Deployment Planner profiler to assess bandwidth and data churn: https://learn.microsoft.com/en-us/azure/site-recovery/hyper-v-deployment-planner-run. 2. Check if replication is paused by reviewing the VM replication health in the Azure portal or via PowerShell: Get-ASRReplicationProtectedItem -FriendlyName <VMName> | Select-Object *ReplicationHealth*. 3. Verify HRL log file size on the Hyper-V host: Check the %SystemDrive%\ProgramData\Microsoft Azure Site Recovery\Data\*.hrl files; if any exceed 50% of available disk space, proceed with storage provisioning. 4. Confirm data churn rate using the profiler output; if churn exceeds 10 MB/s for standard replication, investigate source of churn (e.g., backup jobs, defragmentation).

## Rollback
1. If bandwidth throttling was applied, remove or adjust the throttling rule (e.g., via Group Policy or network QoS). 2. If additional storage was provisioned for HRL logs, revert to original disk configuration if no longer needed. 3. If replication was resumed after being paused, re-pause replication only if necessary to control churn: Set-ASRReplicationProtectedItem -ProtectionDirection <PrimaryToRecovery> -Pause. 4. If data churn source mitigation (e.g., disabling a backup job) caused issues, re-enable the original job.

## References
- <https://learn.microsoft.com/en-us/azure/site-recovery/hyper-v-azure-troubleshoot>
