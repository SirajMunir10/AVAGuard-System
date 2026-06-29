# Troubleshooting: iOS Enrollment (XPC_TYPE_ERROR Connection invalid)

**Domain:** Intune
**Subdomain:** iOS Enrollment
**Incident Type:** Troubleshooting

## Scenario / Query
ADE-managed device enrollment fails with XPC_TYPE_ERROR Connection invalid

## Environment Context
- **Tenant Type:** Intune
- **Configuration:** ADE enrollment profile assigned to device

## Symptoms
- Enrollment fails when turning on an ADE-managed device
- Error message: XPC_TYPE_ERROR Connection invalid
- Log entry: mobileassetd[83] <Notice>: 0x1a49aebc0 Client connection: XPC_TYPE_ERROR Connection invalid <error: 0x1a49aebc0> { count = 1, transaction: 0, voucher = 0x0, contents = "XPCErrorDescription" => <string: 0x1a49aee18> { length = 18, contents = "Connection invalid" } }
- Log entry: iPhone mobileassetd[83] <Notice>: Client connection invalid (Connection invalid); terminating connection
- Log entry: iPhone com.apple.accessibility.AccessibilityUIServer(MobileAsset)[288] <Notice>: [MobileAssetError:29] Unable to copy asset information from https://mesu.apple.com/assets/ for asset type com.apple.MobileAsset.VoiceServices.CombinedVocalizerVoices

## Error Codes
- `XPC_TYPE_ERROR Connection invalid`
- `MobileAssetError:29`

## Root Causes
1. Connection issue between the device and the Apple ADE service

## Remediation Steps
1. Fix the connection issue
2. Use a different network connection to enroll the device
3. Contact Apple if the issue persists

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/mem/intune/enrollment/troubleshoot-ios-enrollment-errors>
