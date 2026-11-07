"""Read-only marisa_trie stand-in for the browser hyphenator page.

Loads the simple binary exports produced from the real ``.trie`` files (see
``export_for_web.py``; the marisa compact format itself is not shipped) and
supports the small API surface ``hyphenator.py`` uses: ``get()``,
``in`` and ``iterkeys(prefix)``.  Values mirror ``marisa_trie``: a list with
one value per key - a tuple for ``RecordTrie`` ("H" -> ``(count,)``,
"II" -> ``(a, b)``) and raw ``bytes`` for ``BytesTrie``.
"""
import struct

_MAGIC = b"HYP1"
_KIND_REC_H = 0
_KIND_BYTES = 1
_KIND_REC_II = 2


class _Trie:
  """Base: keys blob + cumulative end offsets + compact values."""

  def __init__(self):
    self._n = 0
    self._kind = -1
    self._vals = ()
    self._vals2 = ()
    self._ends = ()
    self._blob = b""

  def load(self, path):
    with open(path, "rb") as f:
      data = f.read()
    if data[:4] != _MAGIC:
      raise ValueError("not a HYP1 export: %s" % path)
    kind = data[4]
    (count,) = struct.unpack_from("<I", data, 5)
    off = 9
    if kind == _KIND_REC_H:
      self._vals = struct.unpack_from("<%dH" % count, data, off)
      off += 2 * count
    elif kind == _KIND_BYTES:
      vals = []
      for _ in range(count):
        (ln,) = struct.unpack_from("<I", data, off)
        off += 4
        vals.append(data[off:off + ln])
        off += ln
      self._vals = vals
    elif kind == _KIND_REC_II:
      vals_a = []
      vals_b = []
      for _ in range(count):
        a, b = struct.unpack_from("<II", data, off)
        off += 8
        vals_a.append(a)
        vals_b.append(b)
      self._vals = vals_a
      self._vals2 = vals_b
    else:
      raise ValueError("unknown kind %d" % kind)
    self._ends = struct.unpack_from("<%dI" % count, data, off)
    off += 4 * count
    self._blob = data[off:]
    self._n = count
    self._kind = kind
    return self

  def _key(self, i):
    start = self._ends[i - 1] if i else 0
    return self._blob[start:self._ends[i]]

  def _find(self, key):
    if isinstance(key, str):
      key = key.encode("utf-8")
    lo, hi = 0, self._n
    while lo < hi:
      mid = (lo + hi) // 2
      if self._key(mid) < key:
        lo = mid + 1
      else:
        hi = mid
    if lo < self._n and self._key(lo) == key:
      return lo
    return -1

  def get(self, key, default=None):
    i = self._find(key)
    if i < 0:
      return default
    if self._kind == _KIND_REC_H:
      return [(self._vals[i],)]
    if self._kind == _KIND_REC_II:
      return [(self._vals[i], self._vals2[i])]
    return [self._vals[i]]

  def __getitem__(self, key):
    vals = self.get(key)
    if vals is None:
      raise KeyError(key)
    return vals

  def __contains__(self, key):
    return self._find(key) >= 0

  def __len__(self):
    return self._n

  def iterkeys(self, prefix=""):
    if isinstance(prefix, str):
      prefix = prefix.encode("utf-8")
    lo, hi = 0, self._n
    while lo < hi:
      mid = (lo + hi) // 2
      if self._key(mid) < prefix:
        lo = mid + 1
      else:
        hi = mid
    i = lo
    while i < self._n:
      k = self._key(i)
      if not k.startswith(prefix):
        break
      yield k.decode("utf-8")
      i += 1


class RecordTrie(_Trie):
  """RecordTrie("H") / RecordTrie("II") stand-in (format is read from the
  file header; the constructor argument is accepted for API compatibility)."""

  def __init__(self, fmt="H", *args, **kwargs):
    super().__init__()


class BytesTrie(_Trie):
  """BytesTrie() stand-in."""

  def __init__(self, *args, **kwargs):
    super().__init__()
