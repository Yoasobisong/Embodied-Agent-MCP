module "eks_cluster" {
  source = "../../../modules/k8s"
  region = "aws-eu-west-1"
  node_count = 284
}
