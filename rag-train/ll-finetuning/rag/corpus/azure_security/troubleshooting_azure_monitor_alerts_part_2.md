# Troubleshooting: Azure Monitor Alerts (408)

**Domain:** Azure
**Subdomain:** Azure Monitor Alerts
**Incident Type:** Troubleshooting

## Scenario / Query
How do I troubleshoot a webhook endpoint that is not working correctly in Azure Monitor action groups?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Webhook endpoint is unresponsive or returns errors
- Webhook calls fail after retries

## Error Codes
- `408`
- `429`
- `503`
- `504`
- `HttpRequestException`
- `WebException`
- `TaskCancellationException`

## Root Causes
1. Webhook endpoint is incorrectly configured
2. Webhook endpoint is not working correctly
3. Incorrect JSON format for Slack or Microsoft Teams endpoints
4. Webhook becomes unresponsive or returns errors

## Remediation Steps
1. Verify that the webhook endpoint you configured is correct, and that the endpoint is working correctly.
2. Check your webhook logs or instrument its code so you could investigate (for example, log the incoming payload).
3. Ensure you are using the correct format for calling Slack or Microsoft Teams; each of these endpoints expects a specific JSON format.
4. Follow instructions to configure a logic app action instead.
5. Note that when a webhook is invoked, if the first call fails, it's retried at least 1 more time, and up to five times (5 retries) at various delay intervals (5, 20, 40 seconds). The delay between 1st and 2nd attempt is 5 seconds, between 2nd and 3rd attempt is 20 seconds, between 3rd and 4th attempt is 5 seconds, between 4th and 5th attempt is 40 seconds, between 5th and 6th attempt is 5 seconds.
6. After retries attempted to call the webhook fail, no action group calls the endpoint for 15 minutes.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-troubleshoot>
