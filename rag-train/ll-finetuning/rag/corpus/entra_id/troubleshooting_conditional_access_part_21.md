# Troubleshooting: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Troubleshooting

## Scenario / Query
Why does Conditional Access policy requiring Microsoft Power BI as approved client app fail when using Microsoft Entra application proxy to connect Power BI mobile app to on-premises Power BI Report Server?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with Conditional Access policy requiring approved client app for Power BI
- **Configuration:** Policy uses 'Require approved client app' grant with Microsoft Power BI

## Symptoms
- Conditional Access policy fails when Power BI mobile app connects to on-premises Power BI Report Server via Microsoft Entra application proxy

## Error Codes
N/A

## Root Causes
1. Conditional Access policies that require Microsoft Power BI as an approved client app do not support using Microsoft Entra application proxy to connect the Power BI mobile app to the on-premises Power BI Report Server

## Remediation Steps
1. Do not use Microsoft Entra application proxy for Power BI mobile app connections to on-premises Power BI Report Server when 'Require approved client app' policy is applied
2. Consider alternative connectivity methods or adjust Conditional Access policy

## Validation
1. Confirm the Conditional Access policy is still active: Sign in to the Microsoft Entra admin center, navigate to Protection > Conditional Access > Policies, and verify the policy requiring approved client app for Power BI is enabled. 2. Test connectivity: From a Power BI mobile app, attempt to connect to the on-premises Power BI Report Server via Microsoft Entra application proxy. 3. Verify failure: Observe that the connection fails with an access denied or policy violation message. 4. Check sign-in logs: In the Microsoft Entra admin center, go to Monitoring > Sign-in logs, filter by the user and application (Power BI), and confirm the Conditional Access policy evaluation shows 'Failure' due to the approved client app requirement not being met.

## Rollback
1. Disable or modify the Conditional Access policy: In the Microsoft Entra admin center, navigate to Protection > Conditional Access > Policies, select the policy requiring approved client app for Power BI, and either set 'Enable policy' to 'Off' or remove the 'Require approved client app' grant control. 2. Test connectivity again: From the Power BI mobile app, attempt to connect to the on-premises Power BI Report Server via Microsoft Entra application proxy. 3. Verify success: Confirm the connection succeeds without policy errors. 4. If needed, re-enable the policy with adjusted conditions (e.g., exclude the application proxy scenario) or use an alternative connectivity method as documented.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant>
