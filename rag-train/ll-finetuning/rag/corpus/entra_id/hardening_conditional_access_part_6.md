# Hardening: Conditional Access

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Hardening

## Scenario / Query
A tenant has no Conditional Access policies enforcing multifactor authentication for all users. What hardening steps should be taken to reduce the risk of credential theft?

## Environment Context
- **Tenant Type:** Production
- **Configuration:** No Conditional Access policies exist; all users can authenticate with password only.

## Symptoms
- No Conditional Access policies are configured in the Entra ID admin center.
- Users are not prompted for MFA during sign-in.
- Security defaults are disabled.

## Error Codes
N/A

## Root Causes
1. Conditional Access policies have never been created or assigned.
2. Security defaults were turned off without implementing custom policies.

## Remediation Steps
1. Create a Conditional Access policy named 'Require MFA for all users' with the following settings: Assignments > Users and groups > All users; Cloud apps or actions > All cloud apps; Conditions > None; Access controls > Grant > Require multifactor authentication; Enable policy > On.
2. Enable Security defaults if no custom Conditional Access policies are needed, by navigating to Entra ID > Properties > Manage Security defaults and setting 'Enable Security defaults' to Yes.

## Validation
After creating the policy, sign in as a test user and verify that MFA registration and authentication are required. Confirm the policy appears in the Conditional Access > Policies list with status 'On'.

## Rollback
Set the policy to 'Off' or delete it. If Security defaults were enabled, set 'Enable Security defaults' to No.

## References
- Microsoft Learn: Configure Conditional Access policies
- Microsoft Learn: What are security defaults?
