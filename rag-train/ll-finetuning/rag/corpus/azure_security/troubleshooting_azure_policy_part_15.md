# Troubleshooting: Azure Policy

**Domain:** Azure
**Subdomain:** Azure Policy
**Incident Type:** Troubleshooting

## Scenario / Query
The regex I provided in my policy assignment isn't matching the resources I expected it to match

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Regex pattern in policy assignment does not match expected resources

## Error Codes
N/A

## Root Causes
1. The regex.match function in rego uses RE2, which is not the default flavor served by many online regex matchers

## Remediation Steps
1. Select the RE2 or golang flavor of regex in your online matcher when testing regex patterns
2. See the rego docs for more details on the RE2 flavor and what online tooling is recommended to test your regex

## Validation
1. Identify the policy assignment that uses the regex pattern. Run: az policy assignment list --query "[?contains(properties.displayName, '<policy-name>')].{Name:name, Scope:scope}" --output table
2. Retrieve the policy definition to confirm the regex pattern. Run: az policy definition show --name <policy-definition-name> --query "properties.policyRule.then.details"
3. Test the regex pattern using an RE2-compatible online tool (e.g., https://regex101.com with the Go (RE2) flavor selected) against a sample resource name or ID that should match.
4. Verify that the expected resources now appear in the policy compliance state. Run: az policy state list --resource <resource-id> --query "[?policyAssignmentName=='<assignment-name>'].{ResourceId:resourceId, ComplianceState:complianceState}"

## Rollback
1. If the regex pattern change causes unintended matching, revert to the original regex pattern in the policy definition. Run: az policy definition update --name <policy-definition-name> --rules <path-to-original-rules-json>
2. If the policy assignment was modified, revert to the original assignment parameters. Run: az policy assignment update --name <assignment-name> --params <path-to-original-params-json>
3. Wait for the next policy evaluation cycle (typically 30 minutes) or trigger an on-demand evaluation. Run: az policy state trigger-scan --resource-group <resource-group-name>
4. Confirm that the compliance state returns to the previous state. Run: az policy state list --resource <resource-id> --query "[?policyAssignmentName=='<assignment-name>'].{ResourceId:resourceId, ComplianceState:complianceState}"

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/troubleshoot/general>
