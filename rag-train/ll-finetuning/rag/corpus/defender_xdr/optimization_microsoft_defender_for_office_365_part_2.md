# Optimization: Microsoft Defender for Office 365

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Office 365
**Incident Type:** Optimization

## Scenario / Query
How can I optimize my Microsoft Defender for Office 365 configuration by enabling the 'Allow click-through for URLs' setting in Safe Links policies to reduce false positives while maintaining security?

## Environment Context
- **Tenant Type:** Enterprise with Microsoft 365 E5
- **Configuration:** Safe Links policies currently block all URL clicks without allowing users to proceed to the original URL after warnings.

## Symptoms
- Users report legitimate URLs are blocked by Safe Links, causing productivity loss
- Help desk tickets increase due to users unable to access known safe external sites
- Security team receives false positive alerts for benign URLs

## Error Codes
N/A

## Root Causes
1. Safe Links policy is configured with 'Do not allow users to click through to the original URL' enabled
2. No user override option is set, causing all blocked URLs to be inaccessible even when safe

## Remediation Steps
1. 1. Sign in to the Microsoft 365 Defender portal (https://security.microsoft.com).
2. 2. Go to Email & collaboration > Policies & rules > Threat policies > Safe Links.
3. 3. Select the existing Safe Links policy (or create a new one) and click Edit.
4. 4. In the 'URL and click protection settings' section, under 'Click protection settings', clear the checkbox for 'Do not allow users to click through to the original URL'.
5. 5. Optionally, configure the 'Do not track user clicks' and 'Do not let users click through to the original URL' settings according to your security requirements.
6. 6. Save the policy. The change takes effect within 30 minutes.

## Validation
After the policy update, users should see a warning page when clicking a blocked URL but now have a 'Continue to this website (not recommended)' link to proceed. Verify by testing with a known safe URL that was previously blocked.

## Rollback
Re-enable the 'Do not allow users to click through to the original URL' checkbox in the same Safe Links policy settings.

## References
- Microsoft Learn: 'Safe Links in Microsoft Defender for Office 365' - https://learn.microsoft.com/en-us/defender-office-365/safe-links
