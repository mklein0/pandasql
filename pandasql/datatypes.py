import pandas as pd
from sqlite3 import register_adapter


def call_once(fn):
    """
    Wrap a function to be called only once.  Returns None on sub-sequent calls.
    """
    def wrapper(*args, **kwargs):
        if wrapper.has_run:
            return

        wrapper.has_run = True
        return fn(*args, **kwargs)

    wrapper.has_run = False
    return wrapper


@call_once
def register_pandas_dtype_with_sqlite():
    # Register Pandas Datatypes under sqlite
    register_adapter(pd.Timestamp, lambda val: val.isoformat(" "))

