terraform {
  backend "s3" {
    bucket  = "enter your bucket name"
    key     = "myWebsite-ecs.tfstate"
    region  = "us-east-1"
    profile = "enter your profile name"
  }
}