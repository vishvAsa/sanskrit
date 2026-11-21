"""Minimal stand-in for the ``toml`` package (Pyodide has no wheel for it).

Only the API used by vendored ``indic_transliteration`` is provided:
``load()`` accepting a path string or a file object, and ``loads()``.
Backed by the stdlib ``tomllib`` (Python 3.11+).
"""
import tomllib


def loads(s):
  if isinstance(s, bytes):
    s = s.decode("utf-8")
  return tomllib.loads(s)


def load(f):
  if hasattr(f, "read"):
    return loads(f.read())
  with open(f, "rb") as fh:
    return tomllib.load(fh)


def dump(*args, **kwargs):
  raise NotImplementedError("the browser toml shim is read-only")
