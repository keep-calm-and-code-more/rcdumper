import json
import shutil
from pathlib import Path
import os
import hashlib
import plyvel
import base64
from fetch_and_compare import fetchSha256str, invert


if __name__ == '__main__':
    localpath = os.path.join(".", "lvdb")
    try:
        shutil.rmtree(localpath)
    except:
        print("lvdb folder not exist.")
    Path(localpath).mkdir(parents=True, exist_ok=True)
    dirpath = "/Users/fang/rcworkspace/repchain_1.3.1/repchaindata/data/leveldbdata/121000005l35120456.node1"
    basename = os.path.basename(dirpath)
    shutil.copytree(dirpath, os.path.join(localpath, basename), dirs_exist_ok=True)
    db = plyvel.DB('lvdb/121000005l35120456.node1')
    val_should_fetch = fetchSha256str(2)
    print(val_should_fetch)
    itrt = db.iterator(prefix=b'c_ContractAssetsTPL_')
    loong = bytearray()
    dump_dict = {}
    for key, value in itrt:
        loong += key
        loong += value
        dump_dict[key.decode("ascii")] = invert(value)
        print(key, invert(value), type(invert(value)))
    r = base64.b64encode((hashlib.sha256(loong).digest())).decode('ascii')
    print(r)
    print("equal??? {}".format(val_should_fetch == r))
    jsonstr = json.dumps(
        dump_dict,
        sort_keys=True,
        ensure_ascii=False,
        default=str,
        separators=(',', ':'),
    )
    print(jsonstr)
    with open("tpldump.json", "w") as f:
        f.write(jsonstr)
