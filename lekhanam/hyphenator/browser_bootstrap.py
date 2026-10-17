"""Bootstrap the hyphenator inside Pyodide (browser).

Expects the layout:
  <this file's dir>/hyphenator.py        - copied doc_curation module
  <this file's dir>/marisa_trie.py       - shim (written for the page)
  <this file's dir>/data/*.bin           - exported tries
  <this file's dir>/vendor/indic_transliteration/...  - extracted zip

Exposes ``hyphenate(text)``.
"""
import os
import sys

APP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, APP)
sys.path.insert(0, os.path.join(APP, "vendor"))

import hyphenator as h

_DATA = os.path.join(APP, "data")
h._DICT_TXT = os.path.join(_DATA, "sanskrit-words.bin")
h._TRIE_PATH = h._DICT_TXT
h._DCS_BABYLON = os.path.join(_DATA, "dcs-frequency.bin")
h._DCS_TRIE_PATH = h._DCS_BABYLON
h._RA_TRIE_PATH = os.path.join(_DATA, "ramAnujIya.bin")
h._RA_FORMS_TRIE_PATH = os.path.join(_DATA, "ramAnujIya-splits.bin")
h._RA_NGRAM_TRIE_PATH = os.path.join(_DATA, "ramAnujIya-ngram.bin")
h._RA_SURFACES_TRIE_PATH = os.path.join(_DATA, "ramAnujIya-surfaces.bin")
h._RA_SOURCES_TOML = os.path.join(APP, "no-sources.toml")

h._load_words()

import logging
logging.getLogger().setLevel(logging.WARNING)


def hyphenate(text):
  """Hyphenate Devanagari (possibly markdown-mixed) text."""
  return h.hyphene(text)


def warmup():
  """Prime the lazy caches so the first user click is fast."""
  h.hyphene("इत्येवम्")
  h.hyphene("एतदुक्तं भवति – परस्यैव ब्रह्मणो निखिलहेयप्रत्यनीकानन्तज्ञानानन्दैकस्वरूपतया सकलेतरविलक्षणस्य")
