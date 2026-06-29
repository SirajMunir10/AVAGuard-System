# Implementation: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Implementation

## Scenario / Query
How to check that devices are compliant with the Microsoft Defender for Endpoint service using System Center 2012 R2 Configuration Manager?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** System Center 2012 R2 Configuration Manager

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Set a compliance rule for configuration item in System Center 2012 R2 Configuration Manager to monitor your deployment.
2. This rule should be a non-remediating compliance rule configuration item that monitors the value of a registry key on targeted devices.
3. Monitor the following registry key entry: Path: 'HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection\Status', Name: 'OnboardingState', Value: '1'.

## Validation
In the System Center 2012 R2 Configuration Manager console, navigate to 'Assets and Compliance' > 'Compliance Settings' > 'Configuration Items'. Select the configuration item created for the Defender for Endpoint compliance rule. On the 'Compliance Rules' tab, verify that a rule exists with the following settings: Rule type: 'Value', Setting: 'Registry key', Path: 'HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection\Status', Name: 'OnboardingState', Value: '1'. Then, initiate a compliance evaluation on a targeted device collection by right-clicking the configuration baseline containing this configuration item and selecting 'Evaluate'. After evaluation, check the compliance results for a device: open 'Monitoring' > 'Deployments', select the baseline deployment, and view the 'Compliance Statistics' to confirm the device shows 'Compliant'.

## Rollback
In the System Center 2012 R2 Configuration Manager console, navigate to 'Assets and Compliance' > 'Compliance Settings' > 'Configuration Items'. Locate the configuration item created for the Defender for Endpoint compliance rule. Right-click the configuration item and select 'Delete' to remove it. Alternatively, if you want to keep the configuration item but disable the rule, edit the configuration item, go to the 'Compliance Rules' tab, select the rule, and click 'Remove' to delete the rule. Then, redeploy the configuration baseline without the rule to affected device collections. If devices were already evaluated, no further action is needed as the rule is non-remediating.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-sccm>
