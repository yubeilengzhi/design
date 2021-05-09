"""
AES 对称加密
使用pycryptodome模块进行加解密
"""

from Crypto.Cipher import AES
from Crypto import Random
from hashlib import md5

# 明文
my_data = '我要加密的数据'
# 通过 md5快速生成128位Bytes的秘钥key
key = md5('mysecret'.encode()).hexdigest()

# 生成长度等于AES块大小且不可重复的秘钥块
iv = Random.new().read(AES.block_size)


# 加密明文如果出现TypeError: Object type <class 'str'> cannot be passed to C code
# 需要将参数先转为bytes

def encrypt(key = key, iv = iv, my_data = my_data):
    """
    加密数据
    :param key: 秘钥
    :param iv: 秘钥块
    :param my_data: 需要加密的数据
    :return: 已经加密的数据
    """
    encrypt_data = AES.new(key.encode(), AES.MODE_CFB, iv).encrypt(my_data.encode())
    # encrypt_data = AES.new(key.encode(), AES.MODE_CFB, iv).encrypt(my_data)
    return encrypt_data


def decrypt(key = key,iv = iv,encrypt_data = ''):
    """
    解密数据
    :param key: 秘钥
    :param iv: 秘钥块
    :param encrypt_data: 需要解密的数据
    :return: 已经解密的数据
    """
    decrypt_data = AES.new(key.encode(), AES.MODE_CFB, iv).decrypt(encrypt_data).decode("utf8","ignore")
    # decrypt_data = AES.new(key.encode(), AES.MODE_CFB, iv).decrypt(encrypt_data).decode()
    return decrypt_data

# encrypt_data = encrypt(key,iv,my_data)
# print(encrypt_data)
# decrypt_data = decrypt(key,iv,encrypt_data)
# print(decrypt_data)