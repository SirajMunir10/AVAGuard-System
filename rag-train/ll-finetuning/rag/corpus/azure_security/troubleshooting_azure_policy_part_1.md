# Troubleshooting: Azure Policy (The policy definition '{0}' targets multiple resource types, but the policy rule is authored in a way that makes the policy not applicable to the target resource types '{1}'.)

**Domain:** Azure
**Subdomain:** Azure Policy
**Incident Type:** Troubleshooting

## Scenario / Query
A policy definition that includes multiple resource types fails validation during creation or update with an error about targeting multiple resource types.

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Policy definition fails validation during creation or update

## Error Codes
- `The policy definition '{0}' targets multiple resource types, but the policy rule is authored in a way that makes the policy not applicable to the target resource types '{1}'.`

## Root Causes
1. The policy definition rule has one or more conditions that don't get evaluated by the target resource types.
2. An alias is used without a type condition to ensure it gets evaluated against only the resource type it belongs to.

## Remediation Steps
1. If an alias is used, make sure that the alias gets evaluated against only the resource type it belongs to by adding a type condition before it.
2. Alternatively, split the policy definition into multiple definitions to avoid targeting multiple resource types.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/governance/policy/troubleshoot/general>
