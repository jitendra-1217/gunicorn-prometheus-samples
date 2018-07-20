# gunicorn-prometheus-samples

## falcon framework

### Setup

```sh
# Switch to this directory (/gunicorn-prometheus-samples/falcon)
# Setup virtual environment
virtualenv venv
source venv/bin/activate
# Installs requirements
pip install -r req.lock
# Run gunicorn app with following options
gunicorn --workers=5 \
    --bind=0.0.0.0:8084 \
    --env prometheus_multiproc_dir=prom-metrics-dir \
    --config=gunicorn.conf.py \
    sample:api
```

### References

- https://github.com/prometheus/client_python#multiprocess-mode-gunicorn
