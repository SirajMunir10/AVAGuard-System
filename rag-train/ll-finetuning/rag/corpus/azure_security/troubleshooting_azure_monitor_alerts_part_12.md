# Troubleshooting: Azure Monitor Alerts (408)

**Domain:** Azure
**Subdomain:** Azure Monitor Alerts
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Azure Monitor alerts when calls fail with retryable status codes?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Call failures with status codes 408, 429, 503, 504
- HttpRequestException
- WebException
- TaskCancellationException

## Error Codes
- `408`
- `429`
- `503`
- `504`
- `HttpRequestException`
- `WebException`
- `TaskCancellationException`

## Root Causes
1. Transient failures that allow for the call to be retried

## Remediation Steps
1. Retry the call using retry logic

## Validation
1. Verify that the application or service calling Azure Monitor alerts now uses retry logic with exponential backoff. Check the application logs for successful call completions after retries. 2. Confirm that no new 408, 429, 503, or 504 status codes are logged for the same operation. 3. Run a test call to the Azure Monitor alerts endpoint and inspect the response status code; ensure it returns a 2xx success code. 4. If using an SDK, verify the SDK version includes built-in retry policies (e.g., Azure SDK for .NET).

## Rollback
1. Remove or disable the retry logic implementation from the calling application. 2. Revert to the previous call pattern that did not include retries. 3. If a custom retry policy was added, delete or comment out the retry policy code. 4. Restart the application or service to ensure the change takes effect. 5. Monitor the application logs to confirm that calls are no longer being retried.

## References
- <https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-troubleshoot>
