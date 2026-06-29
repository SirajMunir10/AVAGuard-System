# Implementation: Advanced Hunting

**Domain:** Defender for Endpoint
**Subdomain:** Advanced Hunting
**Incident Type:** Implementation

## Scenario / Query
How do I choose between guided and advanced modes for hunting in the Microsoft Defender portal?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Guided mode is for users not familiar with KQL; advanced mode is for users comfortable with KQL.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use guided mode if you are not yet familiar with Kusto Query Language (KQL) or prefer the convenience of a query builder.
2. Use advanced mode if you are comfortable using KQL to create queries from scratch.

## Validation
1. Open the Microsoft Defender portal (https://security.microsoft.com).
2. Navigate to **Hunting** > **Advanced hunting**.
3. Verify that the **Guided mode** toggle is available and can be switched on/off.
4. In guided mode, confirm that the query builder interface appears with dropdowns for selecting tables, fields, and operators.
5. In advanced mode, confirm that a blank KQL editor is displayed and you can type a query such as `DeviceInfo | take 10` and run it successfully.
6. Ensure that switching between modes does not cause any errors or loss of previously saved queries.

## Rollback
1. If guided mode is not working as expected, switch back to advanced mode by toggling the **Guided mode** switch to off.
2. If advanced mode is not working, switch to guided mode by toggling the switch on.
3. If the toggle is missing or the interface is broken, clear your browser cache and cookies, then reload the portal.
4. If the issue persists, use a different browser or an InPrivate/Incognito session to access the portal.
5. If none of the above resolves the issue, contact Microsoft support with the tenant ID and a description of the problem.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview>
