# Troubleshooting: Microsoft Defender XDR

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender XDR
**Incident Type:** Troubleshooting

## Scenario / Query
How do I filter incidents by service or detection source in Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Service/detection sources filter

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Any in the Service/detection sources.
2. Then select Microsoft Defender for IoT in the Product name.

## Validation
1. Navigate to Microsoft Defender XDR portal (https://security.microsoft.com).
2. Go to Incidents & alerts > Incidents.
3. In the 'Service/detection sources' filter, select 'Any'.
4. In the 'Product name' filter, select 'Microsoft Defender for IoT'.
5. Confirm that the incident list refreshes and displays only incidents where the detection source is Microsoft Defender for IoT.
6. Optionally, run the following advanced hunting query to verify:
   ```kusto
   AlertInfo
   | where ServiceSource == "Microsoft Defender for IoT"
   | summarize count() by AlertId
   ```
   Compare the count with the incidents shown in the portal.

## Rollback
1. Navigate to Microsoft Defender XDR portal (https://security.microsoft.com).
2. Go to Incidents & alerts > Incidents.
3. In the 'Service/detection sources' filter, select 'Any' (or the previous selection).
4. In the 'Product name' filter, clear the selection or select 'All' to remove the filter.
5. Confirm that the incident list returns to showing incidents from all detection sources.
6. If the issue persists, clear browser cache or use an InPrivate/Incognito session to reset filter state.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-alerts>
