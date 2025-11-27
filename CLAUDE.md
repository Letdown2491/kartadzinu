# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Kartadzinu** ("the language of Carthage") is a constructed language (conlang) representing the fictional evolution of Latin/African Romance in an alternate timeline where North Africa remained independent. Named for Carthage, the great city refounded by Rome, the language evolved from Vulgar Latin with significant Berber substrate influence.

## Key Language Features (Version 2.0)

### Typological Profile
- **Word Order**: SVO default, VSO in elevated/narrative registers
- **Morphological Type**: Moderately synthetic, agglutinative-leaning fusional
- **Alignment**: Nominative-Accusative
- **Key Feature**: Aspect-prominent verbal system (completion status > temporal location)

### Phonology
1. **7-vowel system**:
   - Open mid vowels: e /ɛ/, o /ɔ/ (unmarked)
   - Closed mid vowels: é /e/, ó /o/ (marked with acute accent)
   - Origins: Latin short Ĕ/Ŏ → open; Latin long Ē/Ō or short Ĭ/Ŭ → closed
   - Examples: *Dóminu* (Lord), *nóme* (name), *fónte* (fountain), *dolóru* (pain)
2. **Trilled R**: Single r = brief trill, rr = longer trill (as in Spanish/Italian)
3. **No palatalization**: k/g always hard, even before e/i (unlike Italian/Spanish)
4. **G pronunciation**: The letter g (from historical dz) is pronounced /dʒ/ as in English "judge"
   - *viagare* "to travel", *mangare* "to eat", *Guljeta* "Juliet"

### Distinctive Features from Standard Romance
1. **Aspect over tense**: Imperfective (ongoing) vs Perfective (completed) as primary distinction
2. **Construct state**: *fil-rei* "prince" (son-king) for inalienable possession
3. **Inclusive/exclusive "we"**: *nos* (including listener) vs *nosin* (excluding listener)
4. **Berber vocabulary**: Loanwords from Amazigh languages
5. **Telicity markers**: *ja* (already), *aset* (still), *-ment* (through to completion)
6. **Focus particles**: *ka-* (agent focus), *ta-* (patient focus)
7. **Extensive participle use**: As main predicates, not just modifiers

### Semantic Shifts from Other Romance Languages
- *sapere*: "to taste/experience directly" (NOT "to know")
- *konesere*: "to know intellectually" (reversed from standard)
- *via*: "spiritual path" (physical road = *strata*)
- *anima*: "life-force/vitality" (broader than "soul")

## Repository Structure

```
rumantsu/
├── CLAUDE.md
├── index.html              # Interactive web showcase with pronunciation guide
├── reference/
│   ├── grammar.md          # Complete grammar reference with pronunciation guide
│   └── vocabulary.md       # Comprehensive vocabulary (~2800+ words)
└── translations/
    ├── hymn_of_pearl.md    # Gnostic text (Acts of Thomas)
    ├── thunder_perfect_mind.md  # Gnostic text (Nag Hammadi)
    ├── odes_of_solomon.md  # Early Christian hymns
    ├── conlang_benchmarks.md    # North Wind & Sun, Schleicher's Fable, Hobbit, Babel
    └── romeo_juliet.md     # Shakespeare balcony scene
```

## IMPORTANT: Keeping Documentation Updated

**After any translation or language work, ALWAYS update the reference documents:**

1. **New vocabulary** → Add to `reference/vocabulary.md`
   - Add new verbs to the appropriate verb section
   - Add new nouns to the appropriate noun section
   - Add new adjectives to the adjectives section
   - Create a new "### [Text Name] Specific" subsection if translating a new text
   - Update the total word count and source coverage at the bottom

2. **New grammar features** → Add to `reference/grammar.md`
   - Document any new morphological patterns
   - Add new conjugation paradigms if created
   - Update examples to include new constructions

3. **New translations** → Add the file to `translations/` and update the Repository Structure above

Do not wait to be reminded—update these documents immediately after completing translation work.

## Bilingual Document Format

All translated documents must follow this consistent format:

```markdown
# ENGLISH TITLE / RUMANTSU TITLE
## Bilingual Edition: English - Kartadzinu

*Brief description of the source text*

---

## Introduction

[Description of the text, its origin, and why it suits Kartadzinu. List the specific Kartadzinu features the translation showcases.]

The English text follows [translator name]'s translation from [source language].

---

## I. SECTION TITLE IN ENGLISH / SECTION TITLE IN RUMANTSU

**English:**
[English text with poetic line breaks using two trailing spaces]

**Kartadzinu:**
[Kartadzinu translation with matching line breaks]

---

[Continue with sections II, III, etc.]

---

## Translation Notes

### Features Showcased
[Explain which Kartadzinu features appear in this translation with examples]

### Vocabulary Notes
[Table of notable new vocabulary with Latin origins and meanings]

---

*Finis de [Kartadzinu Title]*
*End of the [English Title]*

**Kartadzinu Version 2.0 - [Month Year]**
[Brief credit line for source translation]
```

### Format Rules
- Section numbers use Roman numerals (I, II, III...)
- Section headers are bilingual: `## III. ENGLISH / RUMANTSU`
- English and Kartadzinu blocks labeled with `**English:**` and `**Kartadzinu:**`
- Horizontal rules (`---`) separate all major sections
- Poetic indentation preserved using 4 spaces for continuation lines
- Lacunae (gaps in source text) shown as `[...]`
- Include Introduction explaining text's significance for Kartadzinu
- Include Translation Notes section at end
- End with bilingual *Finis* line and version/date

## Working with Kartadzinu

When translating or creating Kartadzinu text:
1. Check grammar reference for morphological rules (verb conjugations, construct state formation)
2. Use vocabulary file for word lookups
3. Apply aspect distinction (imperfective for ongoing, perfective for completed)
4. Use construct state for inalienable possession and fixed compounds
5. Consider register: VSO for elevated/narrative, SVO for casual speech
6. **Apply vowel markings**: Use é/ó for closed mid vowels in key words (check vocabulary.md)

### Common Patterns
- Articles: *lu/la/lus/las* (definite), *un/una/uns/unas* (indefinite)
- Verb classes: -are (I), -ere (II), -ire (III)
- Plural: add *-s* to singular
- Adverbs: feminine adjective + *-mente*

### Key Vocabulary with Vowel Markings
Words that require closed vowel marking (these are common and should always be marked):
- *Dóminu* (Lord), *Déu* (God), *kélu* (sky/heaven)
- *nóme* (name), *fónte* (fountain), *dónu* (gift)
- *dolóru* (pain), *sól* (sun), *glória* (glory)
- *tóga* (robe), *heróvu* (hero), *só* (I am)
