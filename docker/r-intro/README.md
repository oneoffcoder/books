# Info

To run on Windows.

```bash
docker run -it ^
    -p 8888:8888 ^
    -v %systemdrive%%homepath%\git\books\sphinx\r-intro\source:/root/ipynb ^
    oneoffcoder/book-r-intro:latest
```

# R Packages

[R package sources are available](http://cloud.r-project.org/src/).

Use [simple mass downloader](https://chrome.google.com/webstore/detail/simple-mass-downloader/abdkkegmcbiomijcbdaodaflgehfffed?hl=en-US) with Chrome to download all these packages. You can install packages [from local source](https://riptutorial.com/r/example/5556/install-package-from-local-source).