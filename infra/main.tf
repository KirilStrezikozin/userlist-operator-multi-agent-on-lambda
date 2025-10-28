module "userlist_operator_lambda" {
  source             = "./modules/userlist_operator"
  function_image_uri = var.userlist_operator_function_image_uri
  function_name      = var.userlist_operator_function_name
}
