terraform {
  required_version = ">= 1.6"
  required_providers {
    aws = { source = "hashicorp/aws", version = "~> 5.40" }
  }
}

provider "aws" {
  region = var.region
}

resource "aws_s3_bucket" "invoice_uploads" {
  bucket = "${var.environment}-supplier-invoice-uploads"
  tags = { project = "supplier-portal", environment = var.environment }
}

resource "aws_cloudfront_distribution" "portal" {
  enabled = true
  origin {
    domain_name = var.api_origin
    origin_id   = "supplier-api"
    custom_origin_config {
      http_port  = 80
      https_port = 443
      origin_protocol_policy = "https-only"
      origin_ssl_protocols   = ["TLSv1.2"]
    }
  }
  default_cache_behavior {
    viewer_protocol_policy = "redirect-to-https"
    target_origin_id       = "supplier-api"
    allowed_methods        = ["GET", "HEAD", "OPTIONS", "POST"]
    cached_methods         = ["GET", "HEAD"]
    forwarded_values { query_string = true }
  }
}
