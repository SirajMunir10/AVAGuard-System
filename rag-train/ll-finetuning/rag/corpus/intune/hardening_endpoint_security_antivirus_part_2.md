# Hardening: Endpoint Security â€“ Antivirus

**Domain:** Intune
**Subdomain:** Endpoint Security â€“ Antivirus
**Incident Type:** Hardening

## Scenario / Query
How do I harden Microsoft Defender Antivirus settings in Intune to block potentially unwanted applications (PUA) and enable cloud-delivered protection?

## Environment Context
- **Tenant Type:** Enterprise (Microsoft 365 E5)
- **Configuration:** Intune endpoint security policies for Antivirus are not configured; default settings are in use.

## Symptoms
- Users can install potentially unwanted applications (e.g., adware, bundlers) without admin approval.
- Cloud-delivered protection is not enabled, reducing detection speed for new threats.

## Error Codes
N/A

## Root Causes
1. Intune Antivirus policy does not have 'Block potentially unwanted applications' set to 'Block'.
2. Cloud-delivered protection is set to 'Not configured' (default) instead of 'Enabled'.

## Remediation Steps
1. 1. Sign in to the Microsoft Intune admin center (https://intune.microsoft.com).
2. 2. Navigate to Endpoint security > Antivirus.
3. 3. Create a new policy or edit an existing one: Platform = Windows 10 and later, Profile = Microsoft Defender Antivirus.
4. 4. Set 'Block potentially unwanted applications' to 'Block'.
5. 5. Set 'Cloud-delivered protection' to 'Enabled'.
6. 6. Set 'Cloud-delivered protection level' to 'High' (or 'High + zero tolerance' if desired).
7. 7. Assign the policy to the appropriate device groups and save.

## Validation
On a targeted Windows device, open Windows Security > App & browser control > Reputation-based protection and verify 'Potentially unwanted app blocking' is 'On'. Also verify in Windows Security > Virus & threat protection > 'Cloud-delivered protection' is 'On'.

## Rollback
In the Intune admin center, edit the Antivirus policy and set 'Block potentially unwanted applications' to 'Not configured' and 'Cloud-delivered protection' to 'Not configured'. Then force a sync on the device or wait for the next check-in.

## References
- <https://learn.microsoft.com/en-us/mem/intune/protect/antivirus-microsoft-defender-settings-windows>
