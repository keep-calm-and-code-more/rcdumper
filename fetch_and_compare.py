import base64
import requests
import jpype
import jpype.imports
from jpype.types import *

jpype.startJVM(classpath=['lib/*'])
from com.twitter.chill import KryoInjection


def invert(abytes):
    return KryoInjection.invert(abytes).get()


def parseFromResult(astring):
    return KryoInjection.invert(base64.b64decode(astring)).get()


def fetchSha256str(blocknum):
    url = "http://localhost:9081/block/{}".format(blocknum)
    r = requests.get(url)
    sha256str_in_base64 = r.json()["result"]["transactionResults"][0]["ol"][0][
        "newValue"
    ]
    return parseFromResult(sha256str_in_base64)


if __name__ == '__main__':
    r = fetchSha256str(2)
    print(r)
