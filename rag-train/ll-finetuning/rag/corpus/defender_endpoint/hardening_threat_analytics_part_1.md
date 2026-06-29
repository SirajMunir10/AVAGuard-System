# Hardening: Threat Analytics

**Domain:** Defender for Endpoint
**Subdomain:** Threat Analytics
**Incident Type:** Hardening

## Scenario / Query
How to assess and mitigate threats using threat analytics reports in Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Threat analytics provides analysis of tracked threats and guidance on defense; incorporates network data to indicate active threats and applicable protections.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Identify and react to emerging threats.
2. Learn if you're currently under attack.
3. Assess the impact of the threat to your assets.
4. Review your resilience against or exposure to the threats.
5. Identify the mitigation, recovery, or prevention actions you can take to stop or contain the threats.

## Validation
1. Navigate to Microsoft Defender XDR portal (https://security.microsoft.com).
2. Go to Threat Analytics under the Endpoints section.
3. Confirm that the Threat Analytics dashboard displays the latest tracked threats with active alerts and incident counts.
4. Select a specific threat report and verify that the report includes:
   - Overview of the threat (description, date, source).
   - Active incidents and alerts related to the threat.
   - Impact assessment showing affected devices and users.
   - Recommended actions (mitigation, recovery, prevention).
5. Check that the 'Exposure level' and 'Resilience level' metrics are populated for your tenant.
6. Validate that any recommended actions (e.g., update policies, run antivirus scans) are actionable and link to relevant configuration pages.

## Rollback
1. If the Threat Analytics dashboard fails to load or shows incomplete data, verify that the user account has the required permissions (Security Reader, Security Administrator, or Global Reader).
2. Ensure that Microsoft Defender for Endpoint is properly provisioned and licensed for the tenant.
3. If a specific mitigation action (e.g., blocking an indicator) was applied and caused issues, remove the block by navigating to Settings > Endpoints > Indicators and deleting the relevant entry.
4. For policy changes recommended by Threat Analytics, revert to the previous policy version using the policy history in Microsoft Defender XDR.
5. If the issue persists, contact Microsoft Support with the tenant ID and a description of the problem.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/threat-analytics>
