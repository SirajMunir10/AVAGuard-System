# Implementation: Communication Compliance

**Domain:** Purview
**Subdomain:** Communication Compliance
**Incident Type:** Implementation

## Scenario / Query
How to review Microsoft Teams meeting transcripts in Communication Compliance policies?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Teams meeting transcripts must be turned on for the organization

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Turn on meeting transcripts for your organization (not turned on by default).
2. Ensure Teams is selected as a Microsoft 365 location when creating a custom policy or using a template.
3. For scheduled (nonrecurring) meetings: Communication Compliance ignores communication direction and includes all meeting content if an in-scope user is an invitee or present.
4. For recurring meetings: Policy evaluates only users who were invited or identified by the transcript as having spoken.
5. For unscheduled (Meet now) meetings: Policy evaluates only users identified by the transcript as having spoken.
6. Set one or more of the following policy conditions: Content matches any of these classifiers, Content contains any of these sensitive info types, Message contains any of these words, Message contains none of these words. Other policy conditions are ignored.

## Validation
1. Verify that meeting transcripts are enabled for the organization by running: Get-CsTeamsMeetingPolicy -Identity Global | fl AllowTranscription. Ensure the value is True. 2. Confirm the Communication Compliance policy includes Teams as a location by running: Get-CommunicationCompliancePolicy -Identity "PolicyName" | fl Locations. Verify 'Teams' is listed. 3. For a scheduled meeting, check that an in-scope user was an invitee or presenter and that the policy condition (e.g., 'Content matches any of these classifiers') is set. 4. For a recurring meeting, verify that only invited or speaking users are evaluated by reviewing the policy's scope and the meeting transcript. 5. For an unscheduled meeting, confirm that only users identified by the transcript as having spoken are evaluated. 6. Ensure the policy condition is one of the supported types: 'Content matches any of these classifiers', 'Content contains any of these sensitive info types', 'Message contains any of these words', or 'Message contains none of these words'.

## Rollback
1. Disable meeting transcripts for the organization by running: Set-CsTeamsMeetingPolicy -Identity Global -AllowTranscription $false. 2. Remove Teams as a location from the Communication Compliance policy by running: Set-CommunicationCompliancePolicy -Identity "PolicyName" -RemoveLocation Teams. 3. If needed, revert to default policy conditions by clearing custom conditions or resetting the policy to a template without conditions. 4. For scheduled meetings, remove the in-scope user from the meeting invite or presenter list to exclude the meeting from policy evaluation. 5. For recurring meetings, remove the user from the meeting series invite or ensure they are not identified as a speaker in the transcript. 6. For unscheduled meetings, ensure the user is not identified as a speaker in the transcript.

## References
- <https://learn.microsoft.com/en-us/microsoft-365/compliance/communication-compliance-investigate-remediate>
