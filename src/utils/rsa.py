#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import base64

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


class DocumentRsa:
    code_info = [
        {
            "type": "RSA",
            "description": """
                RSA加密算法是一种公钥加密算法，它能够将明文信息用公钥加密，并用私钥解密。
                填充方式：OAEP填充方式, 使用SHA256算法进行摘要计算。

                加密过程：
                    1. 将明文信息编码为二进制数据。
                    2. 将待加密数据按190字节为一块进行分组。
                    3. 通过公钥加密算法对每一块数据进行加密。
                    4. 将分段密文base64编码, 并拼接起来。
                解密过程：
                    1. 将密文信息编码为二进制数据。
                    2. 将密文按344字节为一块进行分组, 并base64解码。
                    3. 通过私钥解密算法对每一块数据进行解密。
                    4. 将分段二进制数据decode为明文信息, 并拼接起来。

            """,
            "author": "Fry",
            "version": "1.0",
            "date": "2024-12-12",
        }
    ]

    # 生成密钥对
    @staticmethod
    def generate_key_pair():
        private_key = rsa.generate_private_key(
            public_exponent=65537, key_size=2048, backend=default_backend()
        )
        public_key = private_key.public_key()

        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
        with open("file/private.pem", "wb") as f:
            f.write(private_pem)

        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
        with open("file/public.pem", "wb") as f:
            f.write(public_pem)

        return private_pem, public_pem

    # 加密数据
    def encrypt_data(data):
        with open("file/public.pem", "rb") as f:
            public_key = serialization.load_pem_public_key(
                f.read(), backend=default_backend()
            )

        en_data = ""
        if len(data.encode()) > 190:
            for i in range(0, len(data.encode()), 190):
                en_d = public_key.encrypt(
                    data.encode()[i : i + 190],
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None,
                    ),
                )
                en_data += base64.b64encode(en_d).decode()
            return en_data
        else:
            en_data = public_key.encrypt(
                data.encode(),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )
            return base64.b64encode(en_data).decode()

    # 解密数据
    def decrypt_data(data):
        with open("file/private.pem", "rb") as f:
            private_key = serialization.load_pem_private_key(
                f.read(), password=None, backend=default_backend()
            )

        decrypted_data = ""
        if len(data) > 344:
            for i in range(0, len(data), 344):
                d_data = private_key.decrypt(
                    base64.b64decode(data[i : i + 344]),
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None,
                    ),
                )
                decrypted_data += d_data.decode("utf-8", "ignore")

            return decrypted_data
        else:
            decrypted_data = private_key.decrypt(
                base64.b64decode(data),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )

            return decrypted_data.decode("utf-8", "ignore")


if __name__ == "__main__":
    DocumentRsa.generate_key_pair()
