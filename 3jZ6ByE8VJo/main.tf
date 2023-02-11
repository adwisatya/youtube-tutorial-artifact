terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "ap-southeast-1"
  skip_region_validation = true
}

resource "aws_instance" "app_server" {
  ami           = "ami-082b1f4237bd816a1"
  instance_type = "t2.micro"
  key_name = "singapore"
  user_data = <<EOF
#!/bin/bash
curl -O https://raw.githubusercontent.com/angristan/openvpn-install/master/openvpn-install.sh
chmod +x openvpn-install.sh
export IPV6_SUPPORT=n
export PORT_CHOICE=1
export PROTOCOL_CHOICE=1
export DNS=1
export ENDPOINT=`curl -4 ifconfig.me`
export COMPRESSION_ENABLED=n
export CUSTOMIZE_ENC=n
export CLIENT="${var.vpnuser}"
export PASS=1
export APPROVE_INSTALL=y
./openvpn-install.sh
mv /root/${var.vpnuser}.ovpn /home/ubuntu/
EOF
  tags = {
    Name = var.instance_name
  }
}

variable "instance_name" {
  description = "Value of the Name tag for the EC2 instance"
  type        = string
  default     = "OpenVPN-Server"
}
variable "vpnuser" {
  description = "Username for openvpn user"
  type        = string
}
output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.app_server.id
}

output "instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.app_server.public_ip
}


