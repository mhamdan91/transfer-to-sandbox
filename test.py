import time, sys
import logging
import json
import requests
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

def _get_rate_limit():
    r = requests.get(f'https://token:{str(sys.argv[1])}@api.github.com/rate_limit')
    r_data = json.loads(r.text)['resources']['core']
    return r_data['used'], r_data['remaining'], r_data['reset']
print(_get_rate_limit())
