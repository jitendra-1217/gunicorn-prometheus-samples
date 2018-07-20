# Configuration file for gunicorn, passed as file name argument when running gunicorn app

from prometheus_client import multiprocess

def child_exit(server, worker):
    # Prometheus marks each process dead on gunicorn worker exist
    multiprocess.mark_process_dead(worker.pid)
