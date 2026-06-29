# Implementation: Endpoint Protection

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Protection
**Incident Type:** Implementation

## Scenario / Query
How to verify the Endpoint Protection client installation on a reference computer after deploying via SCCM?

## Environment Context
- **Tenant Type:** On-premises
- **Configuration:** System Center Endpoint Protection client installed on reference computer

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. On the reference computer, open System Center Endpoint Protection from the Windows notification area.
2. On the Home tab of the System Center Endpoint Protection dialog box, verify that Real-time protection is set to On.
3. Verify that up to date is displayed for Virus and spyware definitions.
4. To make sure that your reference computer is ready for imaging, under Scan options, select Full, and then click Scan now.

## Validation
1. On the reference computer, open System Center Endpoint Protection from the Windows notification area.
2. On the Home tab, verify that Real-time protection is set to On.
3. Verify that 'up to date' is displayed for Virus and spyware definitions.
4. Under Scan options, select Full, and then click Scan now to confirm the client is ready for imaging.

## Rollback
1. If the client is not installed or not functioning, re-run the SCCM deployment to push the System Center Endpoint Protection client to the reference computer.
2. If real-time protection is off, enable it via the client UI or Group Policy.
3. If definitions are outdated, trigger a manual update from the Update tab or use the command: "%ProgramFiles%\Microsoft Security Client\MpCmdRun.exe" -SignatureUpdate
4. If the scan fails, check the client logs at %ProgramFiles%\Microsoft Security Client\MpLog.txt for errors and resolve accordingly.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-sccm>
