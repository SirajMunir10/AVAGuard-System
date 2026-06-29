# Troubleshooting: Endpoint Security Policy

**Domain:** Intune
**Subdomain:** Endpoint Security Policy
**Incident Type:** Troubleshooting

## Scenario / Query
Why are configurations of the Antivirus permission ignored by Intune?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Antivirus granular permission for endpoint security policies

## Symptoms
- The granular permission of Antivirus for endpoint security policies might be temporarily visible in some Tenants.
- Configurations of the Antivirus permission are ignored by Intune.

## Error Codes
N/A

## Root Causes
1. This permission isn't released and isn't supported for use.

## Remediation Steps
1. Do not use the Antivirus granular permission for endpoint security policies as it is not supported.
2. When Antivirus becomes available to use as a granular permission, its availability will be announced in the What's new in Microsoft Intune article.

## Validation
1. Confirm that the Antivirus granular permission for endpoint security policies is not listed in the Microsoft Intune admin center under Tenant administration > Role permissions. 2. Verify that any role assignments using this permission do not affect Antivirus policy enforcement by checking that Antivirus policies are applied as expected via Endpoint security > Antivirus. 3. Review the 'What's new in Microsoft Intune' article (https://learn.microsoft.com/en-us/mem/intune/whats-new) to ensure no announcement has been made regarding the release of this permission.

## Rollback
1. If the remediation (removing use of the unsupported permission) causes unexpected access issues, reassign the affected roles using only supported permissions (e.g., 'Antivirus' under Endpoint security manager or Security baselines). 2. Restore any previously removed role assignments from backup or documentation. 3. Monitor the 'What's new in Microsoft Intune' article for official release of the Antivirus granular permission and re-enable it only after official announcement.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/endpoint-security-policy>
