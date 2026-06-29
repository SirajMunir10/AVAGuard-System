# Implementation: Advanced Hunting

**Domain:** Defender for Endpoint
**Subdomain:** Advanced Hunting
**Incident Type:** Implementation

## Scenario / Query
How to query event data from healthy sensors on workstations or domain controllers using Advanced Hunting in Microsoft Defender XDR?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Sensors on workstations or domain controllers transmitting to Microsoft Defender for Endpoint and Microsoft Defender for Identity

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Query event data from healthy sensors on workstations or domain controllers almost immediately after they are available on Microsoft Defender for Endpoint and Microsoft Defender for Identity.
2. To collect even more event properties, turn on aggregated reporting.

## Validation
Run the following Kusto query in Advanced Hunting to confirm that event data from healthy sensors on workstations and domain controllers is being collected:

```kusto
DeviceEvents
| where Timestamp > ago(1h)
| where DeviceType in ("Workstation", "DomainController")
| where SensorHealthState == "Healthy"
| take 10
```

If the query returns results, event data from healthy sensors is being ingested. To verify aggregated reporting is enabled, run:

```kusto
DeviceEvents
| where Timestamp > ago(1h)
| where DeviceType in ("Workstation", "DomainController")
| where SensorHealthState == "Healthy"
| summarize AggregatedCount = count() by DeviceName
| where AggregatedCount > 1
```

If the aggregated count shows multiple events per device, aggregated reporting is active.

## Rollback
If the validation query returns no results or aggregated reporting causes performance issues, disable aggregated reporting by reverting to default event collection settings. To do this, navigate to Microsoft Defender XDR > Settings > Endpoints > Advanced features and turn off 'Aggregated event reporting'. Alternatively, use the following PowerShell command to disable it:

```powershell
Set-MpPreference -DisableAggregatedReporting $true
```

Then, re-run the validation query to confirm that basic event data from healthy sensors is still being collected without aggregation.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview>
