# Troubleshooting: Self-Service Password Reset (OnPremisesSuccessCloudFailure)

**Domain:** Entra ID
**Subdomain:** Self-Service Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
A user receives 'OnPremisesSuccessCloudFailure' error: password reset was successful on-premises but failed to write to the cloud. How to resolve?

## Environment Context
- **Tenant Type:** Entra ID with on-premises synchronization
- **Configuration:** Password writeback

## Symptoms
- Message: 'We've reset your password successfully, but you have to wait a few minutes before the changes are committed to the cloud.'
- Message: 'Password reset was successful on-premises, but there was an error while writing to the cloud.'

## Error Codes
- `OnPremisesSuccessCloudFailure`

## Root Causes
1. Error while writing to the cloud
2. Error might be caused by a time-out, or a cloud password policy, throttling, or other reasons

## Remediation Steps
1. Wait a few minutes before the changes are committed to the cloud
2. If issue persists, contact admin to investigate

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr>
