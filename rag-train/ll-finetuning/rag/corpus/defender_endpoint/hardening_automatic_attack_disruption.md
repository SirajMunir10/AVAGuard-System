# Hardening: Automatic Attack Disruption

**Domain:** Defender for Endpoint
**Subdomain:** Automatic Attack Disruption
**Incident Type:** Hardening

## Scenario / Query
How does Microsoft Defender establish confidence for automatic attack disruption actions, and what is the process for excluding assets from automated containment?

## Environment Context
- **Tenant Type:** Microsoft 365 Defender
- **Configuration:** Automatic attack disruption enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. For containment actions, Defender maintains a confidence level of 99% or higher based on real production data.
2. Defender evaluates each detector hit against a broad set of indicators to classify true positives and false positives by combining machine learning outputs, cross-workload correlation, and expert-led incident classification.
3. Defender validates detectors in audit mode before broad release and gradually deploys only detectors that meet strict quality requirements.
4. Disruption detectors are continuously and dynamically evaluated to maintain detection quality and confidence.
5. Microsoft security experts continuously review disruption activity, monitor anomalies, and assess impact to preserve high detection quality over time.
6. All automatic actions can be undone by your security team, so you maintain full control over your environment.
7. Automatic attack disruption enables the exclusion of specific user accounts, devices, and IP addresses from automated containment actions.
8. Excluding assets from automated responses isn't recommended because it can reduce the effectiveness of automatic attack disruption in protecting your environment from sophisticated, high-impact attacks.

## Validation
1. Confirm that automatic attack disruption is enabled: Navigate to Microsoft 365 Defender > Settings > Endpoints > Advanced features > Automatic attack disruption and verify the toggle is set to 'On'. 2. Review the confidence level of recent disruption actions: In Microsoft 365 Defender, go to Incidents & alerts > Incidents, select an incident where automatic disruption was triggered, and check the 'Attack story' tab for the 'Confidence level' indicator (should be 99% or higher). 3. Verify exclusion lists: Go to Settings > Endpoints > Automated investigation and response > Exclusions and confirm that any user accounts, devices, or IP addresses listed are those intended for exclusion. 4. Check audit mode status: In the same section, ensure that any detectors in audit mode are documented and that no disruption actions are taken for those detectors. 5. Review recent disruption activity: In the Microsoft 365 Defender portal, go to Incidents & alerts > Incidents, filter by 'Automatic attack disruption', and confirm that all actions are logged with their status (e.g., 'Completed', 'Undone').

## Rollback
1. To undo a specific automatic containment action: In Microsoft 365 Defender, go to Incidents & alerts > Incidents, select the incident, then under 'Actions' choose 'Undo' for the device, user, or IP containment action. 2. To remove an exclusion: Navigate to Settings > Endpoints > Automated investigation and response > Exclusions, select the entry to remove, and click 'Remove'. 3. To disable automatic attack disruption temporarily: Go to Settings > Endpoints > Advanced features > Automatic attack disruption and set the toggle to 'Off'. 4. To revert a device to its previous state: If a device was contained, use the 'Release from quarantine' action in the Device inventory or via a manual remediation step. 5. To restore a user account: In Microsoft 365 Defender, go to Incidents & alerts > Incidents, select the incident, and under 'Actions' choose 'Undo' for the user containment action.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/automatic-attack-disruption>
