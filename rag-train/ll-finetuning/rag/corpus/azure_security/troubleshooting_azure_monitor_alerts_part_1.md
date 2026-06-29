# Troubleshooting: Azure Monitor Alerts (408)

**Domain:** Azure
**Subdomain:** Azure Monitor Alerts
**Incident Type:** Troubleshooting

## Scenario / Query
A webhook action group is failing to trigger. How do I troubleshoot webhook retries and error codes?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Azure Monitor alert action groups with webhook

## Symptoms
- Webhook action not triggering
- Webhook unresponsive or returning errors

## Error Codes
- `408`
- `429`
- `503`
- `504`
- `HttpRequestException`
- `WebException`
- `TaskCancellationException`

## Root Causes
1. Webhook call fails and retries are exhausted
2. Webhook endpoint returns status codes 408, 429, 503, 504, or exceptions like HttpRequestException, WebException, or TaskCancellationException

## Remediation Steps
1. When a webhook is invoked, if the first call fails, it's retried at least 1 more time, and up to five times (5 retries) at various delay intervals: 5 seconds between 1st and 2nd attempt, 20 seconds between 2nd and 3rd, 5 seconds between 3rd and 4th, 40 seconds between 4th and 5th, 5 seconds between 5th and 6th attempt.
2. After retries attempted to call the webhook fail, no action group calls the endpoint for 15 minutes.
3. The retry logic assumes that the call can be retried. Status codes 408, 429, 503, 504, or HttpRequestException, WebException, or TaskCancellationException allow for the call to be retried.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-troubleshoot>
