def compute_pool_address(self, token_address_a, token_address_b):
    pair_traded = [token_address_a.lower(), token_address_b.lower()]
    pair_traded.sort()
    hexadem = '0x00fb7f630766e6a796048ea87d01acd3068e8ff67d078148a3fa3f4a84f69bd5'
    abiEncoded_1 = encode_abi_packed(['address', 'address'], (pair_traded[0], pair_traded[1]))
    salt_ = self.web3.solidityKeccak(['bytes'], ['0x' + abiEncoded_1.hex()])
    abiEncoded_2 = encode_abi_packed(['address', 'bytes32'], (PANCAKE_FACTORY_ADDRESS, salt_))
    return self.web3.toChecksumAddress(self.web3.solidityKeccak(['bytes', 'bytes'], ['0xff' + abiEncoded_2.hex(), hexadem])[12:])
