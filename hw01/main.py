"""Compatibility shim: expose build_graph and degree_dict as hw01.main

This module imports the implementations from the project's top-level
`main.py` and re-exports them so tests can import `hw01.main`.
"""

from main import build_graph, degree_dict

__all__ = ["build_graph", "degree_dict"]
