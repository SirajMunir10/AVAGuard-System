# Troubleshooting: Windows Enrollment

**Domain:** Intune
**Subdomain:** Windows Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to disable MDM automatic enrollment in Azure for troubleshooting Windows enrollment errors?

## Environment Context
- **Tenant Type:** Azure/Entra ID
- **Configuration:** MDM User scope in Microsoft Entra ID > Mobility (MDM and MAM) > Microsoft Intune

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Sign in to the Azure portal.
2. Go to Microsoft Entra ID > Mobility (MDM and MAM) > Microsoft Intune.
3. Set MDM User scope to None.
4. Click Save.

## Validation
1. Sign in to the Azure portal (https://portal.azure.com).
2. Navigate to Microsoft Entra ID > Mobility (MDM and MAM) > Microsoft Intune.
3. Confirm that the 'MDM User scope' is set to 'None'.
4. Verify that the 'Save' button is grayed out or that a confirmation message indicates the change was saved.
5. Optionally, attempt to enroll a test Windows device to confirm that automatic MDM enrollment is disabled and no enrollment errors occur.

## Rollback
1. Sign in to the Azure portal (https://portal.azure.com).
2. Navigate to Microsoft Entra ID > Mobility (MDM and MAM) > Microsoft Intune.
3. Set the 'MDM User scope' back to the original setting (e.g., 'All', 'Some', or 'None' as previously configured).
4. Click 'Save' to re-enable automatic MDM enrollment.
5. Verify that the change is saved and that Windows devices can enroll automatically as expected.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-windows-enrollment-errors>
