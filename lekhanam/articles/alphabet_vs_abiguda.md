+++
title = "alphabet vs abiguda"
+++

Source: nikhil on discord

I'm also a proponent of Roman transliteration instead of Devanāgarī́, because alphabets are superior (computationally &c.) to abugidas.  If there were an Indian alphabet that were widely used, I'd use it instead of Latin, but I'm not aware of one that even exists let alone being widely used.

Conceptually: they write consonants and vowels separately, which constitute independent sounds not inherently connected to one another, rather than arbitrarily combining them.  Mitrá and mātr̥ ought to begin with the same glyph, but one begins with मि (with the combining vowel in front of the consonant) while the other begins with मा.

<details><summary>उज्ज्वल-प्रतिक्रिया</summary>

svābhāvika-tvḗna (konsepcualī) ítyayáṁ śábdō dr̥ṣṭi-sāpēkṣáḥ (rilēṭiv). dēvanāgaryā́m ḗkēna lipyakṣarḗṇa (gliph-dvārā́) ḗka ēvá svara-varṇáḥ sūcyata íti tátra sundáram 🙂 . ná tú táthā rōmaka-lipāú 😕.
</details>


Computationally: it is far, far easier to do anything involving string search and manipulation in an alphabet than in an abugida.  As an example, if I want to do a regex search like m[iā]trā, this would be extremely difficult to implement in Devanāgarī́ (where I'd have to use combining diacritics in a standalone form).  This is why there aren't really any computational linguistics tools for Sanskrit using anything but Romanization in the back-end; it isn't practical at all to use Devanāgarī́.

<details><summary>उज्ज्वल-प्रतिक्रिया</summary>

kím idám ucyatē 🤷‍♂️ nikhila! saṅgáṇaṁ lípāv ā́yattaṁ ná bhavati khálu! gurukāryā́ya rōmakalipír ápi ná yujyatē 😞 . yát tú kriyátē tád varṇa-vicchēdá 👈  íti kathyatē, ná tú rōmakalipyā́ lḗkhanam íti 😂 . tátra svárāṇām udāttā-nudāttatváṁ hrasva-dīrghatváṁ, vyáñjanānām mārdava-ghōṣatva-vargādi-parijñā́naṁ ca kartavyàm bhavati. tán ná āi-ē-es-ṭī-madhyḗ darśyatē, ná ca es-el-pī-madhyḗ.

aiṣá mámābhiprāyáḥ - saṅgáṇanai (sáṁskr̥ta-viṣayai) prāyaíṇa várṇāir ná kíñcit kriyatai. taíṣāṁ guṇāíḥ prayaújanam bhavati. gunaíṣu svárāṇām udāttā-nudāttatváṁ hrasva-dīrghatváṁ, vyáñjanānām mārdava-ghōṣatva-vargā́dayaś ca santi. ná kā́pi lípir vartatai yásyām imaí víśvai pratyákṣā darśyántai. paraúkṣās tú daivanāgaryā́ṁ raumakalipāú cā́pi baudhyantai. aíkayā likhitáḥ pāṭhaú anyáyā laíkhituṁ śakyatai. táyā dŕ̥ṣṭyā samaí ubhaí.
</details>


Graphically: alphabets make it much easier to add onto specific morphemes or phonemes.  For example, suppose I wanted to emphasize astam in **astam**ayá.  This is very regular in an alphabet: **astam**ayá.  In Devanāgarī́, one must awkwardly split the syllable: **अस्तम्**अय.  Similarly for a phoneme, if I want to emphasize i in M**i**trā́ (e.g. to oppose it to mā́trā), this is very regular in an alphabet: Mitrā́.  In Devanāgarī́, I guess something like म्**इ**त्रा would be required.

There aren't any arguments for abugidas other than saving space (hardly a concern these days) and "tradition" (but it's not as though scripts have any religious significance). 

<details><summary>उज्ज्वल-प्रतिक्रिया</summary>

देवनागर्या॑ ए॑कं गुणं॑ स्मरामि यो॑ रोमकलिपौ॑ ना॑स्ति-  
अस्यां॑ लिपौ॑ ले॑खने य॑दि क॑श्चिद्दो॑षो भ॑वति त॑र्हि स॑ स्पष्ट॑तया दृश्यते।  
त॑स्येदं॑ का॑रणम्-  
उच्चारितवर्णे॑ स्वल्पे॑ना॑पि भे॑देन ले॑खने गुरु॑तरो भे॑दो जायते।  
य॑था ह्रस्व-इकार-स्थाने॑ य॑दि दीर्घ-ईकारो॑ लिख्य॑ते त॑र्हि-  
"कि", "की" इ॑ति गुरु॑र्भे॑दः।  
रोमकलिपौ॑ तु॑-  "i", "ī" इ॑ति अ॑ल्पो भे॑दः।  
दो॑षे कृते॑ न॑ स्फुटं परजञसयत।  

ápi ca yádi várgasya prathamásya sthā́nai tr̥tī́yau likhyátai - "क", "ख" íti mahā́n bhaídaḥ. "k", "kh" ítyátra ná táthā. iyáṁ samasyā́ máyā prāyaíṇā́nubhūyatai yád raumakalipyā́ svayáṁ likhitaí pāṭhaí daúṣai kr̥taí ápi sá ná dr̥śyatai. ítīhá vivakṣitám āsīt.
</details>
