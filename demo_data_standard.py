from RCPython.Client import Client
import os
import json

if __name__ == '__main__':
    client = Client(
        host="localhost:9081",
        pem_path=os.path.join("RCPython", "certs", "121000005l35120456.node1.pem"),
    )
    trans = client.create_trans_invoke(
        "",
        "ContractDump",
        1,
        "putProof",
        json.dumps({"wtf": "no_arg"}, ensure_ascii=False),
    )
    tx = json.loads(client.postTranByString(trans).text)
    print(tx)
