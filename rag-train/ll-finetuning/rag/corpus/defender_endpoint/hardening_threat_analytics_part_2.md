# Hardening: Threat Analytics

**Domain:** Defender for Endpoint
**Subdomain:** Threat Analytics
**Incident Type:** Hardening

## Scenario / Query
How do I review my organization's resilience against a threat using the Recommended actions and Endpoints exposure charts in a Threat Analytics report?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Threat Analytics reports available in Microsoft 365 Defender portal

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Review the Recommended actions chart to see the Action status percentage or number of points achieved to improve security posture.
2. Perform the recommended actions to help address the threat.
3. View the breakdown of points by Category or Status.
4. Review the Endpoints exposure chart to see the number of vulnerable devices.
5. Apply security updates or patches to address vulnerabilities exploited by the threat.

## Validation
1. Navigate to Microsoft 365 Defender portal (https://security.microsoft.com).
2. Go to Threat Analytics under the Endpoints section.
3. Select the specific threat report of interest.
4. In the Recommended actions chart, verify that the Action status percentage or number of points achieved reflects the expected improvement after performing the recommended actions.
5. Confirm the breakdown of points by Category or Status shows the intended distribution.
6. In the Endpoints exposure chart, verify that the number of vulnerable devices has decreased as expected after applying security updates or patches.

## Rollback
1. If the Recommended actions chart shows an unexpected decrease in points or status, review the actions taken and revert any changes that may have caused the issue (e.g., disable a security policy that was enabled).
2. If the Endpoints exposure chart shows an increase in vulnerable devices, identify and uninstall any recently applied security updates or patches that may have caused compatibility issues or new vulnerabilities.
3. For any misconfigured settings, restore the previous configuration using the Microsoft 365 Defender portal or relevant management tools.
4. Monitor the Threat Analytics report for the affected threat to ensure the rollback actions have restored the original exposure levels.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/threat-analytics>
