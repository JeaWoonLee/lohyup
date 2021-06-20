import json

import requests


def post_https_doc(ref):
    r = requests.post(ref)
    print(r.text)
    return r

