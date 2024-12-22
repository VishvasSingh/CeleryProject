from tasks import celery_app  # Import your Celery app instance
import sys
import logging as logger

if __name__ == "__main__":
    queue_name = "default"

    # Check if a queue name was passed as a script parameter
    if len(sys.argv) > 1:
        queue_name = sys.argv[1]

    logger.info(f"Starting Celery worker for queue: {queue_name}")

    celery_app.worker_main(
        argv=[
            "worker",
            "--loglevel=info",  # Set your desired log level
            "--concurrency=5",  # Optional: Adjust concurrency for debugging
            f"--queues={queue_name}"
        ]
    )