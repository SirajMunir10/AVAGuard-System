# Troubleshooting: Azure Resource Manager (Template validation failed: Could not find member 'parameterss' on object of type 'Template'. Path 'parameterss', line 4, position 16)

**Domain:** Azure
**Subdomain:** Azure Resource Manager
**Incident Type:** Troubleshooting

## Scenario / Query
How to fix a validation error in an ARM template due to misspelled element name 'parameterss'?

## Environment Context
- **Tenant Type:** N/A
- **Configuration:** N/A

## Symptoms
- Wavy line under 'parameterss' in Visual Studio Code
- Validation error: 'Template validation failed: Could not find member 'parameterss' on object of type 'Template'. Path 'parameterss', line 4, position 16'
- Undefined parameter reference errors for variables and resources

## Error Codes
- `Template validation failed: Could not find member 'parameterss' on object of type 'Template'. Path 'parameterss', line 4, position 16`

## Root Causes
1. Incorrect spelling of element name 'parameterss' instead of 'parameters'

## Remediation Steps
1. Open the file in Visual Studio Code
2. Hover over the error to see the validation error
3. Select View > Problems to display the template's validation errors
4. Correct the spelling of 'parameterss' to 'parameters'
5. Save the file

## Validation
N/A

## Rollback
N/A

## References
- <https://learn.microsoft.com/en-us/azure/azure-resource-manager/troubleshooting/quickstart-troubleshoot-arm-deployment>
