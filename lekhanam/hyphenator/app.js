/* Client-side Sanskrit hyphenator (पद-भेद-कलनम्).
 *
 * Runs the real doc_curation/sanskrit/hyphenator.py under Pyodide (wasm):
 * the module, its marisa-trie shim and the exported trie data are page
 * resources next to this script; indic_transliteration is vendored as a zip
 * that is extracted into the Pyodide filesystem on first load.
 *
 * The theme re-renders/clones the article content after this script starts,
 * so element references are resolved lazily and clicks are handled by
 * delegation - never bind or cache DOM nodes here.
 */
(function () {
  "use strict";

  var PYODIDE_BASE = "https://cdn.jsdelivr.net/pyodide/v0.26.4/full/";
  var BASE = document.currentScript.src.replace(/[^\/]*$/, "");

  var FILES = [
    ["marisa_trie.py", "/app/marisa_trie.py"],
    ["toml.py", "/app/toml.py"],
    ["browser_bootstrap.py", "/app/browser_bootstrap.py"],
    ["hyphenator.py", "/app/hyphenator.py"],
    ["indic_transliteration.zip", "/app/indic_transliteration.zip"],
  ];
  var DATA = [
    "sanskrit-words.bin.gz",
    "dcs-frequency.bin.gz",
    "ramAnujIya.bin.gz",
    "ramAnujIya-splits.bin.gz",
    "ramAnujIya-ngram.bin.gz",
    "ramAnujIya-surfaces.bin.gz",
  ];

  function el(id) {
    return document.getElementById(id);
  }

  function setStatus(msg) {
    var s = el("hyph-status");
    if (s) s.textContent = msg;
  }

  function setButtonsDisabled(disabled) {
    var b = el("hyph-run");
    if (b) b.disabled = disabled;
    b = el("hyph-copy");
    if (b) b.disabled = disabled;
  }

  function loadScript(src) {
    return new Promise(function (resolve, reject) {
      var s = document.createElement("script");
      s.src = src;
      s.onload = resolve;
      s.onerror = function () { reject(new Error("failed to load " + src)); };
      document.head.appendChild(s);
    });
  }

  async function fetchBytes(url) {
    var resp = await fetch(url);
    if (!resp.ok) throw new Error(resp.status + " " + url);
    var buf = await resp.arrayBuffer();
    if (url.endsWith(".gz")) {
      var stream = new Blob([buf]).stream()
          .pipeThrough(new DecompressionStream("gzip"));
      buf = await new Response(stream).arrayBuffer();
    }
    return new Uint8Array(buf);
  }

  var hyphenate = null;
  var busy = false;

  async function init() {
    setButtonsDisabled(true);
    setStatus("Pyodide लोड भवति (≈10 MB)...");
    await loadScript(PYODIDE_BASE + "pyodide.js");
    var pyodide = await loadPyodide({ indexURL: PYODIDE_BASE });
    setStatus("पाइथन्-सञ्चयौ: regex, tqdm...");
    await pyodide.loadPackage(["regex", "tqdm"]);
    pyodide.FS.mkdirTree("/app/data");

    for (var i = 0; i < FILES.length; i++) {
      setStatus("यन्त्रांश-सञ्चयः: " + FILES[i][0]);
      var bytes = await fetchBytes(BASE + FILES[i][0]);
      pyodide.FS.writeFile(FILES[i][1], bytes);
    }
    for (var j = 0; j < DATA.length; j++) {
      setStatus("शब्द-कोशः: " + DATA[j] + " (" + (j + 1) + "/" + DATA.length + ")");
      var bin = await fetchBytes(BASE + DATA[j]);
      pyodide.FS.writeFile("/app/data/" + DATA[j].replace(/\.gz$/, ""), bin);
    }

    setStatus("Pyodide-मध्ये संस्करणम्...");
    await pyodide.runPythonAsync(
      "import sys, zipfile\n" +
      "zipfile.ZipFile('/app/indic_transliteration.zip').extractall('/app/vendor')\n" +
      "sys.path.insert(0, '/app')\n" +
      "sys.path.insert(0, '/app/vendor')\n" +
      "import browser_bootstrap\n" +
      "browser_bootstrap.warmup()\n" +
      "globals()['hyphenate'] = browser_bootstrap.hyphenate\n");
    hyphenate = pyodide.globals.get("hyphenate");
    setStatus("");
    setButtonsDisabled(false);
  }

  function run() {
    if (!hyphenate || busy) return;
    var inputEl = el("hyph-in");
    var outEl = el("hyph-out");
    if (!inputEl || !outEl) return;
    var text = inputEl.value;
    if (!text.trim()) {
      outEl.textContent = "";
      return;
    }
    busy = true;
    setStatus("पद-भेदः क्रियते...");
    window.setTimeout(function () {
      try {
        outEl.textContent = hyphenate(text);
        setStatus("");
      } catch (err) {
        setStatus("दोषः: " + err);
        console.error(err);
      }
      busy = false;
    }, 0);
  }

  async function copyOut() {
    var outEl = el("hyph-out");
    if (!outEl) return;
    try {
      await navigator.clipboard.writeText(outEl.textContent);
      setStatus("Copy ok");
    } catch (err) {
      var range = document.createRange();
      range.selectNodeContents(outEl);
      var sel = window.getSelection();
      sel.removeAllRanges();
      sel.addRange(range);
      setStatus("Select + Ctrl+C");
    }
    window.setTimeout(function () { setStatus(""); }, 2000);
  }

  document.addEventListener("click", function (ev) {
    var t = ev.target;
    if (!t || !t.id) return;
    if (t.id === "hyph-run") run();
    else if (t.id === "hyph-copy") copyOut();
  });

  init().catch(function (err) {
    setStatus("सञ्चय-दोषः: " + err.message);
    console.error(err);
  });
})();
