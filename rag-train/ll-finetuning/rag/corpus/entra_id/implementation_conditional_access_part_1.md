# Implementation: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Implementation

## Scenario / Query
How to create a Conditional Access policy to block noncompliant devices with Microsoft Defender for Endpoint integration in Intune?

## Environment Context
- **Tenant Type:** Microsoft Entra ID with Intune
- **Configuration:** Endpoint security > Conditional Access

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Go to Conditional Access: In the Microsoft Intune admin center, select Endpoint security > Conditional Access > Create new policy.
2. Basic configuration: Name: Enter a descriptive name, such as 'Block Noncompliant Devices - MDE Integration'.
3. User assignment: Include: Select user groups that should be subject to this policy. Exclude: Exclude your organization's emergency break-glass admin accounts to prevent lockout. If you use Microsoft Entra Connect or Microsoft Entra Connect Cloud Sync, also exclude the Directory Synchronization Accounts directory role.
4. Resource protection: Target resources: Select Cloud apps. Include: Choose Select apps and add: Office 365 SharePoint Online, Office 365 Exchange Online, Other corporate applications as needed.
5. Client app conditions: Conditions > Client apps > Configure: Yes. Select: Browser and Mobile apps and desktop clients. Select Done.
6. Access controls: Grant > Grant access. Select: Require device to be marked as compliant. For multiple controls: Require all the selected controls. Select Select.
7. Enable policy: Set Enable policy to Report-only, and then select Create. The policy is saved but doesn't block access yet.
8. Review report-only results: Wait 24 hours for sign-in data to accumulate, and then review the results: In the Microsoft Entra admin center, go to Identity > Monitoring & health > Sign-in logs. Filter by your policy name and review the Report-only column. Confirm that only expected devices and users show as noncompliant. If the scope looks correct, return to Conditional Access > Policies, select your policy, and change Enable policy to On.

## Validation
Wait 24 hours for sign-in data to accumulate, and then review the results: In the Microsoft Entra admin center, go to Identity > Monitoring & health > Sign-in logs. Filter by your policy name and review the Report-only column. Confirm that only expected devices and users show as noncompliant.

## Rollback
Return to Conditional Access > Policies, select your policy, and change Enable policy to Off.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/advanced-threat-protection-configure>
