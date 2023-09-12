#############################################################################
# LAMBDA GIT PULL REQUEST
#############################################################################

module "lambda_git_pull_request_container_image" {
  source = "github.com/terraform-aws-modules/terraform-aws-lambda.git"

  function_name = "lambda-git-pull-request"
  description   = "My awesome lambda function from container image"
  create_package = false
  image_uri     = "${aws_ecr_repository.service.repository_url}:latest" 
  package_type  = "Image"
  architectures = ["x86_64"]
}