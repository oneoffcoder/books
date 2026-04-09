# scikit-intro-check

This image exists only to execute the `sphinx/scikit-intro` notebooks with nbconvert.

It is intentionally separate from any interactive authoring image:

- runs the public notebooks in Python 3.13
- installs the current notebook dependency set from `sphinx/scikit-intro/pyproject.toml`
- includes `R` so the `rpy2` notebook can execute
- writes executed notebooks to `sphinx/scikit-intro/build/executed-notebooks`
- mounts a persistent cache at `sphinx/scikit-intro/build/notebook-cache`
- keeps the book source mounted read-only

## Execute

Run every public notebook:

```bash
docker/scikit-intro-check/execute-notebooks.sh
```

Run selected notebooks:

```bash
docker/scikit-intro-check/execute-notebooks.sh regression.ipynb tips.ipynb
```

The wrapper defaults `SCIKIT_INTRO_CHECK_MODE=1`, which swaps in local fallback datasets for the largest remote examples. Use the full remote paths with:

```bash
SCIKIT_INTRO_CHECK_MODE=0 SCIKIT_INTRO_RUN_REMOTE_DATASETS=1 docker/scikit-intro-check/execute-notebooks.sh generate-samples.ipynb gensim.ipynb
```
