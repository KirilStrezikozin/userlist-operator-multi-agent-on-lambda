variable "aws_region" {
  description = "AWS region"
  type        = string
}

variable "userlist_operator_function_name" {
  description = "Name to use for the Lambda function"
  type        = string
  default     = "userlist_operator"
}

variable "userlist_operator_function_image_uri" {
  description = "Container image URI to use for the Lambda function"
  type        = string
}
