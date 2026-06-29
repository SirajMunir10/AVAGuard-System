# Implementation: Microsoft Defender for Endpoint onboarding

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint onboarding
**Incident Type:** Implementation

## Scenario / Query
How to create a device collection in Microsoft Configuration Manager for onboarding Windows endpoints to Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Configuration Manager
- **Configuration:** Compliance settings within Configuration Manager console

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In the Microsoft Configuration Manager console, navigate to Assets and Compliance > Overview > Device Collections.
2. Select and hold (or right-click) Device Collection and select Create Device Collection.
3. Provide a Name and Limiting Collection, then select Next.
4. Select Add Rule and choose Query Rule.
5. Select Next on the Direct Membership Wizard and then select Edit Query Statement.
6. Select Criteria and then choose the star icon.
7. Keep criterion type as simple value, choose whereas Operating System - build number, operator as is greater than or equal to and value 14393, and select OK.
8. Select Next and Close.
9. Select Next.

## Validation
1. In the Configuration Manager console, go to Assets and Compliance > Overview > Device Collections. 2. Locate the newly created device collection. 3. Right-click the collection and select 'Show Members' to verify that the expected Windows endpoints (with OS build number >= 14393) appear. 4. Alternatively, run the following SQL query against the Configuration Manager database to confirm membership: SELECT * FROM v_Collection WHERE CollectionName = '<YourCollectionName>'; then check the corresponding collection members in v_FullCollectionMembership.

## Rollback
1. In the Configuration Manager console, navigate to Assets and Compliance > Overview > Device Collections. 2. Right-click the device collection you created and select 'Delete'. 3. Confirm the deletion when prompted. 4. If the collection was used in any compliance settings or client settings, reassign those settings to a different collection or revert to the previous configuration.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-sccm>
