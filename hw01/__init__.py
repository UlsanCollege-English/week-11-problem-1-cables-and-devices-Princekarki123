"""hw01 package shim for tests.

This package re-exports the functions implemented in the project's top-level
`main.py` so tests that import `hw01.main` will find `build_graph` and
`degree_dict`.
"""

from .main import build_graph, degree_dict

__all__ = ["build_graph", "degree_dict"]
