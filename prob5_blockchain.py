import hashlib
import time
import json
import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []

    def add_data(self, data):
        timestamp = get_current_gmt()
        previous_hash = 0
        if len(self.chain):
            previous_hash = self.chain[-1].hash
        block = Block(timestamp=timestamp, data=data, previous_hash=previous_hash)
        self.chain.append(block)


def get_current_gmt():
    gmt_time = datetime.datetime.fromtimestamp(time.mktime(time.gmtime()))
    return gmt_time.isoformat()


bc = Blockchain()
bc.add_data("Alice pays Bob 0.001 BTC")
bc.add_data("Bob pays Charlie 0.023 BTC")
