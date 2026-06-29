# Hardening: Mail Flow Security

**Domain:** Exchange Online
**Subdomain:** Mail Flow Security
**Incident Type:** Hardening

## Scenario / Query
How do I harden Exchange Online to prevent spoofing by ensuring that only authenticated email from my domain is accepted?

## Environment Context
- **Tenant Type:** Enterprise
- **Configuration:** Custom inbound connector configured to accept email from any IP address

## Symptoms
- Users report receiving phishing emails that appear to come from the organization's own domain
- DMARC reports show a high volume of unauthenticated messages from the domain
- Spam filter is not blocking spoofed internal domain emails

## Error Codes
N/A

## Root Causes
1. Inbound connector is configured to bypass spam filtering for messages from any IP address
2. Sender Policy Framework (SPF) record is missing or misconfigured
3. DomainKeys Identified Mail (DKIM) signing is not enabled for the custom domain
4. DMARC policy is set to 'none' (p=none) instead of 'quarantine' or 'reject'

## Remediation Steps
1. Configure SPF record to include only authorized sending IP addresses and services (e.g., 'include:spf.protection.outlook.com')
2. Enable DKIM signing for the custom domain in the Microsoft 365 Defender portal (Email & Collaboration > Email & Collaboration > Policies & Rules > Threat policies > DKIM)
3. Set DMARC policy to 'p=quarantine' or 'p=reject' in the public DNS TXT record for the domain
4. Review and restrict inbound connectors to only accept email from trusted IP addresses, and ensure the connector does not bypass spam filtering
5. Enable the 'Spoof intelligence' policy in Exchange Online Protection (EOP)

## Validation
Run the following PowerShell command to verify SPF, DKIM, and DMARC records: Resolve-DnsName -Name <domain> -Type TXT | Select-Object -ExpandProperty Strings. Also check that the inbound connector's 'RestrictIPs' parameter includes only your organization's IP ranges.

## Rollback
If issues arise, temporarily set DMARC policy back to 'p=none' and disable DKIM signing in the Microsoft 365 Defender portal. Revert SPF record to the previous value using your DNS hosting provider.

## References
- Microsoft Learn: 'Set up SPF to help prevent spoofing' - https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/set-up-spf-in-office-365-to-help-prevent-spoofing?view=o365-worldwide
- Microsoft Learn: 'Use DKIM to validate outbound email sent from your custom domain' - https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/use-dkim-to-validate-outbound-email?view=o365-worldwide
- CIS Microsoft 365 Foundations Benchmark v2.0.0 - Control 4.1: Ensure SPF record is published for all custom domains
