# Hardening: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Hardening

## Scenario / Query
How to exclude Universal Store Service APIs and Web Application (AppID 45a330b1-b1ec-4cc1-9161-9f03992aa49f) from Conditional Access policies to prevent Subscription Activation issues when stepping up from one version of Windows to another?

## Environment Context
- **Tenant Type:** Any
- **Configuration:** Conditional Access policies controlling access, Subscription Activation feature enabled

## Symptoms
- Device might not reactivate automatically when offline for an extended period of time
- Subscription Activation does not work seamlessly

## Error Codes
N/A

## Root Causes
1. Conditional Access policy blocks the Universal Store Service APIs and Web Application (AppID 45a330b1-b1ec-4cc1-9161-9f03992aa49f) needed for Subscription Activation

## Remediation Steps
1. Exclude one of the following cloud apps from Conditional Access policies using Select Excluded Cloud Apps: Universal Store Service APIs and Web Application, AppID 45a330b1-b1ec-4cc1-9161-9f03992aa49f
2. Alternatively, exclude Windows Store for Business, AppID 45a330b1-b1ec-4cc1-9161-9f03992aa49f (note: the app ID is the same, but the name depends on the tenant)

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. For each Conditional Access policy that targets cloud apps, select the policy, then under Assignments > Cloud apps or actions > Exclude, confirm that 'Universal Store Service APIs and Web Application' (or 'Windows Store for Business') is listed. 4. Verify that the App ID 45a330b1-b1ec-4cc1-9161-9f03992aa49f is associated with the excluded app. 5. On a test device that previously experienced Subscription Activation issues, trigger a subscription activation step-up (e.g., upgrade from Windows Pro to Enterprise) and confirm that activation completes without a Conditional Access block.

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator. 2. Navigate to Protection > Conditional Access > Policies. 3. For each policy where the exclusion was added, select the policy, then under Assignments > Cloud apps or actions > Exclude, remove 'Universal Store Service APIs and Web Application' (or 'Windows Store for Business') from the excluded list. 4. Save the policy changes. 5. On a test device, verify that the previous Subscription Activation behavior (e.g., failure to activate when offline) returns, confirming the rollback is effective.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-policy-compliant-device>
