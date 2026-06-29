# Configuration: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Configuration

## Scenario / Query
How do I configure the Cross-policy resolution setting in Communication Compliance?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Cross-policy resolution setting (preview)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In the Microsoft Purview portal, select Settings in the upper-right corner of the page.
2. Select Communication Compliance.
3. Select the Cross-policy resolution setting.
4. To turn off the setting, clear the checkbox or toggle it off.

## Validation
1. Navigate to Microsoft Purview portal > Settings > Communication Compliance. 2. Confirm the 'Cross-policy resolution setting' checkbox is unchecked or toggled off. 3. Verify that no cross-policy resolution is active by checking that policy alerts are not aggregated across policies in the investigation view.

## Rollback
1. Navigate to Microsoft Purview portal > Settings > Communication Compliance. 2. Select the 'Cross-policy resolution setting'. 3. Check the checkbox or toggle it on to re-enable the feature. 4. Confirm the setting is enabled by verifying that policy alerts are aggregated across policies in the investigation view.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
