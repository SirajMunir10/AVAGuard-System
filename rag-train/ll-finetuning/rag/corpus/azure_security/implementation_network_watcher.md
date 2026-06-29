# Implementation: Network Watcher

**Domain:** Azure
**Subdomain:** Network Watcher
**Incident Type:** Implementation

## Scenario / Query
How to run connectivity tests between Azure resources without installing any diagnostic agent or VM extension using the agentless experience in Network Watcher?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Network Watcher enabled in the region

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Initiate connectivity tests directly from the Azure portal without deploying or updating the Network Watcher agent VM extension on your Windows or Linux virtual machines.
2. All diagnostics are performed using Azure platform APIs.

## Validation
1. In the Azure portal, navigate to Network Watcher > Connectivity test (Preview).
2. Select a source virtual machine that does not have the Network Watcher agent VM extension installed.
3. Specify a destination (e.g., another VM, FQDN, or IP address) and configure protocol/ports.
4. Run the connectivity test and confirm that the test completes successfully without any agent-related errors.
5. Verify that the test results include latency, hop-by-hop path, and any connectivity failures, all sourced from Azure platform APIs.
6. Optionally, run the same test via Azure CLI: `az network watcher test-connectivity --resource-group <rg> --source-resource <vm-id> --dest-address <dest> --dest-port <port>` and confirm no agent installation prompts.

## Rollback
1. If the agentless connectivity test fails or produces unexpected results, revert to the classic agent-based connectivity test by installing the Network Watcher agent VM extension on the source VM:
   - For Windows: `az vm extension set --resource-group <rg> --vm-name <vm> --name NetworkWatcherAgentWindows --publisher Microsoft.Azure.NetworkWatcher`
   - For Linux: `az vm extension set --resource-group <rg> --vm-name <vm> --name NetworkWatcherAgentLinux --publisher Microsoft.Azure.NetworkWatcher`
2. After installation, run the connectivity test again using the same parameters to compare results.
3. If the agentless feature is no longer desired, disable the preview feature by removing any saved connectivity test configurations and reverting to the standard Network Watcher connectivity test workflow.

## References
- <https://learn.microsoft.com/en-us/azure/network-watcher/network-watcher-connectivity-overview>
