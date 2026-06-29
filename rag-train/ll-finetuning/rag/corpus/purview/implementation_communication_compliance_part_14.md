# Implementation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Implementation

## Scenario / Query
How to turn off the Cross-policy resolution setting in Communication Compliance to prevent automatic resolution of all instances of the same policy match?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Communication Compliance settings

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In the Microsoft Purview portal, select Settings in the upper-right corner of the page.
2. Select Communication Compliance.
3. Select the Cross-policy resolution setting to turn it off.

## Validation
1. In the Microsoft Purview portal, navigate to Settings > Communication Compliance. 2. Confirm that the 'Cross-policy resolution' toggle is set to Off. 3. Create a test policy match that would have been automatically resolved under the previous setting and verify it remains unresolved across policies.

## Rollback
1. In the Microsoft Purview portal, navigate to Settings > Communication Compliance. 2. Set the 'Cross-policy resolution' toggle back to On. 3. Confirm the setting is saved and active by checking that a new policy match is automatically resolved across policies.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
