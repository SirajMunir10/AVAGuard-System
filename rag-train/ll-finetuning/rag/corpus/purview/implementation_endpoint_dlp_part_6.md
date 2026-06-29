# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
How do I configure file path exclusions for Windows endpoint DLP policies?

## Environment Context
- **Tenant Type:** Windows 10/11 devices
- **Configuration:** Endpoint DLP policy settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the following logic to construct exclusion paths: A valid file path that ends with \ means only files directly under the specified folder are excluded. Example: C:\Temp\
2. A valid file path that ends with \* means only files within subfolders of the specified folder are excluded. Files directly under the specified folder itself aren't excluded. Example: C:\Temp\*
3. A valid file path that ends without \ or \* means all files directly under the specified folder and all of its subfolders are excluded. Example: C:\Temp
4. A path with a wildcard between \ from each side. Example: C:\Users\*\Desktop\
5. A path with a wildcard between \ from each side and with (number) to specify the exact number of subfolders to exclude. Example: C:\Users\*(1)\Downloads\
6. A path with SYSTEM environment variables. Example: %SystemDrive%\Test\*
7. A mix of all the patterns described here. Example: %SystemDrive%\Users\*\Documents\*(2)\Sub\
8. Additional examples: %SystemDrive%\Users\*(1)\AppData\Roaming, %SystemDrive%\Users\*(1)\AppData\Local

## Validation
1. Open the Microsoft Purview compliance portal and navigate to Data Loss Prevention > Endpoint DLP settings > File path exclusions for Windows. 2. Verify that the exclusion paths are configured as per the documented patterns (e.g., C:\Temp\, C:\Temp\*, C:\Temp, C:\Users\*\Desktop\, C:\Users\*(1)\Downloads\, %SystemDrive%\Test\*, %SystemDrive%\Users\*\Documents\*(2)\Sub\, %SystemDrive%\Users\*(1)\AppData\Roaming, %SystemDrive%\Users\*(1)\AppData\Local). 3. On a Windows 10/11 device, create a test file in an excluded folder (e.g., C:\Temp\test.txt) and attempt to copy it to a removable USB drive. 4. Confirm that the file copy is allowed without any DLP policy match or block notification. 5. Create a test file in a non-excluded folder (e.g., C:\NonExcluded\test.txt) and attempt to copy it to a removable USB drive. 6. Confirm that the DLP policy blocks the copy and generates an alert in the Purview portal.

## Rollback
1. In the Microsoft Purview compliance portal, navigate to Data Loss Prevention > Endpoint DLP settings > File path exclusions for Windows. 2. Remove all custom exclusion paths that were added during the remediation. 3. If the exclusion paths were part of a policy, edit the policy to remove the exclusion paths from the 'File path exclusions' setting. 4. On a Windows 10/11 device, create a test file in the previously excluded folder (e.g., C:\Temp\test.txt) and attempt to copy it to a removable USB drive. 5. Confirm that the DLP policy now blocks the copy and generates an alert. 6. Verify that the original DLP behavior is restored by checking that no unintended exclusions remain.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
