# Implementation: Microsoft Defender for Endpoint

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Endpoint
**Incident Type:** Implementation

## Scenario / Query
During the initial onboarding of devices to Microsoft Defender for Endpoint, a security administrator notices that some Windows 10 devices show an 'Inactive' status in the Microsoft 365 Defender portal even though the Microsoft Defender for Endpoint agent is installed and appears to be running. What are the common causes and documented remediation steps for this issue?

## Environment Context
- **Tenant Type:** Microsoft 365 E5
- **Configuration:** Devices are joined to Azure AD and enrolled via Group Policy; Microsoft Defender for Endpoint is configured with the default onboarding policy.

## Symptoms
- Windows 10 devices show 'Inactive' status in Microsoft 365 Defender portal
- Microsoft Defender for Endpoint agent (Sense) is installed and running on the device
- Device appears in the device inventory but with last seen timestamp older than 7 days

## Error Codes
N/A

## Root Causes
1. Device is not properly connected to the Microsoft Defender for Endpoint cloud service due to network proxy or firewall blocks
2. The Microsoft Defender for Endpoint service (Sense) is not started or is in a stopped state
3. Device is not receiving the onboarding policy or the onboarding script has not been applied successfully
4. Device has been unenrolled from the onboarding policy or the policy has expired

## Remediation Steps
1. Verify that the Microsoft Defender for Endpoint service (Sense) is running on the device. Open an elevated PowerShell prompt and run: 'Get-Service -Name Sense' to check the status. If stopped, start the service using 'Start-Service -Name Sense'.
2. Check network connectivity: Ensure the device can reach the required URLs listed in 'Configure device proxy and internet connectivity settings' documentation. Use the Microsoft Defender for Endpoint connectivity test tool (MDECA) as described in the official guide.
3. Reapply the onboarding script: Download the latest onboarding package from the Microsoft 365 Defender portal (Settings > Endpoints > Onboarding) and run the script on the device with administrative privileges.
4. If the device was previously onboarded and then removed, ensure that the offboarding script has been run before reapplying the onboarding script. Refer to 'Offboard devices from Microsoft Defender for Endpoint' documentation.
5. If the issue persists, verify that the device's time is synchronized with an NTP server and that the device's clock is accurate.

## Validation
After applying the remediation steps, the device should show an 'Active' status in the Microsoft 365 Defender portal within a few hours. You can also run the 'Get-MpComputerStatus' PowerShell cmdlet to confirm that the AMProductVersion and AMServiceEnabled fields are populated correctly.

## Rollback
If the device was previously offboarded and you need to revert to the offboarded state, run the offboarding script from the Microsoft 365 Defender portal. If the device was never onboarded, simply do not apply the onboarding script.

## References
- <https://learn.microsoft.com/en-us/defender-endpoint/troubleshoot-onboarding>
- <https://learn.microsoft.com/en-us/defender-endpoint/configure-proxy-internet>
