import hmac
import hashlib
import base64
import uuid

from datetime import datetime
from .config import Configs


def generate_uuid() -> tuple:
    generated_uuid = str(uuid.uuid4())
    url_uuid = generated_uuid.replace("-", "")
    return generated_uuid, url_uuid


def parse_datetime(timestamp: int) -> str:
    if timestamp is not None:
        return str(datetime.fromtimestamp(timestamp))
    return timestamp


def generate_key():
    # TODO: generate secrete_key
    pass


def encrypt(key: str, credential: str):
    pass


def decrypt(key: str, credential: str):
    pass


def signed_info_calculating(uuid: str, timestamp: int, shared_key: bool = False) -> str:
    """
    Pass the device_uuid when shared_key is False.
    """
    shared_key = Configs.YAY_SHARED_KEY if shared_key is True else ""
    return hashlib.md5((
        Configs.YAY_API_KEY + uuid + str(timestamp) + shared_key
    ).encode()).hexdigest()


def signed_version_calculating() -> str:
    hash_object = hmac.new(
        Configs.YAY_API_VERSION_KEY.encode(),
        "yay_android/{}".format(Configs.YAY_API_VERSION).encode(),
        hashlib.sha256
    )
    return base64.b64encode(hash_object.digest()).decode("utf-8")
