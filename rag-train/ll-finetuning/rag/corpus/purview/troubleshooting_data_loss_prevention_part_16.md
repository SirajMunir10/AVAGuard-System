# Troubleshooting: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Troubleshooting

## Scenario / Query
How are DLP policy actions applied when an item matches multiple policies and one policy is in simulation mode?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** DLP policies: Policy ABC in Turn it on mode, Policy MNO in Run the policy in simulation mode

## Symptoms
- Item matches multiple DLP policies where one is in simulation mode
- Actions from simulation mode policy not applied

## Error Codes
N/A

## Root Causes
1. When an item matches multiple policies and one policy is in simulation mode, only actions from policies in Turn it on mode are applied

## Remediation Steps
1. Check the mode of each matching DLP policy
2. Only policies in 'Turn it on' mode will have their actions applied
3. Policies in 'Run the policy in simulation mode' will not enforce actions

## Validation
1. Identify the item that matched multiple DLP policies. 2. Run the DLP policy match report: https://compliance.microsoft.com/datalossprevention?viewid=dlpincidents. 3. For each matching policy, check its mode in the DLP policy list: https://compliance.microsoft.com/datalossprevention?viewid=policy. 4. Confirm that Policy ABC is set to 'Turn it on' and Policy MNO is set to 'Run the policy in simulation mode'. 5. Verify that only actions from Policy ABC (e.g., block, notify) were applied to the item, and no actions from Policy MNO were enforced.

## Rollback
1. If the remediation (i.e., confirming that only 'Turn it on' policies apply) is incorrect or causes issues, change the mode of the simulation policy to 'Turn it on' by editing Policy MNO in the DLP policy editor: https://compliance.microsoft.com/datalossprevention?viewid=policy. 2. Set Policy MNO mode to 'Turn it on' and save. 3. Wait for policy propagation (up to 1 hour). 4. Re-test the item to confirm that actions from both policies are now applied. 5. If the original behavior is desired, revert Policy MNO back to 'Run the policy in simulation mode'.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
