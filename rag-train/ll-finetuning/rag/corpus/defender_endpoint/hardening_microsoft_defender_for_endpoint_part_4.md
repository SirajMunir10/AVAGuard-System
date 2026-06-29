# Hardening: Microsoft Defender for Endpoint

**Domain:** Defender for Endpoint
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Hardening

## Scenario / Query
How to isolate a compromised device using Microsoft Defender for Endpoint while retaining connectivity to the Defender for Endpoint service?

## Environment Context
- **Tenant Type:** Microsoft Defender for Endpoint
- **Configuration:** Selective isolation available for Windows 11, Windows 10 version 1703 or later, Windows Server 2012 R2 and later, Azure Stack HCI OS version 23H2 and later, macOS

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure you have at least the Active remediation actions role assigned.
2. Ensure you have access to the device based on the device group settings.
3. Use a split-tunneling VPN for Microsoft Defender for Endpoint and Microsoft Defender Antivirus cloud-based protection-related traffic to maintain connectivity to the cloud service after isolation.
4. Note: Exclusions such as e-mail, messaging application, and other applications for both macOS and Linux isolation are not supported.
5. Note: Isolating a server running on Microsoft Hyper-V blocks network traffic to all child virtual machines of the server.
6. Note: An isolated device is removed from isolation when an administrator modifies or adds a new iptable rule to the isolated device.

## Validation
1. Confirm the device is listed as 'Isolated' in Microsoft Defender for Endpoint (MDE) under the device inventory. 2. From a separate management console, verify that the device can still communicate with the MDE cloud service by checking the device's last seen timestamp updates in the MDE portal. 3. On the isolated device, run 'nslookup yourtenantname.endpoint.microsoft.com' to confirm DNS resolution succeeds. 4. On the isolated device, run 'Test-NetConnection -ComputerName yourtenantname.endpoint.microsoft.com -Port 443' (PowerShell) to confirm TCP connectivity to the MDE cloud service is allowed.

## Rollback
1. In the MDE portal, navigate to the device inventory, select the isolated device, and choose 'Release from isolation'. 2. Confirm the device status changes from 'Isolated' to 'Active' in the portal. 3. On the device, verify that normal network connectivity is restored by pinging an external host (e.g., 'ping 8.8.8.8'). 4. If the device remains isolated, restart the Microsoft Defender for Endpoint service (via 'net stop sense' then 'net start sense' as Administrator) and re-check the portal status.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/respond-machine-alerts>
