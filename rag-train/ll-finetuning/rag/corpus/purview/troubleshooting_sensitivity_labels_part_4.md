# Troubleshooting: Sensitivity Labels (CannotOverrideCurrentLabel)

**Domain:** Purview
**Subdomain:** Sensitivity Labels
**Incident Type:** Troubleshooting

## Scenario / Query
How to troubleshoot failures when applying, changing, or removing sensitivity labels based on FailureReason values in the Microsoft 365 audit log?

## Environment Context
- **Tenant Type:** Microsoft 365
- **Configuration:** Sensitivity labels configured in Microsoft Purview compliance portal

## Symptoms
- Sensitivity label not assigned to file
- Audit log shows FailureReason property with specific error code

## Error Codes
- `CannotOverrideCurrentLabel`
- `DowngradeJustificationTextMissing`
- `FileEncrypted`
- `FileExtensionNotSupported`
- `FileLockedOrCheckedOut`
- `FileNotFound`
- `FileNotSupported`
- `FileTooLarge`
- `InvalidArgument`
- `LabelIdNotFound`
- `LabelNotSupported`
- `LabelOperationsDisabled`
- `MinorVersionLimitExceeded`
- `UnauthorizedAccessException`
- `ZeroByteFileError`

## Root Causes
1. Currently applied sensitivity label has a higher priority
2. Justification text is required for the operation
3. File is encrypted
4. File type is not supported for the operation
5. File is locked or checked out
6. File is not available
7. File does not support the operation
8. File is too large to support the operation
9. Invalid parameters provided for the operation
10. Sensitivity label provided is unavailable or not valid
11. Sensitivity label provided is not supported
12. Sensitivity label operation is disabled on the file
13. Version limit is exceeded
14. Current user is not authorized to perform the operation
15. Operation cannot be performed on a zero-byte file

## Remediation Steps
1. Check the FailureReason property in the audit log for the specific error code
2. For CannotOverrideCurrentLabel: Ensure the label being applied has higher priority than the current label
3. For DowngradeJustificationTextMissing: Provide justification text when required
4. For FileEncrypted: Decrypt the file before applying the label
5. For FileExtensionNotSupported: Use a supported file type
6. For FileLockedOrCheckedOut: Unlock or check in the file
7. For FileNotFound: Ensure the file is available
8. For FileNotSupported: Use a file that supports the operation
9. For FileTooLarge: Reduce file size
10. For InvalidArgument: Correct the parameters provided
11. For LabelIdNotFound: Verify the sensitivity label is available and valid
12. For LabelNotSupported: Use a supported sensitivity label
13. For LabelOperationsDisabled: Enable label operations on the file
14. For MinorVersionLimitExceeded: Reduce version count
15. For UnauthorizedAccessException: Grant appropriate permissions to the user
16. For ZeroByteFileError: Add content to the file before applying the label

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/purview/audit-log-activities>
