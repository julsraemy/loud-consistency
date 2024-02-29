# LOUD Consistency

Initiatlly, there were several ideas on how consistency of Linked Open Usable Data (LOUD), namely that [International Image Interoperability Framework](https://iiif.io) (IIIF) and [Linked Art](https://linked.art) data could be verified according to several factors (syntax, patterns, compliance to the APIs). This repository is an attempt to document the various actions undertaken in the context of a PhD Thesis on [LOUD for Cultural Heritage](https://phd.julsraemy.ch) in terms of data validation and consistency.

## 1. IIIF Presentation API Resources

- Initial idea: IIIF (X) vs Linked Art (Y), against Xs implementation how consistent? Against Ys implementation

Dropping Linked Art but focusing on IIIF Manifests V2.1 versus V3.0 against the [Presentation API Validator](https://presentation-validator.iiif.io/). For instance: Bodleian, Getty, Internet Archive (some of them have content negotiation implemented). Also how it relates to the cookbook recipes and which viewers support what. 

## 2. LUX Data Consistency

For the first action, a compressed slice of the Linked Art data from LUX, Yale Collections Discovery has been provided. For the second and third action related purely to LUX, a CSV has been provided.

### Syntax

- Initial idea: Syntax against the Linked Art Schema Definitions - Linked Art specification <-> Data [Automatable] - 1/24th records (LUX), the highest number of parallel processes. The JSONL file can be extracted using `lux_jsonl_extractor.py`. See [lux-ectractor](lux-extractor/README.md).

A fork of the [Linked Art JSON Validator](https://github.com/julsraemy/json-validator) will be leveraged. The `lux-schema-test.py` should be amended so it can parse several links or JSON-LD files. 

### Unit to unit consistency (YCBA and YUAG)

- Initial idea: Unit to unit consistency, e.g. YCBA & YUAG to check (same domain). To some extent, first by hand with a couple of instances, then Activity Streams endpoints or thumb drives.

### Consistency of concepts between LUX and the Getty Vocabularies 

- Initial idea: LUX <-> external Linked Art that have the same concepts, that would be the Getty JSON-LD representation of the AAT, ULAN, TGN [To some extent, first by hand with a couple of instances]

## 3. Linked Art Model

- Initial idea: Model consistency with LUX, O'Keeffee, Getty (museum data and vocabularies), Van Gogth Worldwide, Rijksmuseum. Some of the interesting patterns: `Primary Name`, `Exhibition`, `Material Statement`, `Provenance Statement`

Out of scope for the moment in terms of robust model consistency (because there are way too dissimilar) check but needs to be part of the PhD can I can "call them out" in terms of what these instutions have done, why it was modelled like this and the next steps. 

## Collections

### IIIF 

See https://guides.iiif.io/ and target institutions that have implemented both the IIIF Presentation API 2.1 and 3.0.

### Linked Art

The following collections or datasets use slightly different versions and have extensions to be ratified or replaced. The Rijksmuseum dump has also been serialised in Turtle rather than in JSON-LD.

- [LUX](https://lux.collections.yale.edu/)
- [The Art and Life of Georgia O’Keeffe](https://collections.okeeffemuseum.org/)
- [Getty Museum Collection](https://data.getty.edu/museum/collection/docs/)
- [Getty Vocabularies](https://www.getty.edu/research/tools/vocabularies/)
- [Van Gogh Worldwide](https://vangoghworldwide.org/)
- [Rijksmuseum](https://data.rijksmuseum.nl/object-metadata/download/)
