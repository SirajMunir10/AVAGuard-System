# Troubleshooting: Microsoft Defender for Endpoint onboarding

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint onboarding
**Incident Type:** Troubleshooting

## Scenario / Query
How to check and set the Windows diagnostic data service (diagtrack) startup type to automatic during Defender for Endpoint onboarding?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** Windows diagnostic data service (diagtrack) must be set to AUTO_START for successful onboarding

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
1. The Windows diagnostic data service (diagtrack) START_TYPE is not set to AUTO_START

## Remediation Steps
1. Open an elevated command-line prompt on the device: a. Click Start, type cmd, and press Enter. b. Right-click Command prompt and select Run as administrator.
2. Enter the following command, and press Enter: sc qc diagtrack
3. If the START_TYPE isn't set to AUTO_START, then set the service to automatically start by entering: sc config diagtrack start=auto
4. Verify the change by entering: sc qc diagtrack
5. Start the service by entering: sc start diagtrack

## Validation
1. Open an elevated command prompt. 2. Run: sc qc diagtrack. 3. Confirm that the output shows 'START_TYPE' as 'AUTO_START' (value 2). 4. Run: sc query diagtrack. 5. Confirm that the service state is 'RUNNING'.

## Rollback
1. Open an elevated command prompt. 2. Run: sc config diagtrack start=demand. 3. Run: sc stop diagtrack. 4. Verify with: sc qc diagtrack (should show DEMAND_START) and sc query diagtrack (should show STOPPED).

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
