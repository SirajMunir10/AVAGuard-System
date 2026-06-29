# Implementation: Microsoft Defender for Cloud

**Domain:** Azure
**Subdomain:** Microsoft Defender for Cloud
**Incident Type:** Implementation

## Scenario / Query
A security administrator deployed Microsoft Defender for Cloud on a new Azure subscription but the Secure Score remains at 0% and no recommendations appear. What configuration step was missed?

## Environment Context
- **Tenant Type:** Enterprise (Azure AD tenant with multiple subscriptions)
- **Configuration:** Subscription is enrolled in Microsoft Defender for Cloud (formerly Azure Security Center) but the 'Defender plans' are not enabled for any resource type.

## Symptoms
- Secure Score shows 0%
- Recommendations blade is empty
- No security alerts are generated
- Inventory blade shows no resources

## Error Codes
N/A

## Root Causes
1. Microsoft Defender for Cloud requires at least one Defender plan to be enabled (e.g., Defender for Servers, Defender for Storage) to begin assessing resources and generating recommendations.
2. The subscription was onboarded to Defender for Cloud without enabling any Defender plans, leaving it in a 'free' foundational state that does not produce a Secure Score or recommendations.

## Remediation Steps
1. Navigate to Microsoft Defender for Cloud > Environment settings > Select the subscription.
2. Under 'Defender plans', toggle on the plans relevant to your workloads (e.g., Defender for Servers, Defender for Storage, Defender for SQL).
3. Click 'Save' and wait up to 24 hours for the Secure Score and recommendations to populate.

## Validation
After enabling at least one Defender plan, the Secure Score should update to a non-zero value and recommendations should appear within 24 hours. You can also run the Azure CLI command 'az security pricing show --name VirtualMachines' to verify the pricing tier is 'Standard'.

## Rollback
To disable a Defender plan, navigate to the same Defender plans blade and toggle the plan off, then click 'Save'. Note that this will stop security monitoring for that resource type.

## References
- Microsoft Learn: 'Enable Microsoft Defender for Cloud on your Azure subscription' - https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security
