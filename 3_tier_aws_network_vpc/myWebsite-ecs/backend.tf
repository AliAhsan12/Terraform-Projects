terraform {
  backend "s3" {
    bucket  = "myawsbucket-00123"
    key     = "myWebsite-ecs.tfstate"
    region  = "us-east-1"
    profile = "terraform-user"
  }
}