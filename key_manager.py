# key_manager.py
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_rsa_keypair(private_key_path: str, public_key_path: str):
    """
    Generates an RSA keypair and saves to PEM files.
    """
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=4096)
    public_key = private_key.public_key()

    # Save private key
    with open(private_key_path, "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()  # Use passphrase in production
        ))

    # Save public key
    with open(public_key_path, "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))



# generate_rsa_keypair(private_key_path='private_key.pem', public_key_path='public_key.pem')

def load_rsa_private_key(private_key_path: str):
    """Loads an RSA private key from a PEM file."""
    with open(private_key_path, "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None)

def load_rsa_public_key(public_key_path: str):
    """Loads an RSA public key from a PEM file."""
    with open(public_key_path, "rb") as f:
        return serialization.load_pem_public_key(f.read())