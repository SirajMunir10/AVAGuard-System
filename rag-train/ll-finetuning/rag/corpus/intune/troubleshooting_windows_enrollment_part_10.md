# Troubleshooting: Windows Enrollment

**Domain:** Intune
**Subdomain:** Windows Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to correct the MDM terms of use URL for Windows enrollment issues?

## Environment Context
- **Tenant Type:** Azure/Entra ID
- **Configuration:** MDM terms of use URL

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign in to the Azure portal, and then select Microsoft Entra ID.
2. Select Mobility (MDM and MAM), and then click Microsoft Intune.
3. Select Restore default MDM URLs, verify that the MDM terms of use URL is set to https://portal.manage.microsoft.com/TermsofUse.aspx.
4. Choose Save.

## Validation
1. Sign in to the Azure portal (https://portal.azure.com).
2. Navigate to Microsoft Entra ID > Mobility (MDM and MAM) > Microsoft Intune.
3. Verify that the 'MDM terms of use URL' field displays: https://portal.manage.microsoft.com/TermsofUse.aspx.
4. Confirm the URL is saved by refreshing the page and rechecking the field.

## Rollback
1. Sign in to the Azure portal (https://portal.azure.com).
2. Navigate to Microsoft Entra ID > Mobility (MDM and MAM) > Microsoft Intune.
3. In the 'MDM terms of use URL' field, enter the previous custom URL (if known) or restore the default by selecting 'Restore default MDM URLs'.
4. Choose 'Save' to revert the change.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-windows-enrollment-errors>
