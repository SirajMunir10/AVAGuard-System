# Troubleshooting: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Troubleshooting

## Scenario / Query
How does the What If evaluation API differ from the legacy What If experience in Conditional Access?

## Environment Context
- **Tenant Type:** Entra ID tenant with Conditional Access policies
- **Configuration:** Conditional Access policies with specific conditions

## Symptoms
- What If evaluation does not match expected policy results
- Groups of apps like Office 365 or Microsoft Admin Portals do not result in a match

## Error Codes
N/A

## Root Causes
1. The What If API expects all sign-in parameters to be defined for accurate evaluation
2. If sign-in details for specific conditions are not provided, the API cannot evaluate those conditions
3. Groups of apps are not supported; only individual App IDs are matched

## Remediation Steps
1. Use the What If API through the Conditional Access experience or Microsoft Graph API
2. Provide all required sign-in parameters, including the App ID for application specification
3. Ensure that policies with specific conditions have corresponding sign-in details defined

## Validation
1. Open the Conditional Access What If tool in the Azure portal (Entra ID > Conditional Access > What If).
2. Set the user, cloud apps (using individual App IDs, not app groups), and any other sign-in parameters (IP location, device platform, client app, sign-in risk, etc.) exactly as expected for the policy.
3. Click 'What If' and verify that the policy evaluation result matches the expected outcome (e.g., policy applied or not applied).
4. Alternatively, use the Microsoft Graph API to call the `evaluate` endpoint with the same parameters and confirm the response matches the portal result.
5. If the policy includes conditions like location or device state, ensure those parameters are provided in the What If evaluation; otherwise, the condition will not be evaluated.

## Rollback
1. If the What If evaluation still does not match expected results, revert to using the legacy What If experience by ensuring you are not using the new API endpoint (i.e., use the portal's built-in What If tool without custom API calls).
2. Remove any custom App IDs that were added for testing and restore the original policy configuration.
3. If the issue persists, review the policy conditions and sign-in parameters to ensure they are correctly defined and match the intended scenario.
4. If necessary, disable and re-enable the Conditional Access policy to reset its state, then re-run the What If evaluation with the correct parameters.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access-what-if>
