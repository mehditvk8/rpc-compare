import random
import sys
from web3 import Web3

with open(sys.argv[1], 'r') as rpc_file:
    urls = rpc_file.read().split('\n')

compare_dict = {}
checking_blocks = set()
checking_blocks.add(0)

while len(checking_blocks) != int(sys.argv[2]):
    checking_blocks.add(random.randint(1, 1_000_000))

for rpc_url in urls:
    archive_point = 0
    w3 = Web3(Web3.HTTPProvider(rpc_url))

    for block_num in checking_blocks:
        try:
            logs = w3.eth.get_block(block_num)
        except Exception as e:
            print(f"{type(e).__name__}: {e}")
            break

        if compare_dict.get(block_num) is None:
            compare_dict[block_num] = logs
        else:

            if logs != compare_dict[block_num]:
                print(f"Confilct in block {block_num} in {rpc_url}")


        if logs:
            archive_point += 1

    print(f"{rpc_url} : {archive_point}")
