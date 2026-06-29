# Troubleshooting: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Troubleshooting

## Scenario / Query
How do I configure the time zone for the Identity timeline in Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Settings > Security center > Time zone

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Go to Settings > Security center > Time zone.
2. Select your preferred time zone (local time zone or UTC).

## Validation
1. Navigate to Settings > Security center > Time zone in Microsoft Defender XDR.
2. Confirm the selected time zone matches your preferred setting (local time zone or UTC).
3. Open the Identity timeline for any user and verify that displayed timestamps reflect the chosen time zone.
4. Optionally, use the Microsoft Defender XDR API to retrieve a user's timeline entry and check the time zone offset in the response.

## Rollback
1. Go to Settings > Security center > Time zone in Microsoft Defender XDR.
2. Select the original time zone setting (e.g., UTC if you changed to local, or vice versa).
3. Confirm the change by reviewing the Identity timeline timestamps for a sample user.
4. If the change was made via API, revert the time zone parameter to its previous value using the same API call.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-users>
