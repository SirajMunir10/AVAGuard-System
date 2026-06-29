# Troubleshooting: Password Reset

**Domain:** Entra ID
**Subdomain:** Password Reset
**Incident Type:** Troubleshooting

## Scenario / Query
How to collect the necessary details to open a support case for SSPR writeback issues?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** SSPR writeback enabled

## Symptoms
- Unable to find the answer to a problem with SSPR writeback

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Provide a general description of the error, including what the error is, the behavior noticed, and how to reproduce the error.
2. Note the page where the error occurred, including the URL if possible and a screenshot of the page.
3. Reproduce the error, then select the Support code link at the bottom of the screen and send the support engineer the GUID that results.
4. If on a page without a support code at the bottom, select F12 and search for the SID and CID and send those two results to the support engineer.
5. Include the precise date and time with the time zone that the error occurred.
6. Provide the user ID of the user who saw the error (e.g., user@contoso.com).
7. Specify if the user is a federated user, pass-through authentication user, password-hash-synchronized user, or cloud-only user.
8. Confirm if the user has a Microsoft Entra ID license assigned.
9. If using password writeback and the error is in your on-premises infrastructure, include a zipped copy of your Application event log from the Microsoft Entra Connect server.

## Validation
1. Confirm that the SSPR writeback feature is enabled in Microsoft Entra ID by navigating to 'Password reset' > 'On-premises integration' and verifying 'Write back passwords to your on-premises directory?' is set to 'Yes'.
2. On the Microsoft Entra Connect server, open Event Viewer and navigate to 'Applications and Services Logs' > 'Microsoft' > 'Azure AD Connect' to confirm no recent errors related to password writeback.
3. Reproduce the SSPR writeback issue and collect the support code GUID by selecting the 'Support code' link at the bottom of the error page.
4. If no support code is available, press F12 to open developer tools, search for 'SID' and 'CID' in the network traffic, and record those values.
5. Verify the user's identity type (federated, PTA, PHS, or cloud-only) by checking the user properties in Microsoft Entra ID under 'Users' > user > 'Authentication methods'.
6. Confirm the user has a valid Microsoft Entra ID license assigned under 'Users' > user > 'Licenses'.
7. If the error is on-premises, zip the Application event log from the Microsoft Entra Connect server (located in Event Viewer under 'Windows Logs' > 'Application') and ensure it is ready for submission.

## Rollback
1. If SSPR writeback was inadvertently disabled during troubleshooting, re-enable it by navigating to 'Password reset' > 'On-premises integration' and setting 'Write back passwords to your on-premises directory?' back to 'Yes'.
2. If changes were made to the Microsoft Entra Connect configuration (e.g., modifying the permissions of the MA service account), restore the original permissions by running the Microsoft Entra Connect wizard and selecting 'Customize synchronization options' to reconfigure password writeback settings.
3. If the Application event log was cleared or modified, restore it from a backup if available, or note that the log cannot be recovered and a new reproduction of the error is needed.
4. If the user's license was temporarily removed for testing, reassign the appropriate Microsoft Entra ID license via 'Users' > user > 'Licenses' > 'Assignments'.
5. If the user's authentication method was changed (e.g., from federated to cloud-only), revert the change by updating the user's 'User principal name' or 'Federation settings' in Microsoft Entra ID Connect or the on-premises directory.

## References
- <https://learn.microsoft.com/en-us/entra/identity/authentication/troubleshoot-sspr-writeback>
