resource "aws_iam_role" "userlist_operator" {
  name = "userlist_operator_lambda_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Sid    = ""
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "userlist_operator_lambda_basic" {
  role       = aws_iam_role.userlist_operator.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_policy" "userlist_operator_lambda_bedrock" {
  name = "userlist_operator_bedrock_policy"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ]
      Effect   = "Allow"
      Resource = "*"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "userlist_operator_lambda_bedrock" {
  role       = aws_iam_role.userlist_operator.name
  policy_arn = aws_iam_policy.userlist_operator_lambda_bedrock.arn
}
