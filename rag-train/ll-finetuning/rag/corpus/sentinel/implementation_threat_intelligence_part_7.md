# Implementation: Threat Intelligence

**Domain:** Sentinel
**Subdomain:** Threat Intelligence
**Incident Type:** Implementation

## Scenario / Query
How to tag and edit threat intelligence objects in Microsoft Sentinel?

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
1. Use the management interface to sort, filter, and search for your threat intelligence.
2. After you find the objects you want to work with, multiselect them choosing one or more objects of the same type.
3. Select Add tags and tag them all at once with one or more tags.
4. Because tagging is free-form, we recommend that you create standard naming conventions for tags in your organization.
5. Edit threat intelligence one object at a time, whether created directly in Microsoft Sentinel or from partner sources, like TIP and TAXII servers.
6. For threat intel created in the management interface, all fields are editable.
7. For threat intel ingested from partner sources, only specific fields are editable, including tags, Expiration date, Confidence, and Revoked.

## Validation
1. In the Microsoft Sentinel management interface, navigate to Threat Intelligence. 2. Sort, filter, and search for the threat intelligence objects that were tagged or edited. 3. Confirm that the tags you added appear on the selected objects. 4. For an object edited individually, open its details and verify that the changed fields (e.g., tags, Expiration date, Confidence, Revoked) reflect the updates. 5. For objects ingested from partner sources, confirm that only the editable fields (tags, Expiration date, Confidence, Revoked) were modified and that non-editable fields remain unchanged.

## Rollback
1. In the Microsoft Sentinel management interface, navigate to Threat Intelligence. 2. Sort, filter, and search for the affected threat intelligence objects. 3. For objects that were tagged, select the objects and remove the tags that were added. 4. For an object that was edited individually, open its details and revert the changed fields to their previous values. Note: For objects ingested from partner sources, only tags, Expiration date, Confidence, and Revoked can be reverted; other fields cannot be changed. 5. If the issue persists, restore from a known good backup of the threat intelligence data if available.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/work-with-threat-indicators>
