# Troubleshooting: Hybrid Identity

**Domain:** Entra ID
**Subdomain:** Hybrid Identity
**Incident Type:** Troubleshooting

## Scenario / Query
How to collect authentication logs for troubleshooting hybrid Azure AD join issues on Windows current devices?

## Environment Context
- **Tenant Type:** Hybrid
- **Configuration:** Azure AD hybrid join

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Download the Auth.zip file.
2. Extract the files to a folder, such as c:\temp, and then go to the folder.
3. From an elevated Azure PowerShell session, run .\start-auth.ps1 -vAuth -accepteula.
4. Select Switch Account to toggle to another session with the problem user.
5. Reproduce the issue.
6. Select Switch Account to toggle back to the admin session that's running the tracing.
7. From the elevated PowerShell session, run .\stop-auth.ps1.
8. Zip (compress) and send the folder Authlogs from the folder where the scripts were executed.

## Validation
1. Verify that the Authlogs folder exists in the extraction directory (e.g., c:\temp\Authlogs).
2. Confirm that the folder contains at least one .etl or .log file indicating traces were captured.
3. Check that the compressed Authlogs.zip file is present and can be opened.
4. Optionally, review the logs for entries related to the user's authentication attempt during the reproduction step.

## Rollback
1. Delete the extracted Authlogs folder and its contents from the extraction directory.
2. Delete the Auth.zip file if it was downloaded to a temporary location.
3. Close any elevated PowerShell sessions that were opened for tracing.
4. If the tracing scripts modified any system state (e.g., registry keys for logging), restore those keys to their original values using a known good backup or default settings.

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
