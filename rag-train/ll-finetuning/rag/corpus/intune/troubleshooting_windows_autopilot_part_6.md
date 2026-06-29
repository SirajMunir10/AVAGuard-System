# Troubleshooting: Windows Autopilot (System.AggregateException: One or more errors occurred. ---> System.DirectoryServices.DirectoryServicesCOMException: A constraint violation occurred.)

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
Why is the error 'The MSA account couldn't be granted permission to create computer objects in the following OUs' occurring when installing the Intune Connector for Active Directory?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** Intune Connector for Active Directory

## Symptoms
- Error message: 'The MSA account couldn't be granted permission to create computer objects in the following OUs'

## Error Codes
- `System.AggregateException: One or more errors occurred. ---> System.DirectoryServices.DirectoryServicesCOMException: A constraint violation occurred.`

## Root Causes
1. The administrator installing and configuring the Intune Connector for Active Directory doesn't have the required permissions as outlined in the Intune Connector for Active Directory Requirements.
2. The organization unit (OU) specified in the Intune Connector for Active Directory ODJConnectorEnrollmentWiazard.exe.config XML configuration file doesn't exist.

## Remediation Steps
1. Follow the steps to Increase the computer account limit in the Organizational Unit if the following error appears in the ODJConnectorUI.log: System.AggregateException: One or more errors occurred. ---> System.DirectoryServices.DirectoryServicesCOMException: A constraint violation occurred.
2. For more information, see Install the Intune Connector for Active Directory on the server.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
