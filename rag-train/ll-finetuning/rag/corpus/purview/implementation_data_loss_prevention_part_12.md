# Implementation: Data Loss Prevention

**Domain:** Purview
**Subdomain:** Data Loss Prevention
**Incident Type:** Implementation

## Scenario / Query
How to plan for Microsoft Purview Data Loss Prevention (DLP) by identifying stakeholders, describing categories of sensitive information to protect, and setting goals and strategy?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Microsoft Purview DLP

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Identify stakeholders
2. Describe the categories of sensitive information to protect
3. Set goals and strategy

## Validation
1. Confirm that the list of stakeholders is documented and includes representatives from legal, compliance, HR, IT security, and business units. 2. Verify that the categories of sensitive information (e.g., PII, financial data, IP) are defined and mapped to built-in or custom sensitive info types in the Microsoft Purview compliance portal. 3. Ensure that the goals and strategy (e.g., prevent data exfiltration, meet regulatory requirements) are recorded and aligned with the DLP policy creation workflow.

## Rollback
1. If stakeholder identification is incomplete, reconvene the planning team to add missing roles. 2. If sensitive info categories are incorrect, remove or modify the sensitive info types in the DLP policy draft before publishing. 3. If goals and strategy are misaligned, revise the policy objectives and update the policy configuration accordingly before any enforcement actions are taken.

## References
- <https://learn.microsoft.com/en-us/purview/dlp-policy-reference>
