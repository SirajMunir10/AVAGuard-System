# Implementation: Attack Surface Reduction

**Domain:** Defender for Endpoint
**Subdomain:** Attack Surface Reduction
**Incident Type:** Implementation

## Scenario / Query
What are the Windows Server support requirements for ASR rules?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Windows Server 1803 (SAC) or later for standard protection rules; Windows Server 1903 (SAC) or later for Block persistence through WMI event subscription; Windows Server 2016 and Windows Server 2012 R2 require onboarding using the modern unified solution package.

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. For Windows Server 1803 (SAC) or later: Block abuse of exploited vulnerable signed drivers, Block credential stealing from the Windows local security authority subsystem.
2. For Windows Server 1903 (SAC) or later: Block persistence through WMI event subscription.
3. For Windows Server 2016 and Windows Server 2012 R2: Onboard using the modern unified solution package. See New Windows Server 2012 R2 and 2016 functionality in the modern unified solution.

## Validation
1. Verify the Windows Server version: Run `(Get-CimInstance Win32_OperatingSystem).Version` on each server. 2. Confirm ASR rules are enabled: Run `Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Ids` and `Get-MpPreference | Select-Object -ExpandProperty AttackSurfaceReductionRules_Actions`. 3. For servers running Windows Server 2016 or 2012 R2, confirm they are onboarded with the modern unified solution: Run `Get-MpComputerStatus | Select-Object AMProductVersion, AMServiceEnabled` and verify the AMProductVersion is 4.18.2306.0 or later. 4. Check that the specific rules are active: For Windows Server 1803+ ensure 'Block abuse of exploited vulnerable signed drivers' (GUID 56a863a9-875e-4185-98a7-b882c64b5ce5) and 'Block credential stealing from the Windows local security authority subsystem' (GUID 9e6c4e1f-7d60-472f-ba1a-a39ef669e4b2) are set to 1 (block). For Windows Server 1903+ additionally check 'Block persistence through WMI event subscription' (GUID e6db77e5-3df2-4cf1-b95a-636979351e5b) is set to 1.

## Rollback
1. If a server does not meet the required Windows version, upgrade the server to the appropriate SAC release or use the modern unified solution package for Windows Server 2016/2012 R2. 2. If an ASR rule is incorrectly enabled, disable it by running: `Set-MpPreference -AttackSurfaceReductionRules_Ids <GUID> -AttackSurfaceReductionRules_Actions Disabled`. 3. If onboarding with the modern unified solution fails, revert to the previous onboarding method by uninstalling the modern solution and reinstalling the legacy Microsoft Defender for Endpoint agent. 4. If the server is not supported for a specific rule, remove that rule from the ASR policy and apply only the supported rules.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference>
