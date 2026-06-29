# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How do I configure Conditional Access policy conditions for sign-in risk, device platforms, locations, client apps, and filter for devices?

## Environment Context
- **Tenant Type:** Entra ID tenant with Conditional Access licensing
- **Configuration:** Conditional Access policy conditions

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign in to the Microsoft Entra admin center as at least a Conditional Access Administrator.
2. Browse to Protection > Conditional Access > Policies.
3. Select a policy and select Conditions.
4. Configure sign-in risk: Select User risk levels (High, Medium, Low, No risk) or Sign-in risk levels (High, Medium, Low, No risk).
5. Configure device platforms: Select any, none, or specific platforms (Android, iOS, Windows Phone, Windows, macOS, Linux).
6. Configure locations: Select any location, all trusted locations, or all untrusted locations, or specific named locations.
7. Configure client apps: Select Browser, Mobile apps and desktop clients, Exchange ActiveSync clients, or Other clients.
8. Configure filter for devices: Use rule syntax to include or exclude devices based on attributes like device model, manufacturer, or operating system version.

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Select the policy that was configured. 4. Under Conditions, verify that the sign-in risk settings (User risk levels and Sign-in risk levels) match the intended configuration. 5. Confirm that the device platforms selected (e.g., Android, iOS, Windows) are correct. 6. Check that the locations (any, trusted, untrusted, or named locations) are set as expected. 7. Validate the client apps configuration (Browser, Mobile apps and desktop clients, Exchange ActiveSync clients, Other clients). 8. Review the filter for devices rule syntax to ensure it correctly includes or excludes devices based on attributes like device model, manufacturer, or operating system version. 9. Optionally, use the 'What If' tool to test the policy against a sample user, sign-in risk, device platform, location, client app, and device filter to confirm the policy applies as intended.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Select the policy that was modified. 4. Under Conditions, revert each condition to its previous state: a. For sign-in risk, set User risk levels and Sign-in risk levels back to the original selection. b. For device platforms, restore the previous platform selection. c. For locations, select the original location configuration (any, trusted, untrusted, or specific named locations). d. For client apps, re-select the original client app types. e. For filter for devices, remove or adjust the rule syntax to match the prior filter criteria. 5. Save the policy. 6. If the policy was newly created and causes issues, delete the policy entirely. 7. Monitor sign-in logs to confirm that the rollback has restored previous behavior.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-conditions>
