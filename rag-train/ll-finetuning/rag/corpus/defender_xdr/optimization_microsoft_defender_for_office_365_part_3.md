# Optimization: Microsoft Defender for Office 365

**Domain:** Defender XDR
**Subdomain:** Microsoft Defender for Office 365
**Incident Type:** Optimization

## Scenario / Query
How can I optimize my Microsoft Defender for Office 365 configuration to reduce false positive phishing alerts related to internal sender spoofing?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Anti-phishing policy with spoof intelligence enabled

## Symptoms
- Users report legitimate internal emails being quarantined or flagged as phishing
- High volume of false positive alerts for spoofed internal senders in Defender XDR incidents

## Error Codes
N/A

## Root Causes
1. Spoof intelligence is not configured to allow trusted internal senders or domains
2. Anti-phishing policy does not have an explicit allow entry for the organization's own domain

## Remediation Steps
1. 1. In the Microsoft 365 Defender portal, go to Policies & rules > Threat policies > Anti-phishing > Default policy (or custom policy).
2. 2. Under Spoof intelligence, select 'Review senders that are spoofing your users or domains' and add the internal domain as an allowed spoofed sender.
3. 3. Alternatively, use the Exchange Online PowerShell command: Set-AntiPhishPolicy -Identity "Default" -SpoofAllowBlockList @{Add="contoso.com|contoso.com"} to allow spoofed internal email.
4. 4. Monitor the Spoof intelligence insight for any remaining false positives and adjust as needed.

## Validation
Run Get-AntiPhishPolicy -Identity "Default" | Format-List SpoofAllowBlockList to confirm the internal domain is listed in the allowed spoofed senders.

## Rollback
Remove the allowed entry using Set-AntiPhishPolicy -Identity "Default" -SpoofAllowBlockList @{Remove="contoso.com|contoso.com"}.

## References
- <https://learn.microsoft.com/en-us/defender-office-365/anti-phishing-spoof-intelligence?view=o365-worldwide>
