# Hardening: Microsoft Defender for Cloud - Secure Score

**Domain:** Azure
**Subdomain:** Microsoft Defender for Cloud - Secure Score
**Incident Type:** Hardening

## Scenario / Query
An organization wants to ensure that all Azure subscriptions have Microsoft Defender for Cloud's 'Auto-provisioning of the Log Analytics agent for Azure VMs' enabled to meet the CIS Benchmark recommendation. What steps should be taken to verify and remediate if it is not enabled?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Defender for Cloud - Auto-provisioning settings for Log Analytics agent

## Symptoms
- The secure score recommendation 'Auto-provisioning of the Log Analytics agent for Azure VMs' shows as 'Unhealthy' in Microsoft Defender for Cloud.
- New Azure VMs are not automatically configured with the Log Analytics agent.

## Error Codes
N/A

## Root Causes
1. Auto-provisioning of the Log Analytics agent is disabled at the subscription level in Microsoft Defender for Cloud.

## Remediation Steps
1. 1. Navigate to Microsoft Defender for Cloud > Environment settings > Select the relevant subscription.
2. 2. Under 'Auto provisioning', locate 'Log Analytics agent for Azure VMs' and set the status to 'On'.
3. 3. Optionally, select a custom workspace or keep the default workspace created by Defender for Cloud.
4. 4. Click 'Save' to apply the change. This will enable auto-provisioning for all existing and future VMs in the subscription.

## Validation
After enabling auto-provisioning, verify that the secure score recommendation 'Auto-provisioning of the Log Analytics agent for Azure VMs' changes to 'Healthy' within a few hours. Additionally, check that new VMs have the Log Analytics agent installed automatically.

## Rollback
To disable auto-provisioning, navigate to the same settings page and set the status to 'Off', then click 'Save'. Note that disabling does not remove the agent from already provisioned VMs.

## References
- CIS Microsoft Azure Foundations Benchmark v2.0.0, Recommendation 2.1
- Microsoft Learn: 'Enable auto-provisioning of the Log Analytics agent' - https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-auto-provisioning
