# Info

To run on Windows.

```bash
docker run -it ^
    -p 8888:8888 ^
    -v %systemdrive%%homepath%\git\books\sphinx\r-intro\source:/root/ipynb ^
    oneoffcoder/book-r-intro:latest
```