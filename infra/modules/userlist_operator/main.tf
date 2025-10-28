data "aws_region" "current" {}


locals {
  function_timeout     = 15
  function_memory_size = 1024

  function_cloudwatch_group_name = "/aws/lambda/${aws_lambda_function.userlist_operator.function_name}"
}

resource "aws_lambda_function" "userlist_operator" {
  function_name = var.function_name

  architectures = [var.function_architecture]
  package_type  = "Image"

  timeout     = local.function_timeout
  memory_size = local.function_memory_size

  role = aws_iam_role.userlist_operator.arn

  image_uri = var.function_image_uri
}


resource "aws_cloudwatch_log_group" "lambda" {
  name              = local.function_cloudwatch_group_name
  retention_in_days = var.cloudwatch_logs_retention_in_days
}
