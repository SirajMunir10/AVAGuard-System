# Troubleshooting: Microsoft Defender Antivirus (5008)

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender Antivirus
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Event ID 5008 where the antimalware engine encountered an error and failed?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- The antimalware engine encountered an error and failed.
- Microsoft Defender Antivirus engine was terminated due to an unexpected error.

## Error Codes
- `5008`

## Root Causes
1. Failure type: Crash or Hang
2. Exception Code: Error code
3. Resource: Resource

## Remediation Steps
1. Try to restart the service. For antimalware, antivirus and spyware, at an elevated command prompt, type net stop msmpsvc , and then type net start msmpsvc to restart the antimalware engine.
2. For the Network Inspection System , at an elevated command prompt, type net start nissrv , and then type net start nissrv to restart the Network Inspection System engine by using the NiSSRV.exe file.
3. If it fails in the same way, look up the error code by accessing the Microsoft Support Site and entering the error number in the Search box, and contact Microsoft Technical Support .

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-microsoft-defender-antivirus>
