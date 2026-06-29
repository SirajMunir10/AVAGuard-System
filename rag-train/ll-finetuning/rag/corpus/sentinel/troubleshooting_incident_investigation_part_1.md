# Troubleshooting: Incident Investigation

**Domain:** Sentinel
**Subdomain:** Incident Investigation
**Incident Type:** Troubleshooting

## Scenario / Query
How do I investigate incidents in Microsoft Sentinel using the legacy incident investigation experience?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel in the Azure portal, legacy incident investigation experience

## Symptoms
- Access to this page requires authorization
- You can try signing in or changing directories

## Error Codes
N/A

## Root Causes
1. User may not have proper authorization to access the page
2. User may need to sign in or change directories

## Remediation Steps
1. Sign in to the Azure portal with appropriate credentials
2. Change directories if necessary to access the correct tenant

## Validation
1. Open a new browser session and navigate to https://portal.azure.com. 2. Sign in with the user account that has the Microsoft Sentinel Reader, Microsoft Sentinel Responder, or Microsoft Sentinel Contributor role assigned at the subscription or resource group level. 3. In the Azure portal, search for and select 'Microsoft Sentinel'. 4. Select the appropriate Sentinel workspace. 5. Under 'Threat management', click 'Incidents'. 6. Click on an incident to open its details. 7. In the incident details pane, click 'View full details' to open the legacy investigation experience. 8. Verify that the investigation graph, entities, and timeline are displayed without any authorization errors.

## Rollback
1. If the user still sees 'Access to this page requires authorization' or 'You can try signing in or changing directories', verify the user's role assignments: a. In the Azure portal, navigate to the Microsoft Sentinel workspace. b. Under 'Settings', select 'Access control (IAM)'. c. Click 'View access for this resource' and confirm the user has at least Microsoft Sentinel Reader role. 2. If the user lacks the required role, assign the appropriate role: a. In the IAM blade, click 'Add' > 'Add role assignment'. b. Select a role such as 'Microsoft Sentinel Reader' and assign it to the user. 3. If the user is in the wrong directory, instruct them to click the directory + subscription filter in the Azure portal top bar and switch to the correct tenant containing the Sentinel workspace. 4. If the issue persists, clear the browser cache and cookies, then retry the sign-in process.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/investigate-cases>
