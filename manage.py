import redis
from rq import Connection, Worker
from flask.cli import FlaskGroup

from src.server import create_app

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command()
def run_worker():
  """Run the worker. Assumes existence of a Redis server (set up in Docker for this project)"""
  redis_url = app.config['REDIS_URL']
  redis_connection = redis.from_url(redis_url)
  with Connection(redis_connection):
    worker = Worker(app.config['QUEUES'])
    worker.work()

if __name__ == '__main__':
  cli()
