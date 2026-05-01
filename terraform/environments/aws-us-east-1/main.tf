module "eks_cluster" {
  source = "../../../modules/k8s"
  region = "aws-us-east-1"
  node_count = 311
}
