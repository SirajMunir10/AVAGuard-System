# Troubleshooting: Conditional Access (DeviceNotCompliant)

**Domain:** Entra ID
**Subdomain:** Conditional Access
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot common Conditional Access error codes such as DeviceNotCompliant, DeviceNotDomainJoined, ApplicationUsedIsNotAnApprovedApp, BlockedByConditionalAccess, ProofUpBlockedDueToRisk, and Application needs to enforce Intune protection policies?

## Environment Context
- **Tenant Type:** Microsoft Entra ID
- **Configuration:** Conditional Access policies

## Symptoms
- Access blocked or restricted by Conditional Access policy
- Error code displayed in browser with AADSTS prefix

## Error Codes
- `DeviceNotCompliant`
- `DeviceNotDomainJoined`
- `ApplicationUsedIsNotAnApprovedApp`
- `BlockedByConditionalAccess`
- `ProofUpBlockedDueToRisk`
- `Application needs to enforce Intune protection policies`
- `AADSTS53002`

## Root Causes
1. Device does not meet compliance requirements
2. Device is not domain joined
3. Application used is not an approved app
4. Access blocked by Conditional Access policy
5. Proof-up blocked due to user risk
6. Application requires Intune protection policies

## Remediation Steps
1. Review the specific error code in the browser (e.g., AADSTS53002)
2. Refer to Microsoft Entra authentication and authorization error codes documentation for detailed guidance

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access>
- <https://learn.microsoft.com/en-us/entra/identity/conditional-access/troubleshoot-conditional-access#common-conditional-access-error-codes>
