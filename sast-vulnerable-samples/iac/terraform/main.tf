provider "aws" {
  region = "us-east-1"
}

resource "aws_security_group" "open_ssh" {
  name        = "open-ssh"
  description = "Allows SSH from anywhere (insecure)"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_s3_bucket" "public_bucket" {
  bucket = "sast-vulnerable-public-bucket"
  acl    = "public-read"

  versioning {
    enabled = false
  }
  server_side_encryption_configuration {}
}


