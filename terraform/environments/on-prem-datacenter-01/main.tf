module "eks_cluster" {
  source = "../../../modules/k8s"
  region = "on-prem-datacenter-01"
  node_count = 285
}
