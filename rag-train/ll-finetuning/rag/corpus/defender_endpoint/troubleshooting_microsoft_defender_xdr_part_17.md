# Troubleshooting: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Troubleshooting

## Scenario / Query
How to investigate a user identity in Microsoft Defender XDR using the Observed in organization tab to understand blast radius and potential lateral movement?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** User investigation in Microsoft Defender XDR

## Symptoms
- Need to understand where and how an identity appears across the environment
- Need to assess blast radius and potential lateral movement for a user

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Navigate to the Observed in organization tab for the user identity
2. Review all accounts associated with the identity across identity systems, including automatically and manually correlated accounts
3. Manually link other related accounts if needed
4. Check which account is indicated as the primary account
5. Review devices the identity signed into (usually shows recent activity)
6. Review locations observed for sign-ins
7. Review groups associated with the identity (when available)

## Validation
1. In Microsoft Defender XDR, navigate to the user identity page and select the 'Observed in organization' tab. 2. Verify that all associated accounts (automatically and manually correlated) are listed. 3. Confirm the primary account is correctly indicated. 4. Check that devices, locations, and groups (if available) are displayed and reflect recent activity. 5. Ensure any manually linked accounts appear in the list.

## Rollback
1. If manual linking of accounts was performed, remove the linked accounts by editing the user identity and unlinking them. 2. If any changes were made to the primary account designation, revert to the previous primary account. 3. No other rollback actions are required as the 'Observed in organization' tab is read-only and does not modify the environment.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-users>
