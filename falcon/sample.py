# sample.py

import falcon

from prometheus_client import multiprocess, CollectorRegistry, generate_latest
from prometheus_client import Counter

# Sample prometheus counter
request_count = Counter('request_total', 'total number of http requests', ['method', 'endpoint'])

class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        request_count.labels('get', '/quote').inc()
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }

        resp.media = quote

class MetricsResource:
    def on_get(self, req, resp):
        """Handles GET requests
        Prometheus scraps metrics from this endpoint
        """
        request_count.labels('get', '/metrics').inc()
        registry = CollectorRegistry()
        multiprocess.MultiProcessCollector(registry)
        resp.body = generate_latest(registry)

api = falcon.API()
api.add_route('/quote', QuoteResource())
api.add_route('/metrics', MetricsResource())
