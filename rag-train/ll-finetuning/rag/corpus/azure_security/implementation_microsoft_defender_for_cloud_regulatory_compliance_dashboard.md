# Implementation: Microsoft Defender for Cloud - Regulatory Compliance Dashboard

**Domain:** Azure
**Subdomain:** Microsoft Defender for Cloud - Regulatory Compliance Dashboard
**Incident Type:** Implementation

## Scenario / Query
A customer enabled Microsoft Defender for Cloud on a new subscription but the Regulatory Compliance dashboard shows zero controls for Azure CIS 1.4.0. What is the most likely cause and how should it be resolved?

## Environment Context
- **Tenant Type:** Enterprise (EA)
- **Configuration:** Subscription has Microsoft Defender for Cloud (formerly Azure Security Center) enabled at the 'Standard' tier. No custom policies or initiatives have been assigned.

## Symptoms
- Regulatory Compliance dashboard displays 'No results' or '0 controls' for the Azure CIS 1.4.0 benchmark
- Security policy blade shows the built-in 'Azure CIS 1.4.0' initiative is not assigned to the subscription
- No compliance data is generated for the selected regulatory standard

## Error Codes
N/A

## Root Causes
1. The built-in regulatory compliance initiative (e.g., 'Azure CIS 1.4.0') is not assigned to the subscription or management group scope
2. The customer may have only enabled Defender for Cloud but did not assign the corresponding policy initiative for the desired compliance standard

## Remediation Steps
1. Navigate to Microsoft Defender for Cloud > Regulatory Compliance > 'Manage compliance policies'
2. Select the relevant scope (subscription or management group) and click 'Add standards'
3. Choose 'Azure CIS 1.4.0' from the list of available regulatory compliance standards and assign it
4. Wait up to 24 hours for the first compliance scan to complete and data to appear in the dashboard

## Validation
After assignment, the Regulatory Compliance dashboard should display the Azure CIS 1.4.0 controls with a compliance score (even if initially 0%).

## Rollback
Remove the assigned initiative from the scope via the same 'Manage compliance policies' interface by selecting the standard and clicking 'Remove'.

## References
- <https://learn.microsoft.com/en-us/azure/defender-for-cloud/update-regulatory-compliance-packages>
