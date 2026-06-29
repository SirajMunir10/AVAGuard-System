# Troubleshooting: Incident Investigation

**Domain:** Defender for Endpoint
**Subdomain:** Incident Investigation
**Incident Type:** Troubleshooting

## Scenario / Query
Why might blast radius graphs not fully represent environmental risks during incident investigation?

## Environment Context
- **Tenant Type:** Microsoft Defender XDR
- **Configuration:** Microsoft Sentinel data lake, critical asset definitions

## Symptoms
- Blast radius graphs do not fully represent environmental risks.

## Error Codes
N/A

## Root Causes
1. Further workloads are not enabled.
2. Critical assets are not fully defined.

## Remediation Steps
1. Enable further workloads to increase available environment data.
2. Define critical assets. For more information, see Review and classify critical assets.

## Validation
1. Verify that all relevant workloads are enabled in Microsoft Defender XDR: Navigate to Settings > Endpoints > Advanced features and confirm that all applicable workload integrations (e.g., Microsoft Defender for Cloud Apps, Microsoft Defender for Identity, Microsoft Defender for Office 365) are toggled On. 2. Confirm that critical asset definitions are complete: In Microsoft Defender XDR, go to Assets > Devices, select a device, and check that the 'Critical' classification is assigned as needed. Alternatively, use the Advanced Hunting query: `DeviceInfo | where IsCritical == 1` to list all devices marked as critical. 3. Re-run the incident investigation for a recent incident and inspect the blast radius graph to ensure it now includes all relevant assets and workloads.

## Rollback
1. If enabling a workload causes unintended behavior, disable the workload by navigating to Settings > Endpoints > Advanced features and toggling the corresponding feature Off. 2. If critical asset definitions need to be reverted, use the Microsoft Defender XDR API or portal to remove the 'Critical' classification from devices: In Assets > Devices, select the device, edit its classification, and set it to 'Not classified' or 'Standard'. 3. If the blast radius graph becomes inaccurate, re-run the incident investigation to confirm the graph returns to its previous state.

## References
- <https://learn.microsoft.com/en-us/defender-xdr/investigate-incidents>
