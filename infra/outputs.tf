output "userlist_operator_lambda_name" {
  description = "Name of the Lambda function."
  value       = module.userlist_operator_lambda.function_name
}

output "userlist_operator_lambda_image_uri" {
  description = "The ECR image URI for deploying Lambda"
  value       = module.userlist_operator_lambda.image_uri
}
