<h1 align="center">FastAPI + Prometheus + Grafana :tada:</h1>

This is a minimal setup that you can build to monitor your FastAPI microservice.

## Usage

You'll need to run the docker containers:

``` bash
docker compose up
```

Now you have access to those three containers and their respective ports:

* Prometheus: http://localhost:9090/
* Grafana: http://localhost:3000/
* FastAPI: http://localhost:8000/

On the FastAPI, you can access `/metrics` endpoint to see the data Prometheus is scraping from it.


## References

* [Prometheus FastAPI Instrumentator](https://github.com/trallnag/prometheus-fastapi-instrumentator)
* [Generate and Track Metrics for Flask API Applications Using Prometheus and Grafana](https://medium.com/swlh/generate-and-track-metrics-for-flask-api-applications-using-prometheus-and-grafana-55ddd39866f0)
* [PromQL for Humans](https://timber.io/blog/promql-for-humans/)

## Resources
- [loguru](https://signoz.io/guides/loguru/)
- [loki+docker](https://abhiraj2001.medium.com/monitoring-docker-containers-with-grafana-loki-and-promtail-4302a9417c0d)

# Installation du plugin docker pour Loki
- `docker plugin install grafana/loki-docker-driver:2.9.1 --alias loki --grant-all-permissions`
- Collez ce json dans `~/.docker/daemon.json`:
```json
{
    "log-driver": "loki",
    "log-opts": {
        "loki-url": "http://localhost:3100/loki/api/v1/push",
        "loki-batch-size": "400"
    }
}
```