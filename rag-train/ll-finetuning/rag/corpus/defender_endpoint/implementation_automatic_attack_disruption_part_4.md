# Implementation: Automatic Attack Disruption

**Domain:** Defender for Endpoint
**Subdomain:** Automatic Attack Disruption
**Incident Type:** Implementation

## Scenario / Query
How do I configure automatic attack disruption in Microsoft Defender XDR for supported identity services?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Supported identity services: Microsoft Entra ID, Active Directory, Okta (through Microsoft Sentinel integration), AWS IAM (through Microsoft Sentinel integration)

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Configure automatic attack disruption in Microsoft Defender XDR for Microsoft Entra ID and Active Directory (generally available).
2. Enable attack disruption actions in Okta through Microsoft Sentinel integration.
3. Enable attack disruption actions on AWS with Microsoft Sentinel integration.

## Validation
1. In Microsoft Defender XDR, navigate to Settings > Endpoints > Advanced features. Verify that 'Automatic attack disruption' is set to 'On' for Microsoft Entra ID and Active Directory. 2. In Microsoft Sentinel, under Threat management > Analytics > Rule templates, confirm that the 'Okta - automatic attack disruption' rule is enabled. 3. In Microsoft Sentinel, under Threat management > Analytics > Rule templates, confirm that the 'AWS - automatic attack disruption' rule is enabled. 4. Simulate a test attack using the Microsoft 365 Defender evaluation and attack simulation tools to confirm that automatic disruption triggers as expected.

## Rollback
1. In Microsoft Defender XDR, navigate to Settings > Endpoints > Advanced features and set 'Automatic attack disruption' to 'Off' for Microsoft Entra ID and Active Directory. 2. In Microsoft Sentinel, under Threat management > Analytics > Rule templates, disable the 'Okta - automatic attack disruption' rule. 3. In Microsoft Sentinel, under Threat management > Analytics > Rule templates, disable the 'AWS - automatic attack disruption' rule. 4. If any custom configurations were added (e.g., exclusion lists), remove them to restore default behavior.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption>
