import time, sys

def _sleep(sleep_time: int) -> None:
    while sleep_time > 0:
        time.sleep(10)
        sleep_time -= 10
        msg = f'\r {sleep_time} remaining seconds before resuming auditing...'
        sys.stdout.write(msg)
        sys.stdout.flush()
_sleep(60)
