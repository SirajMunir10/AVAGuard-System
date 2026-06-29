# Hardening: Microsoft Defender for Cloud â€“ Secure Score

**Domain:** Azure
**Subdomain:** Microsoft Defender for Cloud â€“ Secure Score
**Incident Type:** Hardening

## Scenario / Query
A customer notices that their Azure Secure Score is lower than expected. They want to identify and remediate the specific security recommendations that are not being followed, especially those related to enabling Microsoft Defender for Cloud plans and configuring just-in-time (JIT) VM access.

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Microsoft Defender for Cloud is enabled but not all Defender plans are turned on; JIT VM access is not configured for any virtual machines.

## Symptoms
- Secure Score is below 80%
- Multiple high-severity recommendations appear in the Microsoft Defender for Cloud dashboard
- Recommendation 'Enable Microsoft Defender for Cloud plans on subscription' is listed as 'Unhealthy'
- Recommendation 'Management ports of virtual machines should be protected with just-in-time network access control' is listed as 'Unhealthy'

## Error Codes
N/A

## Root Causes
1. Not all Defender for Cloud plans are enabled on the subscription (e.g., Defender for Servers, Defender for SQL, etc.)
2. Just-in-time (JIT) VM access policy is not configured for any virtual machines in the subscription

## Remediation Steps
1. 1. In the Azure portal, navigate to Microsoft Defender for Cloud > Environment settings > Select the subscription > Defender plans. Enable all plans that are currently set to 'Off' (e.g., Defender for Servers, Defender for SQL, etc.) and select 'Save'.
2. 2. For JIT VM access: In Defender for Cloud, go to 'Workload protections' > 'Just-in-time VM access' > 'Not configured' tab. Select the VMs to protect and click 'Enable JIT on 1 VM' (or bulk enable). Configure the allowed source IP ranges and ports as needed, then save.

## Validation
After enabling all Defender plans, the Secure Score should increase. For JIT, verify that the recommendation 'Management ports of virtual machines should be protected with just-in-time network access control' changes to 'Healthy' in the Defender for Cloud dashboard.

## Rollback
To disable a Defender plan, navigate to the same Defender plans blade and toggle the plan to 'Off'. To disable JIT, go to the JIT VM access blade, select the VM, and click 'Disable'.

## References
- <https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction>
- <https://learn.microsoft.com/en-us/azure/defender-for-cloud/just-in-time-access-overview>
