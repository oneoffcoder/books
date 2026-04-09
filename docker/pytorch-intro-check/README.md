# pytorch-intro-check

This image exists only to execute the `sphinx/pytorch-intro` notebooks with nbconvert.

It is intentionally separate from the legacy `docker/pytorch-intro-gpu` Jupyter image:

- runs notebooks in a Python 3.13 CUDA-enabled PyTorch container
- requests Docker GPU access with `--gpus all`
- fails before notebook execution if PyTorch cannot see CUDA
- writes executed notebooks to `sphinx/pytorch-intro/build/executed-notebooks`
- mounts a persistent data / `TORCH_HOME` cache at `sphinx/pytorch-intro/build/notebook-cache`
- keeps the book source mounted read-only
- fails fast when a selected notebook raises an exception

## Build

```bash
docker build -t book-pytorch-intro-check:local docker/pytorch-intro-check
```

## Execute

Run every public notebook:

```bash
docker/pytorch-intro-check/execute-notebooks.sh
```

Run selected notebooks:

```bash
docker/pytorch-intro-check/execute-notebooks.sh environment.ipynb tensor.ipynb
```

Run on a CPU-only Docker host:

```bash
DOCKER_GPUS= PYTORCH_INTRO_REQUIRE_CUDA=0 docker/pytorch-intro-check/execute-notebooks.sh tensor.ipynb
```

The wrapper defaults `PYTORCH_INTRO_CHECK_MODE=1` so expensive architecture-tour cells can take a lightweight checker path. Use the full book behavior for selected notebooks with:

```bash
PYTORCH_INTRO_CHECK_MODE=0 docker/pytorch-intro-check/execute-notebooks.sh model.ipynb
```

Run notebooks with the optional remote dataset examples enabled:

```bash
PYTORCH_INTRO_RUN_REMOTE_DATASETS=1 docker/pytorch-intro-check/execute-notebooks.sh data.ipynb
```

## Dataset Cache

Predownload the smaller torchvision datasets used by the book:

```bash
docker/pytorch-intro-check/download-datasets.sh
```

Predownload selected supported datasets:

```bash
docker/pytorch-intro-check/download-datasets.sh mnist cifar10 usps
```

The download helper and the execution helper share `sphinx/pytorch-intro/build/notebook-cache` by default. Set `CACHE_DIR=/some/path` for a different cache location.
