# Implementation: UEBA Enrichments

**Domain:** Sentinel
**Subdomain:** UEBA Enrichments
**Incident Type:** Implementation

## Scenario / Query
How to configure UEBA enrichments in Microsoft Sentinel for Okta and Windows Security Events?

## Environment Context
- **Tenant Type:** Azure
- **Configuration:** Microsoft Sentinel workspace with UEBA enabled

## Symptoms
N/A

## Error Codes
N/A

## Root Causes
N/A

## Remediation Steps
1. Ensure the following Google Cloud APIs are enabled: apigee.googleapis.com, iam.googleapis.com, iamcredentials.googleapis.com, cloudresourcemanager.googleapis.com, compute.googleapis.com, storage.googleapis.com, container.googleapis.com, cloudsql.googleapis.com, bigquery.googleapis.com, bigquerydatatransfer.googleapis.com, cloudfunctions.googleapis.com, appengine.googleapis.com, dns.googleapis.com, bigquerydatapolicy.googleapis.com, firestore.googleapis.com, dataproc.googleapis.com, osconfig.googleapis.com, cloudkms.googleapis.com, secretmanager.googleapis.com
2. For Okta Single Sign-On (Preview), use Azure Functions to collect Okta_CL and OktaV2_CL logs including authentication, MFA, and session events such as: app.oauth2.admin.consent.grant_success, app.oauth2.authorize.code_success, device.desktop_mfa.recovery_pin.generate, user.authentication.auth_via_mfa, user.mfa.attempt_bypass, user.mfa.factor.deactivate, user.mfa.factor.reset_all, user.mfa.factor.suspend, user.mfa.okta_verify, user.session.impersonation.grant, user.session.impersonation.initiate, user.session.start
3. Ensure Okta events have a valid User ID (actor_id_s)
4. For Windows Security Events, use the AMA (Azure Monitor Agent) to forward WindowsEvent logs including: 4624 (An account was successfully logged on), 4625 (An account failed to log on), 4648 (A logon was attempted using explicit credentials), 4672 (Special privileges assigned to new logon), 4688 (A new process has been created)
5. For Microsoft Entra ID, collect all sign-in events

## Validation
1. In the Microsoft Sentinel workspace, navigate to Entity behavior > Entity behavior settings and confirm UEBA is enabled. 2. Verify that the following Google Cloud APIs are enabled in the Google Cloud project: apigee.googleapis.com, iam.googleapis.com, iamcredentials.googleapis.com, cloudresourcemanager.googleapis.com, compute.googleapis.com, storage.googleapis.com, container.googleapis.com, cloudsql.googleapis.com, bigquery.googleapis.com, bigquerydatatransfer.googleapis.com, cloudfunctions.googleapis.com, appengine.googleapis.com, dns.googleapis.com, bigquerydatapolicy.googleapis.com, firestore.googleapis.com, dataproc.googleapis.com, osconfig.googleapis.com, cloudkms.googleapis.com, secretmanager.googleapis.com. 3. For Okta, confirm that the Azure Function app is deployed and collecting Okta_CL and OktaV2_CL logs. Run a sample query: `Okta_CL | take 10` and verify events include authentication, MFA, and session events such as app.oauth2.admin.consent.grant_success, app.oauth2.authorize.code_success, device.desktop_mfa.recovery_pin.generate, user.authentication.auth_via_mfa, user.mfa.attempt_bypass, user.mfa.factor.deactivate, user.mfa.factor.reset_all, user.mfa.factor.suspend, user.mfa.okta_verify, user.session.impersonation.grant, user.session.impersonation.initiate, user.session.start. 4. Check that Okta events contain a valid User ID in the actor_id_s field: `Okta_CL | where isnotempty(actor_id_s) | take 10`. 5. For Windows Security Events, verify the Azure Monitor Agent (AMA) is installed on source machines and forwarding events 4624, 4625, 4648, 4672, 4688. Run: `WindowsEvent | where EventID in (4624,4625,4648,4672,4688) | take 10`. 6. For Microsoft Entra ID, confirm sign-in logs are collected: `SigninLogs | take 10`.

## Rollback
1. Disable UEBA in the Sentinel workspace: In Entity behavior settings, toggle UEBA off. 2. Disable the Google Cloud APIs that were enabled for the integration (list each API individually). 3. Remove or disable the Azure Function app collecting Okta logs. 4. Remove the Okta data connector from Sentinel. 5. Uninstall the Azure Monitor Agent from Windows machines or remove the WindowsEvent data collection rule that forwards events 4624,4625,4648,4672,4688. 6. Disable the Microsoft Entra ID connector for sign-in logs in Sentinel.

## References
- <https://learn.microsoft.com/en-us/azure/sentinel/ueba-enrichments>
