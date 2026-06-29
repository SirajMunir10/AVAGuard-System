# Troubleshooting: Endpoint onboarding

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint onboarding
**Incident Type:** Troubleshooting

## Scenario / Query
How to confirm a Microsoft Defender for Endpoint configuration package has been correctly deployed via Configuration Manager and troubleshoot failed deployments?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Configuration Manager console, Microsoft Defender for Endpoint onboarding package

## Symptoms
- Failed deployments with Error status
- Failed deployments with Requirements Not Met status
- Failed deployments with Failed status

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In the Configuration Manager console, click Monitoring at the bottom of the navigation pane.
2. Select Overview and then Deployments.
3. Select on the deployment with the package name.
4. Review the status indicators under Completion Statistics and Content Status.
5. If there are failed deployments (devices with Error, Requirements Not Met, or Failed statuses), troubleshoot the devices. For more information, see Troubleshoot Microsoft Defender for Endpoint onboarding issues.

## Validation
1. In the Configuration Manager console, navigate to Monitoring > Overview > Deployments. 2. Select the deployment containing the Microsoft Defender for Endpoint onboarding package. 3. Under Completion Statistics, verify that the 'Success' count matches the expected number of target devices and that no devices show 'Error', 'Requirements Not Met', or 'Failed' status. 4. Under Content Status, confirm that all distribution points show 'Success' for content distribution. 5. On a sample target device, open the Configuration Manager client control panel (Configuration Manager Properties) and check the 'Components' tab to ensure 'Microsoft Defender for Endpoint Onboarding' is listed and active.

## Rollback
1. In the Configuration Manager console, navigate to Software Library > Application Management > Packages. 2. Locate the Microsoft Defender for Endpoint onboarding package, right-click it, and select 'Distribute Content' > 'Remove' to remove the package from distribution points. 3. Delete the deployment by right-clicking the deployment in Monitoring > Overview > Deployments and selecting 'Delete'. 4. On affected devices, run the command 'C:\Program Files\Microsoft Defender for Endpoint\OnboardingScript.cmd /uninstall' (if the onboarding script supports uninstall) or manually remove the onboarding registry keys under 'HKLM\SOFTWARE\Microsoft\Windows Advanced Threat Protection\Status' and delete the service 'Sense' using 'sc delete Sense' (requires administrative privileges). 5. Restart the device to complete the rollback.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-sccm>
