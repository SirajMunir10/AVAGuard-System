# Implementation: Endpoint onboarding

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint onboarding
**Incident Type:** Implementation

## Scenario / Query
How to verify that devices are successfully onboarded and appearing in the Microsoft Defender portal after applying Group Policy?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Group Policy deployment for endpoint onboarding

## Symptoms
- Devices do not appear in the Devices inventory list after policy deployment

## Error Codes
N/A

## Root Causes
1. It can take several days for devices to start showing on the Devices list, including time for policy distribution, user logon, and endpoint reporting

## Remediation Steps
1. Go to the Microsoft Defender portal
2. Select Devices inventory
3. Verify that devices are appearing

## Validation
Verify that devices are appearing in the Devices inventory list

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-gp>
