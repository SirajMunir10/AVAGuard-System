# Troubleshooting: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve 'Updating the start type of external service' issue?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Updating the start type of external service. Name: %1, actual start type: %2, expected start type: %3, exit code: %4

## Error Codes
N/A

## Root Causes
1. Changes in start type of mentioned service

## Remediation Steps
1. Identify what is causing changes in start type of mentioned service
2. If the exit code isn't 0, fix the start type manually to expected start type

## Validation
1. Open Services console (services.msc).
2. Locate the service named in the '%1' placeholder.
3. Right-click the service, select Properties, and verify the 'Startup type' matches the expected start type ('%3').
4. Alternatively, run: Get-Service -Name '<ServiceName>' | Select-Object Name, StartType
   Confirm StartType equals the expected value (e.g., Automatic, Manual, Disabled).
5. Check the most recent Microsoft Defender for Endpoint onboarding logs at 'C:\ProgramData\Microsoft\Windows Defender\Platform\<version>\MpLog.txt' for any recurring 'Updating the start type' entries with exit code 0.

## Rollback
1. Open Services console (services.msc).
2. Locate the service named in the '%1' placeholder.
3. Right-click the service, select Properties, and change the 'Startup type' back to the actual start type recorded in the error ('%2').
4. Alternatively, run: Set-Service -Name '<ServiceName>' -StartupType '<ActualStartType>'
   Replace '<ActualStartType>' with the value from '%2' (e.g., Automatic, Manual, Disabled).
5. Restart the service if needed: Restart-Service -Name '<ServiceName>' -Force
6. Verify the change by checking the service start type again using Get-Service or Services console.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
