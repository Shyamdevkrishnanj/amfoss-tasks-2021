import hashlib

class RoonCoinBlock:
    
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        
        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
        
t1 = "Shyam made a transaction to Shashank"
t2 = "Lakshmi made a transaction to Shashank"
t3 = "Shashank made a transaction to Lakshmi"
t4 = "Akshay made a transaction to Shyam"
t5 = "Shashank made a transaction to Aswanth"
t6 = "Shashank made a transaction to Akshay"

initial_block = RoonCoinBlock("Initial String", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash) 

second_block = RoonCoinBlock(initial_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = RoonCoinBlock(second_block.block_hash, [t5, t6])

print(third_block.block_data)
print(third_block.block_hash)