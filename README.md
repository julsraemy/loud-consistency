# Linked Open Usable Data (LOUD) Consistency

Initiatlly, there were several ideas on how consistency of LOUD, namely IIIF and Linked Art data, could be checked. 

## IIIF Presentation API Resources

- Initial idea: IIIF (X) vs Linked Art (Y), against Xs implementation how consistent? Against Ys implementation

Dropping Linked Art but focusing on IIIF Manifests V2.1 versus V3.0 against the [Presentation API Validator](https://presentation-validator.iiif.io/). For instance: Bodleian, Getty, Internet Archive (some of them have content negotiation implemented). Also how it relates to the cookbook recipes and which viewers support what. 

## LUX: Syntax

- Initial idea: Syntax against the Linked Art Schema Definitions - Linked Art specification <-> Data [Automatable] - 1/24th records (LUX), the highest number of parallel processes

The [Linked Art JSON Validator](https://github.com/linked-art/json-validator) will be leveraged. The `lux-schema-test.py` should be amended and used. 

## LUX: Unit to Unit (YCBA and YUAG)

- Initial idea: Unit to unit consistency, e.g. YCBA & YUAG to check (same domain) [To some extent, first by hand with a couple of instances, then Activity Streams endpoints or thumb drives]

Rob will provide a CSV

## LUX versus Getty Vocabularies

- Initial idea: LUX <-> external Linked Art that have the same concepts, that would be the Getty JSON-LD representation of the AAT, ULAN, TGN [To some extent, first by hand with a couple of instances]

Rob will provide a CSV, then find 

##  Linked Art Model

- Initial idea: Model consistency with LUX, O'Keeffee, Getty (museum data and vocabularies), Rijksmuseum. Some of the interesting patterns: `Primary Name`, `Exhibition`, `Material Statement`, `Provenance Statement`

Out of scope for the moment in terms of robust model consistency (because there are way too dissimilar) check but needs to be part of the PhD can I can "call them out" in terms of what these instutions have done, why it was modelled like this and the next steps. 

Collections: 

- LUX
- [The Art and Life of Georgia O’Keeffe](https://collections.okeeffemuseum.org/)
- Getty
- [Rijksmuseum](https://data.rijksmuseum.nl/object-metadata/download/)
