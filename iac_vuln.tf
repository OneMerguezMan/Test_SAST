# iac_vuln.tf
# Vulnérabilité : S3 bucket public
resource "aws_s3_bucket" "bad_bucket" {
  bucket = "my-insecure-bucket"
  acl    = "public-read" # Vulnérabilité : accès public
} 
