# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
What are the restrictions on using multiple printer parameters in Microsoft Purview Endpoint DLP settings?

## Environment Context
- **Tenant Type:** Microsoft 365 E5/A5/G5
- **Configuration:** Endpoint DLP policy with printer restriction

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. You shouldn't use multiple parameters of USB printer, IP range, Print to file, Universal print deployed on a printer, Corporate printer, and Print to local.
2. Assign each printer in the group a Display name. These names appear only in the Microsoft Purview console.

## Validation
1. Navigate to Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings > Printer restrictions. 2. Verify that no more than one of the following parameters is configured in a single rule: USB printer, IP range, Print to file, Universal print deployed on a printer, Corporate printer, Print to local. 3. Confirm each printer group has a unique Display name assigned. 4. Run a test print from an endpoint to ensure the intended printer restriction is enforced and no unintended blocks occur.

## Rollback
1. In Microsoft Purview compliance portal > Data Loss Prevention > Endpoint DLP settings > Printer restrictions, remove any conflicting printer parameters so that only one parameter type remains per rule. 2. If multiple printer groups were created, delete the groups that are not needed. 3. Revert any Display name changes to original values if necessary. 4. Test printing again to confirm restrictions are removed or corrected.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
