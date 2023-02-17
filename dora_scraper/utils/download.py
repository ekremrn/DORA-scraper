import os
import shutil
import socket
import requests

from time import sleep
from urllib.error import HTTPError
from urllib.request import urlretrieve

socket.setdefaulttimeout(5)


def download_image(source, target, delay=0.01):
    target_head, _ = os.path.split(target)
    if not os.path.exists(target_head):
        os.makedirs(target_head)
    elif os.path.exists(target):
        return True

    try:
        urlretrieve(source, target)
    except HTTPError as e:
        r = requests.get(source, stream=True)
        if r.status_code == 200:
            with open(str(target), "wb") as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
    except Exception as e:
        return False

    sleep(delay)
    return True
