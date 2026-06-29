# Troubleshooting: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Troubleshooting

## Scenario / Query
How to minimize notifications when using the Paste to supported browsers action in Microsoft Purview Endpoint DLP?

## Environment Context
- **Tenant Type:** Microsoft 365 with Purview
- **Configuration:** Endpoint DLP policy with Paste to supported browsers action

## Symptoms
- Both policy-evaluation and check-complete notifications in Microsoft Edge or policy-evaluation toast on Chrome and Firefox.

## Error Codes
N/A

## Root Causes
1. Classification latency between when the user attempts to paste text into a web page and when the system finishes classifying it and responds.

## Remediation Steps
1. Configure the overall action to Audit and then use the exceptions to Block the target websites.
2. Alternatively, set the overall action to Block and then use the exceptions to Audit the secure websites.
3. Use the latest Antimalware client version.
4. Ensure your version of Microsoft Edge is 120 or higher.
5. Install these Windows KBs: Windows 10: KB5032278, KB5023773; Windows 11 21H2: KB5023774; Win 11 22H2: KB5032288, KB5023778.
6. On macOS, ensure your antimalware Client version is 101.25022.0003 or later.

## Validation
1. Verify that the Endpoint DLP policy has been updated: run `Get-DlpCompliancePolicy -Identity "YourPolicyName" | Format-List` in Exchange Online PowerShell and confirm the 'Mode' property reflects the intended action (e.g., 'Audit' or 'Block') and that the exceptions list includes the target websites. 2. On a test Windows device, open Microsoft Edge (version 120 or later) and attempt to paste sensitive content into a browser that is not in the exceptions list; confirm that only a single notification appears (either policy-evaluation or check-complete, not both). 3. On the same device, attempt to paste into a browser that is in the exceptions list; confirm that the action is either blocked or audited as configured. 4. Check the Antimalware client version by running `Get-MpComputerStatus | Select-Object AMProductVersion` in PowerShell; ensure it is the latest version. 5. Verify Windows KB installation by running `Get-HotFix -Id KB5032278, KB5023773, KB5023774, KB5032288, KB5023778` and confirm each is installed. 6. On macOS, run `mdatp health --field product_version` in Terminal and confirm the version is 101.25022.0003 or later.

## Rollback
1. Restore the original Endpoint DLP policy action: run `Set-DlpCompliancePolicy -Identity "YourPolicyName" -Mode <OriginalMode>` in Exchange Online PowerShell, where <OriginalMode> is the previous setting (e.g., 'Block' or 'Audit'). 2. Remove any newly added exceptions by running `Set-DlpComplianceRule -Identity "YourRuleName" -ExceptIfAccessedBy <OriginalExclusions>` to revert to the previous exclusion list. 3. If the Antimalware client was updated, roll back to the previous version by uninstalling the update via `wusa /uninstall /kb:<KBNumber>` for Windows or by reinstalling the previous macOS version from Microsoft Defender for Endpoint deployment packages. 4. If Windows KBs were installed, uninstall them using `wusa /uninstall /kb:KB5032278` (repeat for each KB) or via Settings > Windows Update > Update history > Uninstall updates. 5. On macOS, if the antimalware client was updated, revert to the previous version by reinstalling the older package from Microsoft Defender for Endpoint deployment packages.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
