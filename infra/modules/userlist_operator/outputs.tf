output "function_name" {
  description = "Name of the Lambda function."
  value       = aws_lambda_function.userlist_operator.function_name
}

output "image_uri" {
  description = "The ECR image URI for deploying Lambda"
  value       = aws_lambda_function.userlist_operator.image_uri
}
