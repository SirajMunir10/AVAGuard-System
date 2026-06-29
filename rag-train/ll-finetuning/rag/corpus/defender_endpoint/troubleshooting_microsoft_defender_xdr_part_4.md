# Troubleshooting: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Troubleshooting

## Scenario / Query
How to view and manage insider risk management alerts within the Microsoft Defender portal?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender with Purview Insider Risk Management provisioned
- **Configuration:** Insider risk management alerts in Defender portal

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. If provisioned access to Microsoft Purview Insider Risk Management, view and manage insider risk management alerts in the Microsoft Defender portal.
2. Hunt for insider risk management events in the Microsoft Defender portal.

## Validation
1. Confirm that the user account has the required roles (e.g., Insider Risk Management Admin, Insider Risk Management Analyst, or Insider Risk Management Investigator) assigned in the Microsoft 365 Defender portal. 2. Navigate to Microsoft 365 Defender (https://security.microsoft.com) > Incidents & alerts > Incidents. 3. Verify that insider risk management alerts appear in the incident queue, filtered by 'Data sensitivity' or 'Insider risk' categories. 4. Select an insider risk alert and confirm that the alert details include the 'Insider risk management' tab with policy name, risk score, and activity timeline. 5. Use advanced hunting in Microsoft 365 Defender with the query: `AlertInfo | where ServiceSource == 'Microsoft 365 Insider Risk Management'` to confirm that insider risk management events are returned.

## Rollback
1. If insider risk management alerts are not visible in the Defender portal, verify that the Microsoft Purview Insider Risk Management solution is provisioned and licensed for the tenant. 2. Ensure that the user has the correct role assignments (Insider Risk Management Admin, Analyst, or Investigator) and that roles are not removed inadvertently. 3. If advanced hunting queries fail, check that the 'Microsoft 365 Insider Risk Management' service source is enabled in the data connector settings. 4. If alerts are missing, review the insider risk management policy configuration in Microsoft Purview compliance portal (https://compliance.microsoft.com) > Insider risk management > Policies to ensure policies are active and generating alerts. 5. If the issue persists, restore default role assignments or re-provision the Insider Risk Management solution via the Microsoft 365 admin center.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-incidents>
