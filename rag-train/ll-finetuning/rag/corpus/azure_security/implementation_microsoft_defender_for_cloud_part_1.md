# Implementation: Microsoft Defender for Cloud

**Domain:** Azure
**Subdomain:** Microsoft Defender for Cloud
**Incident Type:** Implementation

## Scenario / Query
A security operations team has enabled Microsoft Defender for Cloud on a new Azure subscription but cannot see any security alerts or recommendations for their virtual machines. What configuration step is missing?

## Environment Context
- **Tenant Type:** Enterprise (Azure AD tenant with multiple subscriptions)
- **Configuration:** Microsoft Defender for Cloud is enabled at the subscription level, but no Log Analytics workspace is configured for data collection.

## Symptoms
- No security alerts appear in Microsoft Defender for Cloud dashboard
- No security recommendations are generated for VMs
- The 'Data collection' status in Defender for Cloud shows 'Not configured'

## Error Codes
N/A

## Root Causes
1. Log Analytics agent (formerly Microsoft Monitoring Agent) is not installed on the VMs
2. No Log Analytics workspace is linked to the Defender for Cloud subscription for data ingestion

## Remediation Steps
1. In the Azure portal, navigate to Microsoft Defender for Cloud > Environment settings > select the subscription > Auto provisioning > enable 'Log Analytics agent for Azure VMs' and select an existing Log Analytics workspace or create a new one.
2. Alternatively, use the Azure CLI: az security auto-provisioning-setting update --name default --auto-provision On
3. After enabling, the agent will be automatically installed on existing and new VMs. Allow up to 24 hours for initial data collection and alert generation.

## Validation
Verify in Microsoft Defender for Cloud > Recommendations that recommendations such as 'Log Analytics agent should be installed on your machines' no longer appear, and that alerts are visible under 'Security alerts'.

## Rollback
Disable auto-provisioning in Defender for Cloud > Environment settings > Auto provisioning > set to 'Off'. Uninstall the Log Analytics agent from VMs if no longer needed.

## References
- Microsoft Learn: 'Quickstart: Set up Microsoft Defender for Cloud' - https://learn.microsoft.com/en-us/azure/defender-for-cloud/get-started
