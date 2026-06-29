# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to configure filter for devices as a condition in Conditional Access policies?

## Environment Context
- **Tenant Type:** Entra ID tenant with Conditional Access
- **Configuration:** Conditional Access policy configuration

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Configure filter for devices as a condition in Conditional Access policy
2. Include or exclude devices based on a filter using a rule expression on device properties
3. Author the rule expression for filter for devices using the rule builder or rule syntax
4. Use the rule expression similar to rules for dynamic membership groups

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Select the policy where the filter for devices was configured. 4. Under Assignments > Conditions > Filter for devices, confirm that the configured rule expression appears correctly and is enabled. 5. Use the What If tool (Protection > Conditional Access > What If) to simulate a sign-in from a device that matches the filter rule and verify that the policy applies as expected. 6. Simulate a sign-in from a device that does not match the filter rule and confirm the policy does not apply.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. Select the policy where the filter for devices was configured. 4. Under Assignments > Conditions > Filter for devices, either clear the rule expression to remove the filter, or set the filter to 'Not configured' to disable it. 5. If the entire policy needs to be disabled, set the policy state to 'Off'. 6. Save the changes. 7. Verify that the policy no longer applies by using the What If tool with test devices.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-conditions>
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-conditions#filter-for-devices>
