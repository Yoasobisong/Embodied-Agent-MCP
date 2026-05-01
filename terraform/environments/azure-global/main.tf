module "eks_cluster" {
  source = "../../../modules/k8s"
  region = "azure-global"
  node_count = 213
}
