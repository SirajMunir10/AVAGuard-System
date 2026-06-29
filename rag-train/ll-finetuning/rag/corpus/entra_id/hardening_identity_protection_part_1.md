# Hardening: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Hardening

## Scenario / Query
How to investigate identity risks in Microsoft Entra ID Protection to identify weak points in security strategy?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with Identity Protection enabled
- **Configuration:** Investigation of events is key to better understanding and identifying any weak points in your security strategy.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use ID Protection risk reports to investigate identity risks.
2. Follow the framework provided in the article to get started and review common scenarios and recommended actions.

## Validation
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com) as a Security Administrator or Global Administrator.
2. Navigate to Protection > Identity Protection > Risky users. Confirm the report loads and displays a list of users with risk levels (Low, Medium, High).
3. Navigate to Protection > Identity Protection > Risky sign-ins. Confirm the report loads and shows sign-in risk events.
4. Select a risky user and review the risk history and associated risk detections. Verify that risk details (e.g., risk level, detection timing, risk event type) are visible.
5. Select a risky sign-in and confirm that risk details (e.g., risk level, risk event type, IP address, location) are displayed.
6. Use the 'Risk detections' report under Identity Protection to list all risk detections. Confirm that detections are categorized by detection type (e.g., Atypical travel, Anonymous IP address).
7. Export any of the risk reports to CSV and verify the export contains the expected columns (e.g., User, Risk level, Risk state, Detection timing).

## Rollback
1. If the Identity Protection risk reports are not loading or show incorrect data, verify that the user account used has the required permissions (Security Administrator, Global Administrator, or Security Reader).
2. If risk reports are empty or missing expected data, confirm that Microsoft Entra ID P2 licenses are assigned to all users. Navigate to Identity > Overview > Properties and check the tenant's license tier.
3. If risk detections are not appearing, ensure that Identity Protection is enabled for the tenant. Navigate to Protection > Identity Protection > Overview and verify the service status.
4. If the investigation reveals no risks but risks are expected, review the Identity Protection policy settings under Protection > Identity Protection > Policy to ensure risk-based policies (e.g., user risk policy, sign-in risk policy) are configured and enabled.
5. If the exported CSV file is corrupted or incomplete, re-export the report using the same filter criteria and confirm the file downloads successfully.
6. If any changes were made to Identity Protection settings during investigation (e.g., policy modifications), revert those changes by restoring the previous policy configuration from backup or by manually resetting policies to their default state.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk>
