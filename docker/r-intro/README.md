# Info

To run on Windows.

```bash
docker run -it ^
    -p 8888:8888 ^
    -v %systemdrive%%homepath%\git\books\sphinx\r-intro\source:/root/ipynb ^
    -e NOTEBOOK_PASSWORD=sha1:6676da7235c8:9c7d402c01e330b9368fa9e1637233748be11cc5 ^
    oneoffcoder/book-r-intro:latest
```