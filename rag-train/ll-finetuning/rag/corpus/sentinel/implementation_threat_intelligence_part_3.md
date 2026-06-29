# Implementation: Threat Intelligence

**Domain:** Sentinel
**Subdomain:** Threat Intelligence
**Incident Type:** Implementation

## Scenario / Query
How do I create threat intelligence STIX objects using the management interface in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with threat intelligence enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Use the management interface to create STIX objects.
2. Perform common threat intelligence tasks such as indicator tagging and establishing connections between objects.
3. Define relationships as you create new STIX objects.
4. Use the duplicate feature to copy the metadata from a new or existing TI object to quickly create multiple objects.

## Validation
1. In the Azure portal, navigate to your Microsoft Sentinel workspace. 2. Under Threat Management, select Threat Intelligence. 3. Confirm that the new STIX object (e.g., indicator, threat-actor, attack-pattern) appears in the list. 4. Open the object and verify its properties (name, description, pattern, labels) match what was created. 5. If tags were added, check that the tags are visible on the object. 6. If relationships were defined, navigate to the related object and confirm the relationship is listed. 7. If the duplicate feature was used, verify the new object has the same metadata as the source.

## Rollback
1. In the Azure portal, navigate to your Microsoft Sentinel workspace. 2. Under Threat Management, select Threat Intelligence. 3. Locate the STIX object(s) created during the remediation. 4. Select the object(s) and choose Delete (or the delete option in the context menu). 5. Confirm deletion when prompted. 6. If relationships were created, verify that the related objects are no longer linked. 7. If tags were added to existing objects, remove the tags by editing the object and clearing the tag field.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/work-with-threat-indicators>
