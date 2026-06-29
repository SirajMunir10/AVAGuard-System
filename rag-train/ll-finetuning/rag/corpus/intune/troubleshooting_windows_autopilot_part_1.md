# Troubleshooting: Windows Autopilot (30132)

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the ODJ connector insufficient privileges error when creating Microsoft Entra hybrid joined computers via Windows Autopilot?

## Environment Context
- **Tenant Type:** Microsoft Entra hybrid joined
- **Configuration:** Windows Autopilot with ODJ connector

## Symptoms
- Event ID 30132 in ODJ Connector Service log with error code 5
- ErrorDescription: 'Failed to get the ODJ Blob. The ODJ connector does not have sufficient privileges to complete the operation'
- DiagnosticCode: 0x00000800
- DiagnosticText: 'Failed to get the ODJ Blob. The ODJ connector does not have sufficient privileges to complete the operation [Exception Message: "DiagnosticException: 0x00000800. Failed to get the ODJ Blob. The ODJ connector does not have sufficient privileges to complete the operation"] [Exception Message: "Failed to call NetProvisionComputerAccount machineName=<ComputerName>"]'

## Error Codes
- `30132`
- `5`
- `0x00000800`

## Root Causes
1. Incorrectly delegating permissions to the organizational unit where the Windows Autopilot devices are created

## Remediation Steps
1. Open Active Directory Users and Computers (DSA.msc)
2. Right-click the organizational unit that you will use to create Microsoft Entra hybrid joined computers > Delegate Control
3. In the Delegation of Control wizard, select Next > Add > Object Types
4. In the Object Types pane, select the Computers check box > OK
5. In the Select Users, Computers, or Groups pane, in the Enter the object names to select box, enter the name of the computer where the Connector is installed
6. Select Check Names to validate your entry > OK > Next
7. Select Create a custom task to delegate > Next
8. Select the Only the following objects in the folder check box, and then select the Computer objects, Create selected objects in this folder, and Delete selected objects in this folder check boxes
9. Select Next
10. Under Permissions, select the Full Control check box (this action selects all the other options)
11. Select Next > Finish

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-windows-enrollment-errors>
