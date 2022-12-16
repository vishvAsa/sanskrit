+++
title = "6 3 The Way Forward"

+++

I have not dealt with rules teaching accentuation in this thesis. However, accentuation is  inseparable from Pāṇinian Sanskrit and thus, I hope to conduct research in the future on  whether we can correctly derive accented forms using my method of tackling SSRI.  Conversely, using my method of dealing with SSRI may enhance our knowledge about how  accentuation actually works in the Pāṇinian system.  

Secondly, I have not explored rules taught particularly for deriving Vedic forms in this thesis.  However, in the future, research on derivations involving such rules may enable us to verify the correctness of my findings about Pāṇini’s SSRI mechanism. It could also assist us in  understanding which parts of Vedic literature Pāṇini was familiar with, thereby adding to the  work done by Thieme (1935), Bronkhorst (1991) and others on this subject. In sum, such  research will improve our understanding of the relationship between Pāṇini and the Vedas. 

Even though the question of whether certain rules were interpolated into the ‘original’  version of Aṣṭādhyāyī32 is not closely connected with the topic of SSRI, we can benefit from  studying these topics together. For example, if we get the incorrect form at the end of a  derivation in which we have resolved the SSRI using my method, then, in the presence of  supporting evidence, we can consider the possibility that the rule in question has been edited  or constitutes an interpolation.33 

While it may seem that anuvr̥tti34 does not directly influence or get influenced by SSRI, there  are some strong links between the two topics. Anuvr̥tti alone helps us understand the exact  

[^32]: For a detailed discussion on this, see Joshi and Roodbergen (1983).  

[^33]: See example 1 of section 3.1, chapter 3 to understand this better.  

[^34]: For detailed studies on anuvr̥tti, see Joshi and Bhate (1983, 1984).

212 

contents of any rule, and without knowing the contents of a rule, we cannot establish whether  it interacts with other rules at the same step. So, developing a sound understanding of anuvr̥tti can help us better appreciate the functioning of the Aṣṭādhyāyī. Also, if we get the incorrect  form at the end of a derivation in which we have resolved the SSRI using my method, then  we can reconsider if the right words have been continued through anuvr̥tti into the rules  involved in SSRI.35 

Now let us look at how my findings about SSRI in the Aṣṭādhyāyī can potentially open up  new avenues of research in certain disciplines related to Pāṇinian studies. Let us start by  talking about Sanskrit computational linguistics36. One of the main goals of this field is to  teach Pāṇini’s Aṣṭādhyāyī to the computer, so that when we feed the bases, affixes and the 

speaker’s intention37 into the computer, the computer can perform the derivation for us and  give us the correct final form. Understanding how Pāṇini deals with SSRI and knowing the  actual meaning of 1.4.2 will surely help scholars to make progress in achieving this goal. 

My findings can also help develop new ideas for modern theoretical linguistics, and more  specifically, phonology. In Western phonology, Chomsky and Halle (1968) postulated that,  each language has its own fixed order of applying rules in derivations. This is called extrinsic  ordering. Kiparsky (1968), on the other hand, proposed that the order of rule application  could be viewed as being dependent on the formal relationships between rules, namely,  whether one rule feeds or bleeds the other rule.38 This is called intrinsic ordering.  

Pāṇini’s derivations are neither extrinsically nor intrinsically ordered. In fact, one need not  worry about the concept of rule order at all when performing Pāṇinian derivations. This is  because the choice of the rule which should apply at any given step, depends neither on  whether it feeds or bleeds another rule, not on any predetermined order of application.  Instead, this decision is made by the ingenious algorithm devised by Pāṇini to deal with  

[^35]: For instance, consider example 2 of section 3.1, chapter 3.  

36 ‘Sanskrit Computational Linguistics – First and Second International Symposia’ helps one gain a  good understanding about the diversity and scope of the field.  

[^37]: By ‘speaker’s intention’, I mean, information about the exact form he or she wishes to derive. For  example, ‘imperative passive third person singular’.  

[^38]: A feeds B if the application of A facilitates the application of B, and P bleeds Q if the application of  P obstructs the application of Q.

213 

SSRI. Perhaps modern linguistics can overcome the shortcomings of extrinsic and intrinsic  ordering by experimenting with Pāṇini’s model.  

Finally, my work on Pāṇini’s SSRI mechanism can also potentially propel further research on  the topic of ‘natural language complexity’. In computational theory, attempts have been made  to understand how complex a formal language (i.e., an artificial language used in computer  science) is using the Chomskyan hierarchy (based on Chomsky: 1959), which consists of four  different levels of formal language grammars and the ‘machines’ that correspond with them.  Linguists have also tried to situate natural languages in this hierarchy. Let us look at the  hierarchy before we discuss this topic further. 

Language 

	Least powerful  grammar that can  generate it

	Machine equivalent to this  grammar

	Production rule(s)

	recursively  enumerable

	Type 0 

	Turing Machine

	 δ 🡪 θ 

	context 

sensitive

	Type 1 

	Linear Bounded Automaton 

	αΑβ 🡪 αγβ

	context-free 

	Type 2 

	Pushdown Automaton

	 A 🡪 γ

	regular 

	Type 3 

	Finite State Automaton

	 A 🡪 a  

 A 🡪 aB

	







Key: 

a = terminal symbol  

A, B = non-terminal symbol  

α, β, γ, δ, θ = string of symbols39 

[^39]: This information has a purely indicative value but no claim to exhaustiveness. There are some  constraints on some of these strings depending on whether or not they can contain terminals, whether  or not they can be empty etc. but I won’t delve into this because it is not of much importance in the  present context. 

214 

Please read the following three statements carefully in the context of the table presented  above: 

(i) In A 🡪 γ (Type 2), if the string γ contains only one symbol, namely the terminal symbol a,  then this rule can be rewritten as A 🡪 a (Type 3). Similarly, if the string γ contains only two  symbols, namely aB, then this rule can be rewritten as A 🡪 aB (Type 3). These are only two  of many possibilities. Thus, regular grammars (Type 3) constitute a subset of context free  grammars (Type 2). 

(ii) In αΑβ 🡪 αγβ (Type 1), if both α and β are empty, then this rule can be written as A 🡪 γ (Type 2). This is only one of many possibilities. Thus, context free grammars (Type 2)  constitute a subset of context sensitive grammars (Type 1).  

(iii) In δ 🡪 θ (Type 0), if the string δ is αΑβ and if the string θ is αγβ, then this rule can be  rewritten as αΑβ 🡪 αγβ (Type 1). This is only one of many possibilities. Thus, context  sensitive grammars (Type 1) constitute a subset of recursively enumerable grammars (Type  0). 

Therefore, we can represent these grammars as follows: 

Type 0 

Type 1 

Type 2 

Type 3

215 

As can be seen from the diagram above: 

(i) Type 3 grammars can produce Type 3 languages.  

(ii) Type 2 grammars can produce Type 3 and Type 2 languages. 

(iii) Type 1 grammars can produce Type 3, Type 2 and Type 1 languages. (iv) Type 0 grammars can produce Type 3, Type 2, Type 1 and Type 0 languages. 

Note that in terms of productive power, the grammars can be compared as follows (where G1 > G2 stands for ‘G1 is more powerful than G2’): 

Type 0 > Type 1 > Type 2 > Type 3 

As stated above, even though this hierarchy is primarily meant for formal languages, linguists  have attempted to situate natural languages within it. They have shown that Dutch (Bresnan  et al 1982), Swiss German (Shieber 1985) and Bambara (Culy 1985) are neither regular  (Type 3) nor context free (Type 2). Scholars like Fowler (1965), Staal (1965, 1966), Hyman  (2007), Penn and Kiparsky (2012) and Lowe (in press) have discussed the Aṣṭādhyāyī’s  computational ability, the characteristics of the language it produces, and whether and how  we can situate such a language, i.e., Pāṇinian Sanskrit, in the Chomskyan hierarchy. 

I think that there are several loopholes in the thesis that we can meaningfully situate natural  languages – which are significantly different in their nature, composition and purpose, from  formal languages – in a hierarchy meant for formal languages. However, the outcome of my  research has an interesting parallel with one aspect of the Chomskyan hierarchy which I think  merits further exploration. The following diagram illustrates how a Pāṇinian derivation would  look in the absence of Pāṇini’s algorithm for dealing with SSRI. Let us assume, for the sake  of this discussion, that two rules are applicable at every step of the derivation. The derivation  starts at State 1 and the correct final form is State 4h.

216 

State 1 

State 2a State 2b 

State 3a State 3b State 3c State 3d 

State 4a State 4b State 4c State 4d State 4e State 4f State 4g State 4h 

This is a three-step derivation. Step 1 takes us from state 1 to state 2, step 2 from state 2 to  state 3, and lastly step 3 from state 3 to state 4. To reach state 4h one has to make three  correct decisions: one has to choose state 2b in step 1, state 3d in step 2, and state 4h in step  3. But if there had existed no internal algorithm in Pāṇini’s machine, one could have ended 

up with any of the eight final answers (cf. state 4), and the probability of getting the correct  answer would have been be 1/8. However, by teaching his solution for SSRI, Pāṇini has  converted the above machine into the following machine: 

State 1 State 2b State 3d State 4h

To borrow terms from computational theory, Pāṇini has converted his ‘non-deterministic  machine’, which could potentially proceed along multiple derivational paths, into a  deterministic one, which proceeds along a single path dictated by the algorithm. A  deterministic machine is desirable because it produces only correct forms whereas a non 

deterministic machine is not desirable because it produces both correct and incorrect forms. Penn and Kiparsky (2012) say: “through the lens of contemporary NLP40, the most amazing  fact about the Aṣṭādhyāyī is not that it produces so many correct derivations, after all, but that  it simultaneously avoids so many incorrect ones.” 

[^40]: Natural Language Processing. 

217 

Now let us use this information to situate Pāṇinian Sanskrit in this hierarchy. We already  know that we find rules which resemble context sensitive rules (cf. αΑβ 🡪 αγβ) in Pāṇini’s  grammar. Since regular (Type 3) and context free (Type 2) grammars do not contain such  rules, we can infer that Pāṇini’s grammar is neither regular nor context-free. But does the  presence of context-sensitive rules make Pāṇini’s grammar context sensitive (Type 1)?  Context-sensitive grammars in the Chomskyan hierarchy correspond with non-deterministic  linear bounded automata. But as I said, Pāṇini’s grammar is deterministic. Thus, we cannot  call the Aṣṭādhyāyī a Type 1 (context sensitive) grammar. What kind of grammar is the  Aṣṭādhyāyī then? I trust that scholars will be able to answer this question in the future with  the help of the information I have provided above. 

In sum, I am confident that my findings about Pāṇini’s algorithm for regulating SSRI will  enable us to make substantial advances not only in the field of Pāṇinian studies but also in  multiple allied disciplines. pāṇinaye namaḥ!

218 