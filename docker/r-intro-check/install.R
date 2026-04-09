options(
  repos = c(CRAN = "https://cloud.r-project.org"),
  Ncpus = max(1L, parallel::detectCores() - 1L)
)

install.packages(
  c(
    "IRkernel",
    "dplyr",
    "purrr",
    "tidyr",
    "microbenchmark",
    "missForest",
    "VIM",
    "pROC",
    "randomForest",
    "e1071",
    "cluster",
    "fpc",
    "mclust",
    "comprehenr",
    "readr",
    "ggplot2",
    "maps",
    "mapproj",
    "repr",
    "ggthemes",
    "ggrepel",
    "gridExtra",
    "mice",
    "Amelia",
    "Hmisc",
    "mi",
    "R6",
    "caret",
    "skimr",
    "RANN",
    "PRROC"
  ),
  dependencies = c("Depends", "Imports", "LinkingTo")
)

install.packages(
  "https://cran.r-project.org/src/contrib/Archive/fastAdaboost/fastAdaboost_1.0.0.tar.gz",
  repos = NULL,
  type = "source"
)

IRkernel::installspec(user = FALSE, name = "ir", displayname = "R")
