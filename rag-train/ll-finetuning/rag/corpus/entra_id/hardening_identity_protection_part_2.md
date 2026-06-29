# Hardening: Identity Protection

**Domain:** Entra ID
**Subdomain:** Identity Protection
**Incident Type:** Hardening

## Scenario / Query
How to mitigate future risks by adding corporate VPNs and IP address ranges to named locations in Conditional Access policies to reduce false positives?

## Environment Context
- **Tenant Type:** Entra ID tenant with Identity Protection enabled
- **Configuration:** Conditional Access policies with named locations

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Add corporate VPNs and IP address ranges to named locations in your Conditional Access policies to reduce false positives.
2. Consider creating a known traveler database for updated organizational travel reporting and use it to cross-reference travel activity.
3. Provide feedback in ID Protection to improve detection accuracy and reduce false positives.

## Validation
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator or Security Administrator. 2. Navigate to Protection > Conditional Access > Named locations. 3. Verify that the corporate VPN and IP address ranges are listed as an 'IP ranges location' with the correct CIDR notation. 4. Navigate to Protection > Conditional Access > Policies and select each policy that uses named locations. 5. Confirm that the 'Locations' condition includes the newly added named location and is set to 'Include' or 'Exclude' as intended. 6. Use the 'What If' tool for a test user connecting from a corporate VPN IP to verify the policy applies correctly. 7. In Identity Protection, navigate to Reports > Risky sign-ins and confirm that sign-ins from the added IP ranges are no longer flagged as risky (allow up to 24 hours for changes to propagate).

## Rollback
1. Sign in to the Microsoft Entra admin center as a Conditional Access Administrator or Security Administrator. 2. Navigate to Protection > Conditional Access > Named locations. 3. Select the named location containing the corporate VPN and IP address ranges. 4. Remove the IP ranges or delete the entire named location if it was created solely for this mitigation. 5. Navigate to Protection > Conditional Access > Policies and review each policy that referenced the removed location. 6. If the location was used in a policy condition, either remove the location condition or replace it with the previous named location configuration. 7. Save the policy changes and verify using the 'What If' tool that the policy behavior reverts to the original state.

## References
- <https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-investigate-risk>
