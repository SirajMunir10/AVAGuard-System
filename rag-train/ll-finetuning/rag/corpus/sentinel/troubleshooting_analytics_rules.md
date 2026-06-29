# Troubleshooting: Analytics Rules

**Domain:** Sentinel
**Subdomain:** Analytics Rules
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot validation errors when creating a custom analytics rule in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Custom analytics rule creation in Sentinel

## Symptoms
- Error message appears instead of 'Validation passed' when creating a custom analytics rule

## Error Codes
N/A

## Root Causes
1. Configuration error on one of the wizard tabs

## Remediation Steps
1. Find and select the red X on the tab in the wizard where the error occurred
2. Correct the error
3. Go back to the Review and create tab to run the validation again

## Validation
When the 'Validation passed' message appears, select Create

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/detect-threats-custom>
