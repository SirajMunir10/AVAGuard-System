# Troubleshooting: Windows Enrollment (hr 0x8007064c)

**Domain:** Intune
**Subdomain:** Windows Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve Windows enrollment error hr 0x8007064c indicating the machine is already enrolled?

## Environment Context
- **Tenant Type:** Intune-managed
- **Configuration:** Windows device enrollment

## Symptoms
- Enrollment fails with the error 'The machine is already enrolled.'
- Enrollment log shows error hr 0x8007064c

## Error Codes
- `hr 0x8007064c`

## Root Causes
1. The computer was previously enrolled
2. The computer has the cloned image of a computer that was already enrolled
3. The account certificate of the previous account is still present on the computer

## Remediation Steps
1. From the Start menu, type Run -> MMC.
2. Choose File > Add/Remove Snap-ins.
3. Double-click Certificates, choose Computer account > Next, and select Local Computer.
4. Double-click Certificates (Local computer) and choose Personal > Certificates.
5. Look for the Intune cert issued by Sc_Online_Issuing, and delete it, if present.
6. If the following registry key exists, delete it: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\OnlineManagement and all sub keys.
7. Try to re-enroll.
8. If the PC still can't enroll, look for and delete this key, if it exists: KEY_CLASSES_ROOT\Installer\Products\6985F0077D3EEB44AB6849B5D7913E95.
9. Try to re-enroll.

## Validation
N/A

## Rollback
For added protection, back up the registry before you modify it. Then, you can restore the registry if a problem occurs.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-windows-enrollment-errors>
