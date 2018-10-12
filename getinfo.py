# -*- coding: UTF-8 -*-

# Get head block id's last two digit
# as lucky number

import urllib.request
import json

url = 'http://api.eosnewyork.io/v1/chain/get_info'

def make_request():
    response = urllib.request.urlopen(url)
    info = response.read().decode('utf8', "ignore")
    return info

if __name__ == '__main__':
    while 1:
        info = make_request()
        resp = json.loads(info)
        hash = resp["head_block_id"]
        index = 63
        dst = ""
        while index:            
            c = hash[index]
            if c.isdigit():
                tmp = dst
                dst = c + tmp

            if len(dst) == 2:
                break
            index -= 1
        print("lucky number is: %s" % dst)
