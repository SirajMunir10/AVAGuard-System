# Implementation: Endpoint Protection

**Domain:** Defender for Endpoint
**Subdomain:** Endpoint Protection
**Incident Type:** Implementation

## Scenario / Query
How to enable Endpoint Protection and configure custom client settings in Configuration Manager?

## Environment Context
- **Tenant Type:** On-premises Configuration Manager
- **Configuration:** Configuration Manager console, Endpoint Protection site system role

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. In the Configuration Manager console, click Administration.
2. In the Administration workspace, click Client Settings.
3. On the Home tab, in the Create group, click Create Custom Client Device Settings.
4. In the Create Custom Client Device Settings dialog box, provide a name and a description for the group of settings, and then select Endpoint Protection.
5. Configure the Endpoint Protection client settings that you require.
6. Install the Endpoint Protection site system role before you configure client settings for Endpoint Protection.
7. Click OK to close the Create Custom Client Device Settings dialog box.
8. Select the custom client settings you want to deploy.
9. In the Home tab, in the Client Settings group, click Deploy.
10. In the Select Collection dialog box, choose the collection to which you want to deploy the client settings and then click OK.
11. Clients are configured with these settings when they next download client policy.

## Validation
1. In the Configuration Manager console, go to Administration > Client Settings. 2. Verify the custom client device settings you created appear in the list with the name you specified. 3. Select the custom settings and click Properties; confirm that the Endpoint Protection settings are configured as intended. 4. In the Monitoring workspace, review the Client Status dashboard to ensure the targeted collection’s devices have received the policy (check for ‘Policy download’ success). 5. On a targeted client, open the Configuration Manager control panel and verify the ‘Endpoint Protection’ tab shows the configured settings. 6. Run the following command on a client to confirm the policy was applied: `Get-WmiObject -Namespace root\ccm\policy\machine\requestedconfig -Class CCM_EndpointProtectionPolicy`.

## Rollback
1. In the Configuration Manager console, go to Administration > Client Settings. 2. Select the custom client device settings you created. 3. On the Home tab, in the Client Settings group, click Deploy. 4. In the Select Collection dialog, choose the same collection and click OK to redeploy the default client settings (or remove the deployment by selecting the custom settings and clicking Deploy, then choosing ‘None’ if available). 5. Alternatively, delete the custom client settings entirely: select the custom settings, then on the Home tab, in the Delete group, click Delete. 6. If the Endpoint Protection site system role was installed solely for this purpose, you can remove it by going to Administration > Site Configuration > Servers and Site System Roles, selecting the server, right-clicking the Endpoint Protection role, and choosing Remove Role. 7. Clients will revert to default Endpoint Protection settings on their next policy download cycle.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-endpoints-sccm>
