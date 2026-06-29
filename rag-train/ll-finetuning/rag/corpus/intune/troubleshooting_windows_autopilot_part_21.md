# Troubleshooting: Windows Autopilot

**Domain:** Intune
**Subdomain:** Windows Autopilot
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Windows MDM enrollment being disabled in the Intune tenant during Windows Autopilot OOBE?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** Device platform restrictions

## Symptoms
- Windows MDM enrollment is disabled in the Intune tenant

## Error Codes
N/A

## Root Causes
1. Windows (MDM) enrollment is set to Block in device type restrictions

## Remediation Steps
1. Sign into the Microsoft Intune admin center.
2. In the Home screen, select Devices in the left hand pane.
3. In the Devices | Overview screen, under By platform, select Windows.
4. In the Windows | Windows devices screen, under Device onboarding, select Enrollment.
5. In the Windows | Enrollment screen, under Enrollment options, select Device platform restriction.
6. In the Enrollment restrictions screen, under Device type restrictions, select All Users under the Name column.
7. In the All Users screen that opens, under Manage, select Properties.
8. In the Properties screen that opens, next to Platform settings, select the Edit link.
9. In the Edit restriction screen that opens: Locate Windows (MDM) under the Type column. Make sure that Windows (MDM) is set to Allow under the Platform column. If Windows (MDM) is set to Block, change it to Allow.
10. Select Review + save, and then either Save if a setting was changed, or Cancel if no settings were changed.
11. Repeat the above steps for any additional restrictions that might exist in the Enrollment restrictions screen other than All Users. Only restrictions for the Windows platform need to be verified.

## Validation
1. Sign into the Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to Devices > Windows > Enrollment > Device platform restrictions.
3. Under Device type restrictions, select each restriction (e.g., All Users, any custom restrictions).
4. For each restriction, go to Properties > Edit next to Platform settings.
5. Verify that Windows (MDM) is set to Allow under the Platform column.
6. If any restriction shows Block, change it to Allow, then select Review + save and Save.
7. To confirm the change is effective, attempt a Windows Autopilot OOBE enrollment on a test device and verify that MDM enrollment proceeds without the 'disabled' error.

## Rollback
1. Sign into the Microsoft Intune admin center (https://intune.microsoft.com).
2. Navigate to Devices > Windows > Enrollment > Device platform restrictions.
3. Under Device type restrictions, select the restriction that was modified (e.g., All Users).
4. Go to Properties > Edit next to Platform settings.
5. Locate Windows (MDM) under the Type column and change it back to Block.
6. Select Review + save and then Save.
7. Repeat for any other restrictions that were changed.
8. Verify that the original blocking behavior is restored by checking that MDM enrollment is again disabled for new Autopilot enrollments.

## References
- <https://learn.microsoft.com/en-us/autopilot/troubleshoot-oobe>
