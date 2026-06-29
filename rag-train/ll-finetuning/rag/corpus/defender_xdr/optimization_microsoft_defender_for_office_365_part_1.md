# Optimization: Microsoft Defender for Office 365

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Office 365
**Incident Type:** Optimization

## Scenario / Query
A security operations team notices that many legitimate emails are being moved to Junk Email folder despite Safe Links policies being correctly configured. How can they optimize the spam confidence level (SCL) threshold and configure Advanced Spam Filter (ASF) settings to reduce false positives while maintaining security?

## Environment Context
- **Tenant Type:** Microsoft 365 Enterprise (E5)
- **Configuration:** Exchange Online Protection (EOP) anti-spam policies with default SCL threshold of 5; Safe Links and Safe Attachments enabled

## Symptoms
- Users report that legitimate internal and external emails are incorrectly classified as spam
- High volume of false positives in the Junk Email folder
- Spam confidence level (SCL) for legitimate emails is consistently above 5

## Error Codes
N/A

## Root Causes
1. The spam confidence level (SCL) threshold is set too aggressively (e.g., SCL 5 or lower) causing legitimate bulk mail to be filtered
2. Advanced Spam Filter (ASF) settings such as 'Increase spam score' or 'Mark as spam' are enabled for rules that are too broad

## Remediation Steps
1. Review the current anti-spam policy: In the Microsoft 365 Defender portal, go to Policies & rules > Threat policies > Anti-spam policies. Select the default policy or custom policy and examine the 'Spam and bulk actions' section.
2. Adjust the SCL threshold: Increase the SCL threshold to 6 or 7 for the 'Spam' action to reduce false positives. For example, set 'Spam' action to 'Move message to Junk Email folder' only when SCL is 6 or higher.
3. Tune Advanced Spam Filter (ASF) settings: Under 'Advanced spam filtering (ASF)', disable or set to 'Off' any ASF rule that is causing false positives, such as 'Numeric IP address in From header' or 'Sender ID filtering hard fail'.
4. Test changes: Use the 'Test mode' option in ASF to evaluate the impact before applying enforcement.
5. Monitor and adjust: After changes, review the Threat Explorer for false positive trends and further refine the SCL threshold or ASF rules as needed.

## Validation
After applying the changes, verify that legitimate emails are no longer moved to Junk Email folder by checking the Threat Explorer for false positive reports and confirming with end users that expected emails are delivered to the Inbox.

## Rollback
If false positives increase or security is compromised, revert the SCL threshold to the previous value (e.g., 5) and re-enable any disabled ASF rules. Document the previous policy settings before making changes.

## References
- Microsoft Learn: 'Anti-spam protection in EOP' - https://learn.microsoft.com/en-us/defender-office-365/anti-spam-protection?view=o365-worldwide
- Microsoft Learn: 'Advanced Spam Filter (ASF) settings' - https://learn.microsoft.com/en-us/defender-office-365/advanced-spam-filtering-asf-settings?view=o365-worldwide
