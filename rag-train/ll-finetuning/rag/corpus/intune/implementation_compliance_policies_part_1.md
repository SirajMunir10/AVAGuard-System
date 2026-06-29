# Implementation: Compliance Policies

**Domain:** Intune
**Subdomain:** Compliance Policies
**Incident Type:** Implementation

## Scenario / Query
How to configure Windows OS version build ranges in a compliance policy to ensure devices are compliant?

## Environment Context
- **Tenant Type:** Intune managed
- **Configuration:** Windows 11 24H2, 23H2, Windows 10 22H2 build ranges

## Symptoms
- Device user receives noncompliant notification from Company Portal when device build is outside specified ranges

## Error Codes
N/A

## Root Causes
1. Device OS build version does not fall within any of the specified compliant ranges in the policy

## Remediation Steps
1. Specify multiple ranges of OS version builds in the compliance policy
2. Document the acceptable OS version ranges for managed devices in your organization

## Validation
Company Portal notifies device user that the device is noncompliant with this setting if build is outside ranges

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/compliance-policy-create-windows>
