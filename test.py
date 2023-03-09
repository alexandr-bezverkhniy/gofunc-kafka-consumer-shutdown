import json
import random
import subprocess
import argparse
import time

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='test', description='Run test publisher')
    parser.add_argument('-c','--count', type=int, default=5)
    args = parser.parse_args()

    for i in range(args.count):
        order_id = random.randint(1000, 9999)
        data = json.dumps({"order-id": order_id, "num": i})
        print(f"DATA: '{data}'")
        subprocess.run(["httpx", "-f", "httpbin.http", "kafka-pub", "--data", data])
        sleep_time = random.uniform(0.5, 1)
        time.sleep(sleep_time)