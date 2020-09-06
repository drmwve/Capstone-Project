import time
from functools import wraps

class _Disabled:
    """helper class for a decorator that disables
    a function for some time delay"""

    def __init__(self, disable_duration):
        self.first_call = True
        self.disable_duration = disable_duration
        self.last_called = time.time()

    def __bool__(self):
        """return True if disabled, False otherwise
        Attention: has a side effect with consequences:
        ==>> upon first time called, sets first_called flag to false
        """
        if self.first_call:
            self.first_call = False
            return False

        _disabled = time.time() - self.last_called > self.disable_duration

        if _disabled:
            self.last_called = time.time()
            return False
        return True


def disable_for_a_while_after_called(disable_time=5):
    """Decorator factory that modifies the decorated functions so that
    after execution, they are disabled for some time, before they can run
    again
    """
    def _disable_for_a_while_after_called(f):
        must_not_call_function = _Disabled(disable_time)

        @wraps(f)
        def wrapped(*args):
            if must_not_call_function:
                r = None
            else:
                r = f(*args)
            return r
        return wrapped
    return _disable_for_a_while_after_called
