# Implementation: Security Baselines

**Domain:** Intune
**Subdomain:** Security Baselines
**Incident Type:** Implementation

## Scenario / Query
How do I find details about using or configuring settings available in a security baseline in Intune?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Security baseline policy

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Review the Intune security baseline policy UI for information text taken from the source CSP.
2. Follow the link provided in the UI to the CSP documentation for details on how to configure each option.
3. Consult the Intune documentation for the list of settings in each security baseline version and its default configuration.

## Validation
1. In the Microsoft Intune admin center, navigate to Endpoint security > Security baselines and select the baseline you deployed. 2. For each policy, review the 'Settings' tab and confirm that the information text for each setting matches the corresponding CSP documentation. 3. Click the 'Learn more' link next to a setting and verify it opens the correct CSP documentation page. 4. Cross-reference the list of settings and default configurations with the official Intune documentation at https://learn.microsoft.com/en-us/mem/intune/protect/security-baselines.

## Rollback
1. In the Microsoft Intune admin center, go to Endpoint security > Security baselines. 2. Select the baseline policy that was modified. 3. Click 'Properties' and then 'Settings' to review the current configuration. 4. If the changes caused issues, edit the policy and revert each setting to its previous value or to the default configuration as documented in the official Intune documentation. 5. Alternatively, delete the policy and re-create it using the default baseline template. 6. Monitor affected devices for policy reapplication and compliance status.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/security-baselines>
