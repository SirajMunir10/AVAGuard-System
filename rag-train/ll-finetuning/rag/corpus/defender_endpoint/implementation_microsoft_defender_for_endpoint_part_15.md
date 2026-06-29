# Implementation: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Implementation

## Scenario / Query
How to create and deploy an application in Microsoft Configuration Manager to onboard devices to Microsoft Defender for Endpoint?

## Environment Context
- **Tenant Type:** Microsoft Configuration Manager
- **Configuration:** Microsoft Defender for Endpoint onboarding

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Create an application in Microsoft Configuration Manager.
2. Select Manually specify the application information.
3. Specify information about the application, then select Next.
4. Specify information about the software center, then select Next.
5. In Deployment types select Add.
6. Select Manually specify the deployment type information, then select Next.
7. Specify information about the deployment type, then select Next.
8. In Content > Installation program specify the command: net start sense.
9. In Detection method, select Configure rules to detect the presence of this deployment type, then select Add Clause.
10. Specify the following detection rule details, then select OK.
11. In Detection method select Next.
12. In User Experience, specify the following information, then select Next.
13. In Requirements, select Next.
14. In Dependencies, select Next.
15. In Summary, select Next.
16. In Completion, select Close.
17. In Deployment types, select Next.
18. In Summary, select Next.
19. In Completion, select Close.
20. Deploy the application by right-clicking the app and selecting Deploy.
21. In General select Automatically distribute content for dependencies and Browse.
22. In Content select Next.
23. In Deployment settings, select Next.
24. In Scheduling select As soon as possible after the available time, then select Next.

## Validation
1. On a target device, open Configuration Manager client and verify the application is installed. 2. Run 'sc query sense' to confirm the Microsoft Defender for Endpoint service is running. 3. Check the device is listed in Microsoft 365 Defender portal under Devices.

## Rollback
1. In Configuration Manager console, right-click the deployed application and select 'Retire' or 'Delete' to remove it. 2. On affected devices, run 'sc stop sense' and 'sc delete sense' to stop and remove the service. 3. Remove any onboarding scripts or packages from the device.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
