import os

def is_raspberry_pi(raise_on_errors=False):
    """Checks if Raspberry PI.

    :return:
    """
    return os.uname()[4].startswith("arm")