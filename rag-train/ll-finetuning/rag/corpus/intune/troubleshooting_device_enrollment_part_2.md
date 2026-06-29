# Troubleshooting: Device Enrollment (MDM authority not defined)

**Domain:** Intune
**Subdomain:** Device Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve the 'MDM authority not defined' error during device enrollment in Intune?

## Environment Context
- **Tenant Type:** Microsoft Entra ID integrated
- **Configuration:** MDM Authority not set or user credential sync issue

## Symptoms
- User receives an 'MDM authority not defined' error

## Error Codes
- `MDM authority not defined`

## Root Causes
1. Either the MDM Authority has not been set or there is a user credential issue

## Remediation Steps
1. Verify that the MDM Authority has been set appropriately
2. Verify that the user's credentials have synced correctly with Microsoft Entra ID
3. Verify that the user's UPN matches the Active Directory information in the Microsoft 365 admin center
4. If the UPN doesn't match the Active Directory information: Turn off DirSync on the local server
5. Delete the mismatched user from the Intune Account Portal user list
6. Wait about one hour to allow the Azure service to remove the incorrect data
7. Turn on DirSync again and check if the user is now synced properly

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-device-enrollment-in-intune>
