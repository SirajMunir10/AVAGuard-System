# Implementation: Advanced Hunting

**Domain:** Defender for Endpoint
**Subdomain:** Advanced Hunting
**Incident Type:** Implementation

## Scenario / Query
How can I use advanced hunting queries to build custom detection rules?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Advanced hunting supports queries that check data from Microsoft Defender for Endpoint, Office 365, Cloud Apps, Identity, and Sentinel.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the same threat hunting queries to build custom detection rules.
2. These rules run automatically to check for and then respond to suspected breach activity, misconfigured machines, and other findings.

## Validation
1. In Microsoft Defender XDR, navigate to Advanced Hunting and run the custom detection query you created. Confirm that the query returns expected results based on your threat hunting logic. 2. Go to Custom detection rules, locate the rule built from the query, and verify its status is 'Active'. 3. Trigger a test event that matches the rule's conditions and confirm that an alert is generated and the configured response action (e.g., isolation, email notification) executes as expected.

## Rollback
1. In Microsoft Defender XDR, go to Custom detection rules and select the rule you created. 2. Click 'Turn off' to disable the rule, preventing further automatic checks and responses. 3. If the rule was created from a saved query, delete the custom detection rule entirely. 4. Optionally, delete the underlying saved query from Advanced Hunting if it is no longer needed.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview>
