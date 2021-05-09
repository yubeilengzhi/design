"""
RSA 非对称加密
"""

import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5


def encrypt(public_key, message):
    """
    加密明文
    :param public_key: 公钥
    :param message: 明文
    :return: 加密的文本
    """
    message_bype = message.encode(encoding="utf-8")
    cipher = PKCS1_v1_5.new(public_key)
    dd = cipher.encrypt(message_bype)
    cipher_text = base64.b64encode(dd)
    return cipher_text


def decrypt(rsakey, encrypt_text):
    """
    解密数据
    :param rsakey: 私钥
    :param encrypt_text: 需要解密的文本
    :return: 已经解密的数据
    """
    cipher = PKCS1_v1_5.new(rsakey)
    return cipher.decrypt(base64.b64decode(encrypt_text), '')


# 生成指定大小的密钥对(需大于1024) 公钥和密钥
key_pair = RSA.generate(1024)

# 以pem格式输出私钥
private_pem = key_pair.exportKey()
# print(private_pem)

# 查看公钥
public_key = key_pair.publickey()
# print(public_key)

# 以pem格式输出公钥
public_pem = key_pair.publickey().exportKey()


# print(public_pem)

def test():
    # 明文
    message = 'hello, world'
    # 公钥加密
    encrypt_text = encrypt(public_key, message)
    print('encrypt_text: ', encrypt_text)
    # 私钥解密
    decrypt_text = decrypt(key_pair, encrypt_text)
    print('decrypt_text: ', decrypt_text)

# test()
