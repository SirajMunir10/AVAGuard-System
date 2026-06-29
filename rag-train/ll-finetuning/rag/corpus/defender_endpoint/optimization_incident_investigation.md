# Optimization: Incident Investigation

**Domain:** Defender for Endpoint
**Subdomain:** Incident Investigation
**Incident Type:** Optimization

## Scenario / Query
How can IT administrators use blast radius analysis to prioritize vulnerabilities?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Blast radius analysis enabled, critical assets defined

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use blast radius analysis to mobilize resources based on business impact and potential damage estimation.
2. Prioritize the most critical vulnerabilities that require immediate attention.
3. Proactively allocate required resources based on the blast radius reach to critical targets by examining multiple nodes marked with vulnerabilities on the map.

## Validation
1. In Microsoft Defender XDR, navigate to Incidents & alerts > Incidents. Select an incident and review the 'Attack story' tab. Confirm that the blast radius analysis map displays nodes marked with vulnerabilities and highlights critical assets. 2. Verify that the blast radius analysis shows the potential impact and reach of vulnerabilities to critical targets. 3. Check that the incident priority and resource allocation recommendations align with the blast radius assessment.

## Rollback
1. If blast radius analysis is not functioning as expected, ensure that 'Blast radius analysis' is enabled in the Microsoft Defender XDR settings under 'Permissions > Roles > Advanced features'. 2. Verify that critical assets are correctly defined in 'Assets > Critical asset rules'. 3. If the map does not display correctly, clear the browser cache or use an InPrivate/Incognito session to reload the incident. 4. If issues persist, contact Microsoft Support for further assistance.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-incidents>
