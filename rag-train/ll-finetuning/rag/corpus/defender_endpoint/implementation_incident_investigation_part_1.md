# Implementation: Incident Investigation

**Domain:** Defender for Endpoint
**Subdomain:** Incident Investigation
**Incident Type:** Implementation

## Scenario / Query
How do I use Microsoft Security Copilot during incident investigation in Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR with Security Copilot provisioned access
- **Configuration:** N/A

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. When users with provisioned access to Microsoft Security Copilot open an incident, they see the Copilot pane on the right side of the screen.
2. Copilot provides real-time insights and recommendations to help investigate and respond to incidents.

## Validation
1. Open the Microsoft Defender portal (https://security.microsoft.com).
2. Navigate to Incidents & alerts > Incidents.
3. Select any incident to open its details page.
4. Verify that the Copilot pane is visible on the right side of the screen. If not, click the Copilot icon in the top-right toolbar to open it.
5. In the Copilot pane, confirm that real-time insights and recommendations are displayed, such as incident summary, related alerts, device details, and suggested actions.
6. Optionally, ask a natural language question in the Copilot chat box (e.g., 'What is the top recommended action?') and verify that a relevant response is returned.

## Rollback
1. If the Copilot pane does not appear or shows errors, verify that the user has been assigned the required Security Copilot license and role (e.g., Security Copilot Contributor or Security Copilot Reader).
2. Ensure that the Microsoft Security Copilot service is enabled in the tenant by checking the Copilot settings in the Microsoft 365 admin center or Defender portal.
3. If the issue persists, contact Microsoft support to confirm provisioning status and troubleshoot any service health issues.
4. As a last resort, disable and re-enable Security Copilot for the affected user(s) via the Microsoft 365 admin center > Users > Active users > select user > Licenses and apps > uncheck and recheck Security Copilot.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-incidents>
