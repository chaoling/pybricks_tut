"""Registry of programs available from ``master.py``.

Add each new run to ``RUNS``. The menu count is calculated from this tuple.
"""

from run1 import run1
from run2 import run2


RUNS = (
    run1,
    run2,
)