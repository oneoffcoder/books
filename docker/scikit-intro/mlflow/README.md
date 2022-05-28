```bash
docker build --no-cache -t mlflow-server:local .

docker run --rm -v `pwd`/mlflow:/mlflow/ -v /tmp/mlflow:/tmp/mlflow -p 5001:5000 mlflow-server:local
docker run --rm -p 5001:5000 mlflow-server:local
```
