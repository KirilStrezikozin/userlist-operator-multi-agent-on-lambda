<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 1.2 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | ~> 5.92 |

## Providers

No providers.

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_userlist_operator_lambda"></a> [userlist\_operator\_lambda](#module\_userlist\_operator\_lambda) | ./modules/userlist_operator | n/a |

## Resources

No resources.

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_aws_region"></a> [aws\_region](#input\_aws\_region) | AWS region | `string` | n/a | yes |
| <a name="input_userlist_operator_function_image_uri"></a> [userlist\_operator\_function\_image\_uri](#input\_userlist\_operator\_function\_image\_uri) | Container image URI to use for the Lambda function | `string` | n/a | yes |
| <a name="input_userlist_operator_function_name"></a> [userlist\_operator\_function\_name](#input\_userlist\_operator\_function\_name) | Name to use for the Lambda function | `string` | `"userlist_operator"` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_userlist_operator_lambda_image_uri"></a> [userlist\_operator\_lambda\_image\_uri](#output\_userlist\_operator\_lambda\_image\_uri) | The ECR image URI for deploying Lambda |
| <a name="output_userlist_operator_lambda_name"></a> [userlist\_operator\_lambda\_name](#output\_userlist\_operator\_lambda\_name) | Name of the Lambda function. |
<!-- END_TF_DOCS -->