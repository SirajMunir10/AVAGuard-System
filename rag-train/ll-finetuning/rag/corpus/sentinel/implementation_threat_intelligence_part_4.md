# Implementation: Threat Intelligence

**Domain:** Sentinel
**Subdomain:** Threat Intelligence
**Incident Type:** Implementation

## Scenario / Query
How do I create a new STIX object in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with Threat Intelligence enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Select Add new > TI object.
2. Choose the Object type, then fill in the form on the New TI object page. Required fields are marked with a red asterisk (*).
3. Consider designating a sensitivity value, or Traffic light protocol (TLP) rating to the TI object.
4. If you know how this object relates to another threat intelligence object, indicate that connection with the Relationship type and the Target reference.
5. Select Add for an individual object, or Add and duplicate if you want to create more items with the same metadata.

## Validation
1. Navigate to the Microsoft Sentinel workspace in the Azure portal. 2. Under Threat Management, select Threat Intelligence. 3. Verify that the newly created STIX object appears in the list of threat intelligence objects. 4. Click on the object to open its details and confirm that all required fields (Object type, name, etc.) are correctly populated. 5. Check that any specified sensitivity/TLP rating and relationships are displayed as configured.

## Rollback
1. In the Microsoft Sentinel workspace, go to Threat Intelligence. 2. Locate the STIX object you created. 3. Select the object and choose Delete (or the appropriate delete action) to remove it. 4. Confirm the deletion when prompted. 5. If the object was part of a bulk creation, repeat steps 2-4 for each object that needs to be removed.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/work-with-threat-indicators>
