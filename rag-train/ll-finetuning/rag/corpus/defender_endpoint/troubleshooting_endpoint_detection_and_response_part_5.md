# Troubleshooting: Endpoint Detection and Response

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Detection and Response
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot file submission failures for deep analysis in Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Sample collection policy via registry key HKLM\SOFTWARE\Policies\Microsoft\Windows Advanced Threat Protection

## Symptoms
- Problem when trying to submit a file for deep analysis

## Error Codes
N/A

## Root Causes
1. File is not a PE file (does not have .exe or .dll extension)
2. Service does not have access to the file, file is missing, corrupted, or modified
3. Queue is full or temporary connection/communication error
4. Sample collection policy is configured to block sample collection (registry value = 0)

## Remediation Steps
1. Ensure the file in question is a PE file (typically .exe or .dll extensions)
2. Ensure the service has access to the file, that it still exists, and hasn't been corrupted or modified
3. Wait a short while and try to submit the file again
4. If sample collection policy is configured, verify the policy setting allows sample collection by checking the registry value at HKLM\SOFTWARE\Policies\Microsoft\Windows Advanced Threat Protection, Name: AllowSampleCollection, Type: DWORD. Hexadecimal value: 0 = block sample collection, 1 = allow sample collection
5. Change the organizational unit through Group Policy

## Validation
1. Verify the file extension is .exe or .dll using: Get-Item 'C:\path\to\file' | Select-Object Extension
2. Confirm the file exists and is accessible: Test-Path 'C:\path\to\file'
3. Check the sample collection registry value: Get-ItemProperty -Path 'HKLM:\SOFTWARE\Policies\Microsoft\Windows Advanced Threat Protection' -Name 'AllowSampleCollection' | Select-Object -ExpandProperty AllowSampleCollection
   - Expected value: 1 (allow)
4. Attempt to submit the file again via the Microsoft Defender portal and confirm no error is returned.

## Rollback
1. If the registry value was changed to 1, revert to the original value (e.g., 0) using: Set-ItemProperty -Path 'HKLM:\SOFTWARE\Policies\Microsoft\Windows Advanced Threat Protection' -Name 'AllowSampleCollection' -Value 0
2. If Group Policy was modified, restore the previous organizational unit setting via Group Policy Management Console.
3. If the file was replaced or restored, ensure the original file is placed back in its location.
4. Wait a short while and retry submission; if issues persist, contact Microsoft support.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-file-alerts>
