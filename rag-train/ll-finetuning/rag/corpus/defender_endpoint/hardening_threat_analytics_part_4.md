# Hardening: Threat Analytics

**Domain:** Defender for Endpoint
**Subdomain:** Threat Analytics
**Incident Type:** Hardening

## Scenario / Query
How to review and implement recommended mitigations from a threat analytics report to increase organizational resilience?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Threat Analytics recommended actions tab

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Review list of mitigations and the status of your devices in the Recommended actions tab.
2. Review the list of specific actionable recommendations that can help you increase your organizational resilience against the threat.
3. Review the list of tracked mitigations including supported security configurations such as: Cloud-delivered protection, Potentially unwanted application (PUA) protection, Real-time protection.

## Validation
1. Navigate to Microsoft 365 Defender portal (https://security.microsoft.com).
2. Go to Threat Analytics under the Endpoints section.
3. Select the specific threat analytics report relevant to the incident.
4. Click on the 'Recommended actions' tab.
5. Verify that the list of mitigations is displayed, including their status (e.g., 'Completed', 'In progress', 'Not started').
6. Confirm that the specific actionable recommendations are visible and match the expected security configurations (e.g., Cloud-delivered protection, PUA protection, Real-time protection).
7. Check that the status of each mitigation reflects the intended state after remediation (e.g., all devices show 'Completed' for the applied configurations).

## Rollback
1. Navigate to Microsoft 365 Defender portal (https://security.microsoft.com).
2. Go to Threat Analytics under the Endpoints section.
3. Select the same threat analytics report.
4. Click on the 'Recommended actions' tab.
5. For each mitigation that was applied as part of the remediation, revert the configuration to its previous state (e.g., disable Cloud-delivered protection, disable PUA protection, disable Real-time protection) using the appropriate security policy or device configuration method (e.g., Intune, Group Policy, or Defender for Endpoint settings).
6. After reverting, refresh the 'Recommended actions' tab to confirm that the status of each mitigation returns to its original state (e.g., 'Not started' or 'In progress').
7. If the rollback involves multiple devices, verify that the changes propagate and the status updates accordingly.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/threat-analytics>
