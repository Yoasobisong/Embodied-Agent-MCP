module "eks_cluster" {
  source = "../../../modules/k8s"
  region = "gcp-asia-northeast1"
  node_count = 235
}
