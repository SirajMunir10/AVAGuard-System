# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How does network share coverage and exclusions complement DLP On-premises repository actions?

## Environment Context
- **Tenant Type:** Purview
- **Configuration:** DLP On-premises repository actions

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Network share coverage and exclusions complements DLP On-premises repository actions.
2. DLP policies scoped to Devices are applied to all network shares and mapped drives that the device connects to. Supported actions: Devices.
3. Policies that are scoped to On-premises repositories can enforce protective actions on on-premises data-at-rest in file shares and SharePoint document libraries and folders.

## Validation
1. Confirm that DLP policies scoped to Devices are applied to network shares and mapped drives by running the following on a test device: Get-DlpConfiguration | Where-Object {$_.Scope -eq 'Device'} | Select-Object PolicyName, NetworkShareCoverage. 2. Verify that policies scoped to On-premises repositories enforce actions on file shares and SharePoint document libraries by checking the policy configuration in the Purview compliance portal: navigate to Data Loss Prevention > Policies, select the relevant policy, and confirm the 'Locations' include 'On-premises repositories' with specific file share paths. 3. Test a file in a network share that matches a DLP rule and confirm the expected action (e.g., block, audit) is triggered via the DLP alerts page.

## Rollback
1. If network share coverage causes unintended blocks, modify the DLP policy scoped to Devices to exclude specific network share paths: in the policy, under 'Locations', edit 'Devices' and add exclusions for the affected share paths. 2. If on-premises repository actions are too restrictive, adjust the policy scoped to On-premises repositories by reducing the action severity (e.g., change from 'Block' to 'Audit only') or removing specific file share locations from the policy scope. 3. To revert entirely, disable the DLP policy by setting its status to 'Disabled' in the Purview compliance portal.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
