# TEST LOCAL

```bash
cd git_service/pr/
python3 app.py
```


## Push on ECR.

```bash
docker build -t 259941133233.dkr.ecr.us-west-2.amazonaws.com/ecr-git-pull-request:latest --no-cache -f Dockerfile .
aws --profile develop_smarty ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 259941133233.dkr.ecr.us-west-2.amazonaws.com | 
docker push 259941133233.dkr.ecr.us-west-2.amazonaws.com/ecr-git-pull-request:latest
```

## Lambda Terraform Deploy.

```bash
terraform init
terraform plat -out plan.tfplan
terraform apply
```


