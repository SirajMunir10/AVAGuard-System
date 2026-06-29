# Implementation: Endpoint Data Loss Prevention (DLP)

**Domain:** Purview
**Subdomain:** Endpoint Data Loss Prevention (DLP)
**Incident Type:** Implementation

## Scenario / Query
How to configure DLP policy to detect copying or moving protected files using unallowed Bluetooth apps?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Endpoint DLP settings, unallowed Bluetooth apps (Windows only, not supported for macOS)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the 'Copy or move using unallowed Bluetooth app' condition in DLP policy to detect when a protected file is copied or moved from an onboarded Windows device using an unallowed Bluetooth app.
2. For more information, see Unallowed Bluetooth apps.

## Validation
1. Verify that the DLP policy includes the condition 'Copy or move using unallowed Bluetooth app' by navigating to Microsoft Purview compliance portal > Data loss prevention > Policies, selecting the policy, and reviewing the rules. 2. On a test Windows device onboarded to Endpoint DLP, attempt to copy or move a protected file using a Bluetooth app that is not in the allowed list. 3. Confirm that the DLP policy triggers an alert or blocks the action as configured. 4. Check the DLP activity explorer for matching events.

## Rollback
1. In Microsoft Purview compliance portal > Data loss prevention > Policies, edit the policy and remove the condition 'Copy or move using unallowed Bluetooth app' from the rule. 2. Alternatively, disable the entire rule or policy if the condition is causing unintended blocks. 3. Verify that the change takes effect by repeating the test action and confirming no DLP alert or block occurs.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
