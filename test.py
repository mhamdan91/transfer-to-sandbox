import time, sys
import logging
log = logging.getLogger(__name__)
def _sleep(sleep_time: int) -> None:
    while sleep_time > 0:
        time.sleep(1)
        sleep_time -= 10
#         msg = f'\r {sleep_time} remaining seconds before resuming auditing...'
#         sys.stdout.write(msg)
#         sys.stdout.flush()
        log.info("%s remaining seconds before resuming auditing...", sleep_time)
        print(f"{sleep_time} remaining seconds before resuming auditing......")
_sleep(65)
