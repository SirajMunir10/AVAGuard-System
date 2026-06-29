# Implementation: Identity Explorer

**Domain:** Defender for Endpoint
**Subdomain:** Identity Explorer
**Incident Type:** Implementation

## Scenario / Query
How to set up and use the Identity Explorer tab in Microsoft Defender XDR for investigating identity attack paths?

## Environment Context
- **Tenant Type:** Microsoft 365 with Microsoft Sentinel Data Lake license
- **Configuration:** Identity Explorer tab requires a Microsoft Sentinel Data Lake license

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure the tenant has a Microsoft Sentinel Data Lake license.
2. Navigate to the Identity Explorer tab in Microsoft Defender XDR.
3. Use the hunting graph to visualize identity attack paths and exposure scenarios as interactive graphs.
4. The graph is pre-seeded with the current identity to see how it relates to other entities.
5. Use the Identity Explorer to discover lateral movement paths, privilege escalation routes, and credential-access risks.

## Validation
1. Confirm the tenant has a Microsoft Sentinel Data Lake license by running: Get-MsolAccountSku | Where-Object {$_.AccountSkuId -like '*SENTINEL*'}. 2. Navigate to Microsoft Defender XDR > Identity Explorer tab. 3. Verify the hunting graph loads and displays interactive graphs showing identity attack paths. 4. Check that the current identity is pre-seeded in the graph. 5. Test discovery of lateral movement paths, privilege escalation routes, and credential-access risks by interacting with the graph.

## Rollback
1. If the Identity Explorer tab does not load, verify the Microsoft Sentinel Data Lake license is assigned to the tenant. 2. If the license is missing, acquire and assign it via the Microsoft 365 admin center. 3. If the graph fails to display, clear browser cache and retry. 4. If issues persist, contact Microsoft support for further assistance.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-users>
