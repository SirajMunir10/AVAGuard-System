# Implementation: Multifactor Authentication

**Domain:** Entra ID
**Subdomain:** Multifactor Authentication
**Incident Type:** Implementation

## Scenario / Query
How to determine which Microsoft Entra ID license is required for specific MFA features?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** MFA licensing

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Plan out your needs for securing user authentication, then determine which approach meets those requirements.
2. Review the feature comparison table for the various versions of Microsoft Entra ID for multifactor authentication.

## Validation
1. Navigate to the Microsoft Entra admin center (https://entra.microsoft.com) and sign in with a Global Administrator account.
2. Go to Identity > Overview > Licenses > All products and verify the assigned licenses (e.g., Microsoft Entra ID P1, P2, or Microsoft 365 F1/E3/E5).
3. Under Identity > Users > All users, select a test user and click Licenses to confirm the user has the appropriate license assigned.
4. Review the feature comparison table at https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-licensing to ensure the desired MFA features (e.g., per-user MFA, Conditional Access MFA, risk-based MFA) are included in the licensed SKU.
5. Optionally, run the Microsoft Graph PowerShell command: Get-MgSubscribedSku | Select-Object SkuPartNumber, CapabilityStatus to list all licensed products and their status.

## Rollback
1. If incorrect licenses were assigned, remove the wrong license from users: In the Microsoft Entra admin center, go to Identity > Users > All users, select the affected user, click Licenses > Assignments, uncheck the incorrect license, and click Save.
2. Assign the correct license: Under the same user’s Licenses > Assignments, check the appropriate license (e.g., Microsoft Entra ID P1 or P2) and click Save.
3. If a license was purchased by mistake, cancel the subscription via the Microsoft 365 admin center (Billing > Your products) or contact your reseller.
4. Revert any Conditional Access policies that were modified: In the Microsoft Entra admin center, go to Protection > Conditional Access > Policies, select the changed policy, and restore its previous state using the policy’s version history or manual reconfiguration.
5. For per-user MFA settings, navigate to Identity > Users > Per-user MFA, select the user, and disable MFA if it was enabled incorrectly.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mfa-licensing>
