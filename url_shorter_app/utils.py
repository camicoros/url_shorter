import random
import string

CHARACTERS = string.ascii_letters + string.digits


def generate_slug(url_length: int = 6):
    result = random.choices(CHARACTERS, k=url_length)
    return "".join(result)
