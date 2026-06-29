# Troubleshooting: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Troubleshooting

## Scenario / Query
How does the mode of a DLP policy affect which actions are applied when an item matches multiple policies?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policies in different modes (enforce vs simulation)

## Symptoms
- Item matches multiple policies but actions from simulation mode policies are not applied as expected

## Error Codes
N/A

## Root Causes
1. When policies have identical actions, actions from policies in 'Turn it on' state (enforce mode) are applied preferentially over policies in simulation modes
2. Policies in 'Run the policy in simulation mode' state apply different actions than they would in 'Turn it on right away' state

## Remediation Steps
1. Check the mode of each matching policy: 'Turn it on right away', 'Run the policy in simulation mode with policy tips', or 'Run the policy in simulation mode'
2. Ensure that policies in enforce mode have the desired actions applied first
3. If simulation mode is needed, verify that the actions applied in simulation are appropriate for testing

## Validation
Review DLP reports to confirm which policy's actions were applied based on mode

## Rollback
Change policy mode from simulation to enforce or vice versa as needed

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
