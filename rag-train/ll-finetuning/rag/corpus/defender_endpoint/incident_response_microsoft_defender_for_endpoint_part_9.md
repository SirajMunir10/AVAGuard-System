# Incident Response: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Incident Response

## Scenario / Query
How to consult a Microsoft threat expert for insights regarding a potentially compromised or already compromised device?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Microsoft Threat Experts enabled in Defender portal

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Engage Microsoft Threat Experts directly from within the Defender portal for timely and accurate response.
2. Experts provide insights regarding a potentially compromised device, complex threats, targeted attack notifications, or threat intelligence context on the portal dashboard.

## Validation
1. In the Microsoft Defender portal (https://security.microsoft.com), navigate to Incidents & alerts > Incidents. Select the relevant incident. 2. On the incident page, verify that the 'Ask Threat Experts' button is visible and active. 3. Click 'Ask Threat Experts' and confirm the dialog opens with options to 'Ask a question' or 'Request targeted attack notification'. 4. Submit a test question (e.g., 'Is this device compromised?') and verify that the response is received in the portal within the expected timeframe (typically within 30 minutes). 5. Check the incident timeline for an entry indicating the expert consultation was initiated and completed.

## Rollback
1. If the 'Ask Threat Experts' button is missing or inactive, ensure the Microsoft Threat Experts service is enabled in the Defender portal: navigate to Settings > Endpoints > General > Advanced features and verify 'Microsoft Threat Experts' is toggled On. 2. If the service is enabled but the button remains unavailable, verify that the user has the required permissions (e.g., Security Administrator or Security Operator role). 3. If the expert response contains incorrect or misleading information, contact Microsoft Support to report the issue and request a review. 4. If the consultation causes unintended actions (e.g., automated response triggered), manually revert those actions using the device's action center in the Defender portal.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
