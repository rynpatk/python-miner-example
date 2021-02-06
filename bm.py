from hashlib import sha256
import time

MAX_NONCE = 1000000

# encode a string before encrypting with sha and then stringify the output hex
# 64 4-bit characters === 256 bit
# print(sha256('ryan'.encode('ascii')).hexdigest())

mock_hash = '0000a2b6471d044a53a7757994b51dd33c6b3ec90e1aca21cebc8e2ae79d6d9b'

def SHA256(text):
    return sha256(text.encode('ascii')).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_string = prefix_zeros * '0' # outputs something like '0000'
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)

        if new_hash.startswith(prefix_string):
            print(f'success! block mined with nonce {nonce}:')
            return new_hash

    raise BaseException('block unable to be mined with available compute :(')
    
# python main entry point check
if __name__ == '__main__':
    transactions = '''
        foo->bar->20,
        bat->bing->45
    '''

    difficulty = 5
    start_time = time.time()
    new_hash = mine(5, transactions, mock_hash, difficulty)
    time_duration = str(time.time() - start_time)

    print(f'computation finished in {time_duration} seconds')
    print(new_hash)
