"""Bootstrap the hyphenator inside Pyodide (browser).

Expects the layout:
  <this file's dir>/hyphenator/*.py       - copied doc_curation package
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
import hyphenator.constants as C

_DATA = os.path.join(APP, "data")
# With no wordlist sources present, _load_words loads the prebuilt word
# tries and never rebuilds.
C._DCS_TRIE_PATH = os.path.join(_DATA, "dcs-stems.bin")
C._WORD_TRIE_PATHS = {
    "padas": os.path.join(_DATA, "padas.bin"),
    "nominal-stems": os.path.join(_DATA, "nominal-stems.bin"),
    "verb-stems": os.path.join(_DATA, "verb-stems.bin"),
    "avyayas": os.path.join(_DATA, "avyayas.bin"),
}
C._RA_TRIE_PATH = os.path.join(_DATA, "ramAnujIya.bin")
C._RA_FORMS_TRIE_PATH = os.path.join(_DATA, "ramAnujIya-splits.bin")
C._RA_NGRAM_TRIE_PATH = os.path.join(_DATA, "ramAnujIya-ngram.bin")
C._RA_ATTESTATIONS_TRIE_PATH = os.path.join(_DATA, "ramAnujIya-attestations.bin")
C._RA_BADSPLITS_TRIE_PATH = os.path.join(_DATA, "ramAnujIya-badsplits.bin")
C._RA_SEPS_TRIE_PATH = os.path.join(_DATA, "ramAnujIya-seps.bin")
C._RA_SOURCES_TOML = os.path.join(APP, "no-sources.toml")
C._MISC_DATA_TOML = os.path.join(_DATA, "misc_hyphenator_data.toml")
C._MISC_VOCAB_TOML = os.path.join(_DATA, "misc-vocab.toml")

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
