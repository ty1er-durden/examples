import threading
import logging
import os
import time

logger = logging.getLogger(__name__)


def report_progress(path: str):
    """ Generates log message to track progress """
    size_kb = os.stat(path).st_size / 1024
    logger.info(f"Download in progress ({size_kb:.2f}KB downloaded)...")


def download_with_progress(fn, *args, update_frequency: int = 10):
    """ Periodically provides feed back to indicate to user that download is progressing"""
    progress = threading.Event()
    logger.info(f"Executing {fn.__name__}")
    thr = threading.Thread(target=fn, args=(*args,))
    logger.info("Download started")
    thr.start()
    while thr.isAlive():
        progress.wait(update_frequency)
        report_progress(*args)
    logger.info("Download completed")


def download(*args):
    """ Placeholder function for actual code to perform the download"""
    logger.info(f"Simulating download to location '{args[0]}'")
    time.sleep(5)


if __name__ == "__main__":

    # Configure logging
    formatter = logging.Formatter(
        "%(asctime)s @ %(name)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
    )
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.setLevel(logging.INFO)

    dest_path = os.path.abspath(__file__)
    download_with_progress(download, dest_path, update_frequency=1)
