# Troubleshooting: iOS Enrollment

**Domain:** Intune
**Subdomain:** iOS Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve an error that occurs while uploading the Enrollment Program token in Intune?

## Environment Context
- **Tenant Type:** Intune administrator
- **Configuration:** ADE token upload

## Symptoms
- Error message: An error occurred while uploading the Enrollment Program token
- Error message: An error occurred
- Request ID: AjaxError: ajaxExtended call failed

## Error Codes
N/A

## Root Causes
1. ADE token upload failure

## Remediation Steps
1. Sign in to Graph Explorer as an Intune administrator.
2. Run a GET request to enumerate the tokens in the tenant by using the following URL: https://graph.microsoft.com/beta/deviceManagement/depOnboardingSettings
3. If necessary, grant consent and rerun the request.
4. Find the GUID of the token that needs to be renewed.
5. Run a GET request to get the public encryption key of the token by using the following URL: https://graph.microsoft.com/beta/deviceManagement/depOnboardingSettings/<TokenGuid>/getEncryptionPublicKey
6. Copy the value from the response and create a text file as follows. Then, save the text file as a .pem file. For example, token.pem. The file contains three lines, and there are no link breaks in the base64 string. -----BEGIN CERTIFICATE----- SOMEBASE64STRING== -----END CERTIFICATE-----
7. Sign in to Apple Business Manager or Apple School Manager and find the token server that needs to be updated. Then, select Edit.

## Validation
1. Sign in to Graph Explorer as an Intune administrator. 2. Run a GET request to enumerate the tokens: https://graph.microsoft.com/beta/deviceManagement/depOnboardingSettings. 3. Confirm the response includes the token GUID that was renewed and that its 'lastModifiedDateTime' reflects the recent update. 4. Run a GET request to retrieve the public encryption key: https://graph.microsoft.com/beta/deviceManagement/depOnboardingSettings/<TokenGuid>/getEncryptionPublicKey. 5. Verify the response contains a valid base64-encoded certificate string. 6. In Apple Business Manager or Apple School Manager, confirm the token server shows the updated token and the status is 'Active' or 'Valid'.

## Rollback
1. Sign in to Apple Business Manager or Apple School Manager. 2. Locate the token server that was edited and select 'Edit'. 3. Upload the previous valid token file (if available) or re-download the original token from Apple. 4. Save the changes. 5. In Intune, navigate to 'Tenant administration' > 'Connectors and tokens' > 'Apple Enrollment Program tokens'. 6. Select the affected token and choose 'Renew' or 'Upload' to replace it with the original token. 7. Confirm the token status returns to 'Active' and no errors are displayed.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-ios-enrollment-errors>
