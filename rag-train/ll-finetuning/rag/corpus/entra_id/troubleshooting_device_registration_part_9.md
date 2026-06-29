# Troubleshooting: Device Registration (DSREG_AUTOJOIN_ADCONFIG_READ_FAILED (0x801c001d/-2145648611))

**Domain:** Entra ID
**Subdomain:** Device Registration
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot Microsoft Entra hybrid join failures using diagnostic data and event logs?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Hybrid Azure AD join

## Symptoms
- DRS Discovery Test shows FAIL with error code 0x801c0021/0x80072ee2
- Device unable to complete Microsoft Entra hybrid join

## Error Codes
- `DSREG_AUTOJOIN_ADCONFIG_READ_FAILED (0x801c001d/-2145648611)`
- `DSREG_AUTOJOIN_DISC_FAILED (0x801c0021/-2145648607)`
- `DSREG_AUTOJOIN_DISC_WAIT_TIMEOUT (0x801c001f/-2145648609)`
- `DSREG_AUTOJOIN_USERREALM_DISCOVERY_FAILED (0x801c003d/-2145648579)`
- `0x80072ee2`

## Root Causes
1. Unable to read the service connection point (SCP) object and get the Microsoft Entra tenant information
2. Generic discovery failure - failed to get discovery metadata from the data replication service (DRS)
3. Operation timed out while performing discovery
4. Generic realm discovery failure - failed to determine domain type (managed/federated) from STS

## Remediation Steps
1. For DSREG_AUTOJOIN_ADCONFIG_READ_FAILED: Refer to the 'Configure a service connection point' section
2. For DSREG_AUTOJOIN_DISC_WAIT_TIMEOUT: Ensure https://enterpriseregistration.windows.net is accessible in the system context
3. For DSREG_AUTOJOIN_DISC_FAILED: Investigate further by finding the suberror in the next sections
4. For DSREG_AUTOJOIN_USERREALM_DISCOVERY_FAILED: Investigate further by finding the suberror in the next sections
5. Use Event Viewer logs: Open User Device Registration event logs under Applications and Services Log > Microsoft > Windows > User Device Registration and look for event ID 201

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-hybrid-join-windows-current>
