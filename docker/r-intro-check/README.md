# r-intro-check

This image exists only to execute the `sphinx/r-intro` notebooks end-to-end.

It is intentionally separate from the legacy `docker/r-intro` Jupyter image:

- smaller package surface
- current package install path
- deterministic notebook execution
- no dependency on the historical `oneoffcoder/book-r-intro` image

Current pinned runtime:

- `R 4.5.3`
- `JupyterLab 4.5.6`
