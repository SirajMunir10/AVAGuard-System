# Incident Response: Incident Management

**Domain:** Sentinel
**Subdomain:** Incident Management
**Incident Type:** Incident Response

## Scenario / Query
How do I manage incident status and ownership during an investigation in Microsoft Sentinel?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Set the incident's status to Active until you close it.
2. Assign an owner to the incident by setting the Owner field.
3. Add comments so that other analysts are able to understand what you investigated and what your concerns are around the incident.

## Validation
1. In the Microsoft Sentinel workspace, navigate to Incidents and open the incident you remediated. 2. Verify the Status field shows 'Active' (or the appropriate status you set). 3. Confirm the Owner field displays the assigned user or group. 4. Check the Comments section for the added comments and verify they are visible and correctly reflect the investigation notes.

## Rollback
1. Open the incident in Microsoft Sentinel. 2. If the status was changed incorrectly, set it back to the previous status (e.g., 'New' or 'In Progress') using the Status dropdown. 3. If the owner assignment is wrong, clear the Owner field or reassign to the original owner. 4. If comments contain errors, edit or delete the problematic comments using the comment edit/delete options.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/investigate-cases>
