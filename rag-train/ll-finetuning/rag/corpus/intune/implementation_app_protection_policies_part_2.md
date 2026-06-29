# Implementation: App Protection Policies

**Domain:** Intune
**Subdomain:** App Protection Policies
**Incident Type:** Implementation

## Scenario / Query
Which client applications support the 'Require app protection policy' grant in Conditional Access?

## Environment Context
- **Tenant Type:** Microsoft Entra ID tenant with Intune integrated
- **Configuration:** Conditional Access policy with grant control set to 'Require app protection policy'

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. The following client apps support this setting (list is not exhaustive and subject to change):
2. Adobe Acrobat Reader mobile app
3. iAnnotate for Office 365
4. Microsoft Cortana
5. Microsoft Dynamics 365 for Phones
6. Microsoft Dynamics 365 Sales
7. Microsoft Edge
8. Microsoft Excel
9. Microsoft Power Automate
10. Microsoft Launcher
11. Microsoft Lists
12. Microsoft Loop
13. Microsoft Office
14. Microsoft OneDrive
15. Microsoft OneNote
16. Microsoft Outlook
17. Microsoft Planner
18. Microsoft Power BI
19. Microsoft PowerApps
20. Microsoft PowerPoint
21. Microsoft SharePoint
22. Microsoft Stream Mobile Native 2.0
23. Microsoft Teams
24. Microsoft To Do
25. Microsoft Word
26. Microsoft Whiteboard Services
27. MultiLine for Intune
28. Nine Mail - Email and Calendar
29. Notate for Intune
30. Provectus - Secure Contacts
31. Viva Engage (Android, iOS, and iPadOS)
32. Windows App (Android, iOS/iPadOS, and Microsoft Edge on Windows)
33. Note: Kaizala, Skype for Business, and Visio do not support the 'Require app protection policy' grant. If these apps are required, use the 'Require approved apps' grant exclusively.

## Validation
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com).
2. Navigate to Protection > Conditional Access > Policies.
3. Select the Conditional Access policy that uses 'Require app protection policy' as a grant control.
4. Under 'Grant', confirm that 'Require app protection policy' is selected.
5. Test the policy by signing in with a user account that is in scope of the policy using each of the supported client apps listed in the remediation steps (e.g., Microsoft Outlook, Microsoft Teams, Microsoft Edge).
6. Verify that access is granted only when the app protection policy is applied to the client app.
7. For apps that do not support this grant (e.g., Kaizala, Skype for Business, Visio), confirm that access is blocked or that an alternative grant (e.g., 'Require approved app') is used.

## Rollback
1. Sign in to the Microsoft Entra admin center (https://entra.microsoft.com).
2. Navigate to Protection > Conditional Access > Policies.
3. Select the Conditional Access policy that was modified.
4. Under 'Grant', change the setting from 'Require app protection policy' to 'Require approved app' or remove the grant control entirely, depending on the original configuration.
5. Save the policy.
6. If the policy was newly created, delete the policy entirely.
7. Verify that users can access resources using the previously blocked client apps (e.g., Kaizala, Skype for Business, Visio) if they are now allowed.

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant>
