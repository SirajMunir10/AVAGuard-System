# Troubleshooting: Windows Autopilot (Cannot start service ODJConnectorSvc on computer '.')

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
Why is the error 'Cannot start service ODJConnectorSvc on computer '.' occurring when setting up the Intune Connector for Active Directory?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** Intune Connector for Active Directory

## Symptoms
- Error message: 'Cannot start service ODJConnectorSvc on computer '.'

## Error Codes
- `Cannot start service ODJConnectorSvc on computer '.'`

## Root Causes
1. The domain has more than one domain controller with a replication latency policy. The MSA was created in one of the domain controllers but the search happened against another domain controller.
2. A group policy is configured that doesn't allow services to be started as a non-privileged account.

## Remediation Steps
1. Wait until replication has completed in accordance with your policy or manually sync. Once the replication is complete, then open the connector and choose Configure MSA.
2. Make sure the MSA account has Log on as a service privileges granted. For example, see this instance with Operations Manager to Enable service logon.

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
