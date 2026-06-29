# Troubleshooting: Windows Enrollment

**Domain:** Intune
**Subdomain:** Windows Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the error 'Something went wrong. Looks like we can't connect to the URL for your organization's MDM terms of use' during Windows enrollment?

## Environment Context
- **Tenant Type:** Hybrid (MDM for Microsoft 365 and Intune)
- **Configuration:** MDM Terms of Use endpoint configuration in Microsoft Entra ID

## Symptoms
- Error message: Something went wrong. Looks like we can't connect to the URL for your organization's MDM terms of use. Try again, or contact your system administrator with the problem information from this page.

## Error Codes
N/A

## Root Causes
1. You use both MDM for Microsoft 365 and Intune on the tenant, and the user who tries to enroll the device doesn't have a valid Intune license or an Office 365 license.
2. The MDM terms and conditions in Microsoft Entra ID is blank or doesn't contain the correct URL.

## Remediation Steps
1. To fix this issue, use one of the following methods:
2. Method 1: Ensure the user has a valid Intune license or Office 365 license.
3. Method 2: Verify and correct the MDM terms and conditions URL in Microsoft Entra ID.

## Validation
1. Confirm the user has a valid license: In Microsoft Entra admin center, go to Users > select the affected user > Licenses > verify an Intune or Office 365 license is assigned. 2. Check MDM terms URL: In Microsoft Entra admin center, go to Mobility (MDM and MAM) > Microsoft Intune > Restore default URLs > verify the MDM terms of use URL is not blank and points to a valid endpoint (e.g., https://portal.manage.microsoft.com/TermsofUse.aspx). 3. Attempt Windows enrollment again and confirm the error no longer appears.

## Rollback
1. If a license was added, remove the Intune or Office 365 license from the user in Microsoft Entra admin center > Users > select user > Licenses > Remove license. 2. If the MDM terms URL was modified, restore the original URL by navigating to Mobility (MDM and MAM) > Microsoft Intune > Restore default URLs > select Restore default URLs. 3. Re-test enrollment to confirm the original error reappears (if desired).

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-windows-enrollment-errors>
