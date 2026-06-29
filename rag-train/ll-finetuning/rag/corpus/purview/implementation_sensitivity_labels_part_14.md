# Implementation: Sensitivity Labels

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Implementation

## Scenario / Query
How do I configure external sharing and Conditional Access settings for labeled SharePoint sites?

## Environment Context
- **Tenant Type:** Microsoft 365 with SharePoint and Microsoft Entra Conditional Access
- **Configuration:** External sharing and Conditional Access settings must be selected

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select the option 'Control external sharing from labeled SharePoint sites'.
2. Choose one of the following: external sharing for anyone, new and existing guests, existing guests, or only people in your organization.
3. Select the option 'Use Microsoft Entra Conditional Access to protect labeled SharePoint sites' only if your organization has configured and is using Microsoft Entra Conditional Access.
4. Select one of the following settings: 'Determine whether users can access SharePoint sites from unmanaged devices' which uses the SharePoint feature that uses Microsoft Entra Conditional Access to block or limit access to SharePoint and OneDrive content from unmanaged devices.

## Validation
1. Verify that the sensitivity label policy includes the 'Control external sharing from labeled SharePoint sites' setting by running: Get-SPOTenant | Select-Object -ExpandProperty ExternalSharingPolicy. 2. Confirm the external sharing option selected (e.g., 'Anyone', 'NewAndExistingGuests', 'ExistingGuests', 'OnlyPeopleInYourOrganization') by checking the label configuration in the Microsoft Purview compliance portal: navigate to Information Protection > Sensitivity labels > [label name] > Site and group settings. 3. If 'Use Microsoft Entra Conditional Access to protect labeled SharePoint sites' was selected, validate that a corresponding Conditional Access policy exists in the Microsoft Entra admin center under Protection > Conditional Access, targeting the labeled SharePoint sites. 4. Verify the 'Determine whether users can access SharePoint sites from unmanaged devices' setting by running: Get-SPOTenant | Select-Object -ExpandProperty ConditionalAccessPolicy.

## Rollback
1. Remove the 'Control external sharing from labeled SharePoint sites' setting by editing the sensitivity label in the Microsoft Purview compliance portal and deselecting the option. 2. Reset the external sharing option to the previous value (e.g., 'ExistingGuests' or 'OnlyPeopleInYourOrganization') by modifying the label's site and group settings. 3. If 'Use Microsoft Entra Conditional Access to protect labeled SharePoint sites' was enabled, disable or delete the associated Conditional Access policy in the Microsoft Entra admin center under Protection > Conditional Access. 4. Revert the 'Determine whether users can access SharePoint sites from unmanaged devices' setting to its original state by running: Set-SPOTenant -ConditionalAccessPolicy <original_value>.

## References
- <https://learn.microsoft.com/en-us/purview/sensitivity-labels-teams-groups-sites>
