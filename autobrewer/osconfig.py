import platform

def is_raspberry_pi(raise_on_errors=False):
    """Checks if Raspberry PI.

    :return:
    """
    return platform .uname()[4].startswith("arm")