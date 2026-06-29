# Implementation: Licensing

**Domain:** Governance
**Subdomain:** Licensing
**Incident Type:** Implementation

## Scenario / Query
How to set up Microsoft 365 E5 trial licenses for a pilot in an existing production tenant?

## Environment Context
- **Tenant Type:** existing production tenant
- **Configuration:** Microsoft 365 E5 trial licenses

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign in to your existing Microsoft 365 tenant administration portal.
2. Select Purchase Services from the navigation menu.
3. From the Office 365 section select Details under Office 365 E5 license.
4. Select Start free trial.
5. Confirm your request and select Try now.

## Validation
1. Sign in to the Microsoft 365 admin center (https://admin.microsoft.com).
2. Go to Billing > Purchase services and verify that 'Microsoft 365 E5 Trial' appears in the list of purchased services.
3. Go to Billing > Licenses and confirm that the trial license count is shown (e.g., 25 licenses).
4. Assign a trial license to a test user: In Users > Active users, select a user, go to Licenses and apps, expand 'Microsoft 365 E5 Trial', check the box, and save. Confirm the license is assigned successfully.
5. Verify the user can access Microsoft 365 E5 features (e.g., Microsoft Defender for Office 365, Microsoft 365 Defender portal) by signing in as that user.

## Rollback
1. Sign in to the Microsoft 365 admin center (https://admin.microsoft.com).
2. Go to Billing > Licenses, select the 'Microsoft 365 E5 Trial' license, and unassign all trial licenses from users.
3. Go to Billing > Purchase services, locate the 'Microsoft 365 E5 Trial' subscription, and select 'Cancel trial' (or 'Cancel subscription') to remove the trial.
4. Confirm cancellation when prompted.
5. Verify the trial no longer appears under Billing > Licenses and that users no longer have E5 trial licenses assigned.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/security/defender/eval-overview>
