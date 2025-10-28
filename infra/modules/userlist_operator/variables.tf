variable "function_name" {
  description = "Name to use for the Lambda function"
  type        = string
  default     = "userlist_operator"
}

variable "function_architecture" {
  description = "Lambda function architecture (arm64 or x86_64)"
  type        = string
  default     = "arm64"
}

variable "function_image_uri" {
  description = "Container image URI to use for the Lambda function"
  type        = string
}

variable "cloudwatch_logs_retention_in_days" {
  description = "The number of days you want to retain log events. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, and 3653."
  type        = number
  default     = 30
}
