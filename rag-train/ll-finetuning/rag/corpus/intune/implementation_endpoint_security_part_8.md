# Implementation: Endpoint Security

**Domain:** Intune
**Subdomain:** Endpoint Security
**Incident Type:** Implementation

## Scenario / Query
What are the prerequisites for configuring Microsoft Defender for Endpoint integration with Intune compliance policies?

## Environment Context
- **Tenant Type:** Microsoft Intune
- **Configuration:** Admin roles and permissions

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure admin access to the Microsoft Intune admin center with Endpoint Security Manager role or equivalent permissions.
2. For custom roles, ensure the following rights are assigned: Assign, Create, Delete, Read, and Update for the Device compliance policies permission.

## Validation
1. Sign in to the Microsoft Intune admin center (https://endpoint.microsoft.com) with an account that has the Endpoint Security Manager role or equivalent permissions.
2. Navigate to Endpoint security > Microsoft Defender for Endpoint.
3. Verify that the Microsoft Defender for Endpoint connection status shows 'Enabled' or 'Connected'.
4. Confirm that the compliance policy assignment includes devices that are onboarded to Microsoft Defender for Endpoint.
5. Use the following PowerShell command to verify the connection: Get-MgDeviceManagementManagedDeviceCompliancePolicy -Filter "(scheduledActionConfigurations/any(s:s/actionType eq 'microsoft.graph.deviceComplianceActionType' and s/actionMessage eq 'Microsoft Defender for Endpoint'))"

## Rollback
1. Sign in to the Microsoft Intune admin center with an account that has the Endpoint Security Manager role or equivalent permissions.
2. Navigate to Endpoint security > Microsoft Defender for Endpoint.
3. Set the Microsoft Defender for Endpoint connection to 'Disabled' or 'Disconnect'.
4. Remove any compliance policies that reference Microsoft Defender for Endpoint by navigating to Devices > Compliance policies, selecting the policy, and deleting it.
5. If custom roles were modified, revert the permissions by removing the Assign, Create, Delete, Read, and Update rights for Device compliance policies from the custom role.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
