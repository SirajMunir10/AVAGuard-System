# Troubleshooting: Information Barriers

**Domain:** Purview
**Subdomain:** Information Barriers
**Incident Type:** Troubleshooting

## Scenario / Query
How do I determine which segments are included in an Information Barriers policy?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Information Barriers policies configured

## Symptoms
- Users may be blocked from communicating with certain segments

## Error Codes
N/A

## Root Causes
1. Information Barriers policy may be blocking communication as intended
2. Policy may need refinement

## Remediation Steps
1. Use the Get-InformationBarrierPolicy cmdlet together with the Identity parameter. Syntax: Get-InformationBarrierPolicy -Identity <policy GUID>.
2. Use details, such as the policy GUID (ExoPolicyId) you received during the previous step, as an identity value.
3. Example: Get-InformationBarrierPolicy -Identity b42c3d0f-xyxy-4506-xyxy-bf2853b5df6f. This example provides detailed information about the Information Barriers policy that has ExoPolicyId b42c3d0f-xyxy-4506-xyxy-bf2853b5df6f.
4. After you run the cmdlet, examine the results for AssignedSegment, SegmentsAllowed, and SegmentsBlocked values. For example, after you run the Get-InformationBarrierPolicy cmdlet, you see the following in the results: AssignedSegment : Sales, SegmentsAllowed : {}, SegmentsBlocked : {Research}. In this case, you can see that an Information Barriers policy affects people who are in the Sales and Research segments. People in Sales are prevented from communicating with people in Research. If this seems correct, then the information barriers are working as expected. If not, go to the next step.

## Validation
Run the Get-InformationBarrierPolicy cmdlet with the Identity parameter set to the policy GUID (ExoPolicyId). For example: Get-InformationBarrierPolicy -Identity b42c3d0f-xyxy-4506-xyxy-bf2853b5df6f. Examine the output for the AssignedSegment, SegmentsAllowed, and SegmentsBlocked fields. Confirm that the segments listed match the intended policy configuration. If the policy is blocking communication as expected, the validation is successful.

## Rollback
If the policy is not working as intended, refine the policy by using the Set-InformationBarrierPolicy cmdlet to adjust the SegmentsAllowed or SegmentsBlocked values, or remove the policy using Remove-InformationBarrierPolicy. Then reapply the policy using Start-InformationBarrierPoliciesApplication. Refer to the official documentation for exact cmdlet syntax and parameters.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/information-barriers-troubleshooting>
