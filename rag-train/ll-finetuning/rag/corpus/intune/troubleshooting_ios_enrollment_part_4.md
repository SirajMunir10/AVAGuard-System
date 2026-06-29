# Troubleshooting: iOS Enrollment

**Domain:** Intune
**Subdomain:** iOS Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve an error indicating the file format is incorrect when uploading a .pem file to Apple Business Manager or Apple School Manager for Intune enrollment?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** Apple Business Manager or Apple School Manager token server settings

## Symptoms
- Error message indicating the file format is incorrect when uploading a .pem file

## Error Codes
N/A

## Root Causes
1. The .pem file was not created according to the required steps

## Remediation Steps
1. Sign in to Apple Business Manager or Apple School Manager and find the token server that needs to be updated.
2. Select Edit.
3. In the MDM Server Settings section, upload the .pem file, and then select Save.
4. If you receive an error message indicating the file format is incorrect, make sure that the file is created according to step 5.
5. After the file format is fixed, close the page and select Edit again.
6. In the MDM Server Settings section, upload the .pem file, and then select Save.
7. Select Download Token to download the new token.
8. Sign in to Intune and select to refresh the downloaded token.

## Validation
1. Confirm the .pem file was recreated following the exact steps in the documentation (step 5 of the remediation).
2. Sign in to Apple Business Manager or Apple School Manager, navigate to the token server, and verify the MDM Server Settings now show the uploaded .pem file without errors.
3. Download the new token from Apple Business Manager or Apple School Manager.
4. Sign in to Intune, go to Tenant Administration > Apple MDM Push Certificate, and select 'Refresh' to upload the downloaded token.
5. Verify no error messages appear during the refresh process and the certificate status shows as active.

## Rollback
1. If the .pem file upload still fails, revert to the previous .pem file (if available) by uploading it in Apple Business Manager or Apple School Manager.
2. If no previous .pem file exists, contact Apple Support to regenerate the token server settings.
3. In Intune, do not refresh the token until a valid .pem file is successfully uploaded; keep the existing token in place.
4. If the refresh in Intune causes issues, re-upload the last known good token by downloading it from Apple Business Manager or Apple School Manager and refreshing in Intune.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-ios-enrollment-errors>
