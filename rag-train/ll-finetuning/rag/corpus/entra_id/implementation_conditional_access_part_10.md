# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to review report-only results for a Conditional Access policy before enabling it?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Conditional Access policy with report-only mode

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Wait 24 hours for sign-in data to accumulate.
2. In the Microsoft Entra admin center, go to Identity > Monitoring & health > Sign-in logs.
3. Filter by your policy name and review the Report-only column.
4. Confirm that only expected devices and users show as noncompliant.
5. If the scope looks correct, return to Conditional Access > Policies, select your policy, and change Enable policy to On.

## Validation
1. In the Microsoft Entra admin center, navigate to Identity > Monitoring & health > Sign-in logs. 2. Apply a filter for the policy name used in report-only mode. 3. Verify that the 'Report-only' column displays results for sign-ins over the past 24 hours. 4. Confirm that only expected devices and users are marked as noncompliant. 5. If the scope appears correct, proceed to enable the policy.

## Rollback
1. In the Microsoft Entra admin center, go to Identity > Protection > Conditional Access > Policies. 2. Locate the policy that was enabled. 3. Select the policy and change 'Enable policy' from 'On' back to 'Report-only'. 4. Save the change. 5. Monitor sign-in logs to confirm the policy is no longer enforced.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
