# Implementation: Threat Analytics

**Domain:** Defender for Endpoint
**Subdomain:** Threat Analytics
**Incident Type:** Implementation

## Scenario / Query
How to set up custom detection rules and link them to Threat analytics reports in Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Custom detection rules

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Set up custom detection rules and link them to Threat analytics reports.
2. If these rules get triggered and an alert generates an incident, the report shows up in that incident and the incident appears under the Related incidents tab, just like any other Microsoft-defined detection.

## Validation
1. In Microsoft Defender XDR, navigate to Threat Analytics and select a report. 2. Under the report, click 'Create custom detection rule' and follow the wizard to define a rule based on the report's indicators. 3. After saving, go to 'Settings > Endpoints > Custom detection rules' and confirm the rule is listed with status 'Active'. 4. Simulate the rule's trigger (e.g., using a test file or command) and verify that an alert is generated. 5. Confirm the alert creates an incident, and in that incident, verify the 'Related incidents' tab shows the Threat Analytics report.

## Rollback
1. In Microsoft Defender XDR, go to 'Settings > Endpoints > Custom detection rules'. 2. Select the custom detection rule you created. 3. Click 'Turn off' to disable the rule, or click 'Delete' to remove it permanently. 4. If the rule was linked to a Threat Analytics report, the link is automatically removed when the rule is deleted. 5. Verify the rule no longer appears in the list and that no new alerts are generated from it.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/threat-analytics>
