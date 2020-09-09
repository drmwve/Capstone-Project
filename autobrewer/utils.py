import time
from functools import wraps
from .exceptions import ComponentControlError

class _Disabled:
    """helper class for a decorator that disables
    a function for some time delay"""

    def __init__(self, disable_duration, num_components):
        self.first_call = [True for x in range(num_components)]
        self.disable_duration = disable_duration
        self.last_called = [time.time() for x in range(num_components)]

    def __bool__(self, index):
        """return True if disabled, False otherwise
        Attention: has a side effect with consequences:
        ==>> upon first time called, sets first_called flag to false
        """


    def __call__(self,index):
        if self.first_call[index]:
            self.first_call[index] = False
            return False

        _disabled = time.time() - self.last_called[index] > self.disable_duration

        if _disabled:
            self.last_called[index] = time.time()
            return False
        return True


def set_windup_time(disable_time=5, num_components=1):
    """Decorator factory that modifies the decorated functions so that
    after execution, they are disabled for some time, before they can run
    again
    """
    def _disable_for_a_while_after_called(f):
        must_not_call_function = _Disabled(disable_time, num_components)
        @wraps(f)
        def wrapped(self, component_index, *args, **kwargs):
            if must_not_call_function(component_index):
                raise ComponentControlError("Attempted to control component while changing state")
            else:
                r = f(self, component_index, *args, **kwargs)
            return r
        return wrapped
    return _disable_for_a_while_after_called
