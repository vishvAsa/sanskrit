---
title: "+पद-भेद-कलन-यन्त्रम्"
summary: "संस्कृत-पदानां समास-पद-भेद-कलनं जालपुट एव (Pyodide/WASM-मध्ये पूर्णः कोडः) - समास-सन्धिषु -, पदयोर् मध्ये रिक्तस्थानं च।"
---

## परिचयः

संस्कृत-पदानां समास-पद-भेदान् प्रस्तुति-रीत्या दर्शयति - समास-सन्धिषु `-`, पदयोर् मध्ये रिक्तस्थानम्। सन्धि-भेदः स्थितः सन् एव दर्श्यते (यथा "तद्धि" → "तद् धि"), न तु पुनः संयुज्यते; दीर्घ-गुण-वृद्धि-मेलनानि ("धर्मार्थ", "स्वप्रकाशाद्वितीय") न भिद्यन्ते। रामानुजीय-प्रस्तुति-सञ्चय-स्मृतिश् च यथेष्टम् अनुस्रियते - यथा "आकाशादि-विशेष-शब्दैर्", "जगत्-कारणे"।

सर्वं जालपुट एव संसरति - [Pyodide](https://pyodide.org/)-द्वारा पूर्णो हाइफनेटर्-कोडः (WASM-मध्ये पाइथन्) तत्रैव धार्यते, शब्दकोश-सञ्चयश् च क्रमशः पठ्यते। न किमपि सर्वरं प्रति प्रेष्यते।

<textarea id="hyph-in" rows="10" cols="80">एतदुक्तं भवति – परस्यैव ब्रह्मणो निखिलहेयप्रत्यनीकानन्तज्ञानानन्दैकस्वरूपतया सकलेतरविलक्षणस्य स्वाभाविकानविधकातिशयासङ्ख्येयकल्याणगुणगणाश्च सन्ति। जगतामुपकाराय न सा कर्मनिमित्तजा। इत्येवं सर्वप्रमाणशतैः सिद्धं सर्वज्ञत्वम् अपास्तसमस्तदोषं जगत्कारणं ब्रह्मैव।</textarea>

<p><button id="hyph-run" type="button" disabled>पद-भेदं कुरु</button> <button id="hyph-copy" type="button" disabled>फलं सङ्कलय (copy)</button> <span id="hyph-status" aria-live="polite"></span>

### फलम्

<pre id="hyph-out" style="white-space: pre-wrap; overflow-wrap: break-word;"></pre>

<script src="app.js"></script>

## यन्त्रांशाः

- कोड्: [app.js](app.js) · [hyphenator.py](hyphenator.py) · [marisa_trie.py](marisa_trie.py) · [toml.py](toml.py) · [browser_bootstrap.py](browser_bootstrap.py) · [indic_transliteration.zip](indic_transliteration.zip)
- शब्द-सञ्चयः (gzip; जालपुटे DecompressionStream-द्वारा विवृत्य पठ्यते): [sanskrit-words.bin.gz](sanskrit-words.bin.gz) · [dcs-frequency.bin.gz](dcs-frequency.bin.gz) · [ramAnujIya.bin.gz](ramAnujIya.bin.gz) · [ramAnujIya-splits.bin.gz](ramAnujIya-splits.bin.gz) · [ramAnujIya-ngram.bin.gz](ramAnujIya-ngram.bin.gz) · [ramAnujIya-surfaces.bin.gz](ramAnujIya-surfaces.bin.gz)
