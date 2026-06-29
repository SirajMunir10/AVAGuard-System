# Implementation: Endpoint DLP

**Domain:** Purview
**Subdomain:** Endpoint DLP
**Incident Type:** Implementation

## Scenario / Query
What are the prerequisites for enabling advanced classification scanning on Windows devices for DLP?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Advanced classification scanning and protection support

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure devices run supported Windows versions: all Windows 11 versions, Windows 10 versions 20H1/21H1 or higher (KB 5006738), or Windows 10 RS5 (KB 5006744)
2. For Windows 10 devices, install KB5016688
3. For Windows 11 devices, install KB5016691
4. Enable advanced classification before Activity explorer displays contextual text for DLP rule-matched events

## Validation
1. Verify the Windows version on the device: run 'winver' and confirm it matches supported versions (Windows 11 all versions, Windows 10 20H1/21H1 or higher with KB 5006738, or Windows 10 RS5 with KB 5006744).
2. Check installed updates: run 'wmic qfe list brief /format:text' and confirm KB5016688 (Windows 10) or KB5016691 (Windows 11) is present.
3. Confirm advanced classification is enabled: in the Microsoft Purview compliance portal, navigate to Endpoint DLP settings and verify 'Advanced classification scanning and protection' is turned on.
4. Validate Activity explorer shows contextual text for DLP rule-matched events: generate a test DLP event and check Activity explorer for the presence of contextual text.

## Rollback
1. If advanced classification scanning causes issues, disable it: in the Microsoft Purview compliance portal, go to Endpoint DLP settings and turn off 'Advanced classification scanning and protection'.
2. If a specific KB update causes problems, uninstall it: run 'wusa /uninstall /kb:5016688' (Windows 10) or 'wusa /uninstall /kb:5016691' (Windows 11) from an elevated command prompt.
3. If the device OS version is incompatible, downgrade to a supported version or apply the required KB updates as per the remediation steps.
4. After rollback, verify DLP functionality by checking that DLP rules still apply and events appear in Activity explorer (without contextual text).

## References
- <https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings>
