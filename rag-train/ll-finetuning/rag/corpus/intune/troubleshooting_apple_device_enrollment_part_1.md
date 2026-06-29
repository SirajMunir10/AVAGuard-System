# Troubleshooting: Apple Device Enrollment

**Domain:** Intune
**Subdomain:** Apple Device Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
How to resolve sync token errors between Intune and Apple Automated Device Enrollment (ADE) when the token is expired, revoked, or malformed?

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** Apple Business Manager (ABM) or Apple School Manager (ASM) MDM server token

## Symptoms
- Token sync errors between Intune and ADE

## Error Codes
N/A

## Root Causes
1. Token may be expired, revoked, or malformed

## Remediation Steps
1. Renew the token.
2. If issues persist, contact the Intune support team.
3. You may need to use a new public key on the existing MDM server in Apple Business Manager or Apple School Manager: Preferences > MDM Server Settings > Upload Public Key.

## Validation
1. In the Intune admin center, navigate to Devices > iOS/iPadOS > iOS enrollment > Apple Business Manager (or Apple School Manager).
2. Verify the token status shows 'Active' and the expiration date is in the future.
3. Check the 'Last sync' timestamp; it should be recent (within the last 24 hours).
4. Run the sync action manually and confirm no errors appear.
5. Optionally, review the Intune audit logs for token-related events to ensure no renewal or sync failures.

## Rollback
1. If the renewed token causes sync failures, contact Intune support immediately.
2. As a temporary measure, you can revert to the previous token by uploading the old .p7m file in Apple Business Manager > Preferences > MDM Server Settings > Upload Public Key.
3. If the old token is unavailable, you must create a new MDM server in Apple Business Manager and obtain a new token.
4. After reverting, verify the token status and sync as described in the validation steps.

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-ios-enrollment-errors>
