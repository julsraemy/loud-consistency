# 2. LUX Data Consistency

1. [Syntax](#syntax)
  1. [Investigation](#investigation)
  2. [Concepts](#concepts)
  3. [Digital Objects](#digital-objects)
  4. [Events](#events)
  5. [Groups](#groups)
  6. [People](#people)
  7. [Physical Objects](#physical-objects)
  8. [Places](#places)
  9. [Provenance Activities]
  10. [Sets]
  11. [Textual Works](#textual-work)
  12. [Visual Works]
  13. [Summary](#summary)
2. [Unit to unit consistency (YCBA and YUAG)](#unit-to-unit-consistency-ycba-and-yuag)
3. [Consistency of concepts between LUX and the Getty Vocabularies](#consistency-of-concepts-between-lux-and-the-getty-vocabularies)

## Syntax

Testing the Linked Art JSON validator and the schemas with data coming from the [Linked Art API Endpoints](https://linked.art/api/1.0/endpoint/) and [LUX](https://lux.collections.yale.edu/).

### Investigation

The test was done between 5 and 6 October 2023 to see if the Linked Art examples and schemas were up-to-date as well as to validate examplary data from LUX before conducting validation on a larger scale.

The Python Script that was used is a adaption from the Linked Art JSON validator and is stored within a fork: https://github.com/julsraemy/json-validator/blob/master/schema-test.py


### Concepts

- Documentation: https://linked.art/api/1.0/endpoint/concept/
- Schema: https://linked.art/api/1.0/schema/concept.json 

#### Linked Art Endpoint Example

- https://linked.art/example/concept/0.json

```bash
-----------------------
Processing: https://linked.art/example/concept/0.json
  Validation failed. Validation errors:
  Error 1: /member_of/0 --> 'id' is a required property
  Error 2: /created_by/influenced_by/0 --> 'id' is a required property
  Error 3: /created_by/influenced_by/1 --> 'id' is a required property
  Error 4: /broader/0 --> 'id' is a required property
```

#### LUX

- https://lux.collections.yale.edu/data/concept/000052b6-a350-4bcb-afca-15dceb72920a

```bash
-----------------------
Processing: https://lux.collections.yale.edu/data/concept/000052b6-a350-4bcb-afca-15dceb72920a
  Validation failed. Validation errors:
  Error 1: / --> Additional properties are not allowed ('_links' was unexpected)
```

### Digital Objects

- Documentation: https://linked.art/api/1.0/endpoint/digital_object/
- Schema: https://linked.art/api/1.0/schema/digital.json


#### Linked Art Endpoint Example

- https://linked.art/example/digital/0

```bash
-----------------------
Processing: https://linked.art/example/digital/0
  Validation failed. Validation errors:
  Error 1: /part_of --> [{'id': 'https://iiif.harvardartmuseums.org/manifests/object/299843', 'type': 'DigitalObject', '_label': 'IIIF Manifest'}] is not of type 'object'
  Error 2: /digitally_shows/0 --> 'id' is a required property
```

#### LUX

```bash
-----------------------
Processing: https://lux.collections.yale.edu/data/digital/0000a6dc-87c3-40e9-b6fe-eac4b7858d9a
  Validation failed. Validation errors:
  Error 1: /identified_by/1 --> {'type': 'Identifier', 'content': 'ils:yul:mfhd:11743917', 'attributed_by': [{'type': 'AttributeAssignment', 'carried_out_by': [{'id': 'https://lux.collections.yale.edu/data/group/d07b9b86-0a1e-4026-aa4c-8ecba8bbd9c9', 'type': 'Group', '_label': 'Yale University Library'}]}], 'classified_as': [{'id': 'https://lux.collections.yale.edu/data/concept/89630361-18a3-4c4b-bcd7-16894d95defd', 'type': 'Type', '_label': 'System-Assigned Number'}]} is not valid under any of the given schemas
  Error 2: / --> Additional properties are not allowed ('_links' was unexpected)
```

### Events

- Documentation: https://linked.art/api/1.0/endpoint/event/
- Schema: https://linked.art/api/1.0/schema/event.json

#### Linked Art Endopint Example

- https://linked.art/example/event/0

```bash
-----------------------
Processing: https://linked.art/example/event/0
  Validation failed. Validation errors:
  Error 1: /subject_of/0 --> Additional properties are not allowed ('id' was unexpected)
```

#### LUX

- https://lux.collections.yale.edu/data/activity/00b7bec9-3f14-49c1-9b58-22e04196c6ad (`Period`)

```bash
-----------------------
Processing: https://lux.collections.yale.edu/data/activity/00b7bec9-3f14-49c1-9b58-22e04196c6ad
  Validation failed. Validation errors:
  Error 1: /equivalent/0/type --> 'Activity' was expected
  Error 2: / --> Additional properties are not allowed ('_links' was unexpected)
```

### Groups

- Documentation: https://linked.art/api/1.0/endpoint/group/
- Schema: https://linked.art/api/1.0/schema/group.json

#### Linked Art Endpoint Example

- https://linked.art/example/group/0

```bash
-----------------------
Processing: https://linked.art/example/group/0
  Validation failed. Validation errors:
  Error 1: /residence/0 --> 'id' is a required property
  Error 2: /formed_by/took_place_at/0 --> 'id' is a required property
  Error 3: /dissolved_by/took_place_at/0 --> 'id' is a required property
```

#### LUX

- https://lux.collections.yale.edu/data/group/020318c8-df24-4999-a5b8-8d17fd79ed6e

```bash
-----------------------
Processing: https://lux.collections.yale.edu/data/group/020318c8-df24-4999-a5b8-8d17fd79ed6e
  Validation failed. Validation errors:
  Error 1: / --> Additional properties are not allowed ('_links' was unexpected)
```

### People

- Documentation: https://linked.art/api/1.0/endpoint/person/
- Schema: https://linked.art/api/1.0/schema/person.json

#### Linked Art Endpoint Example

- https://linked.art/example/person/0

```bash
-----------------------
Processing: https://linked.art/example/person/0
  Validation failed. Validation errors:
  Error 1: /carried_out/0/took_place_at/0 --> 'id' is a required property
  Error 2: /residence/0 --> 'id' is a required property
  Error 3: /born/took_place_at/0 --> 'id' is a required property
  Error 4: /died/took_place_at/0 --> 'id' is a required property
```

#### LUX

- https://lux.collections.yale.edu/data/person/02051b6b-b245-43db-985a-e6bedc830444

```bash
-----------------------
Processing: https://lux.collections.yale.edu/data/person/02051b6b-b245-43db-985a-e6bedc830444
  Validation failed. Validation errors:
  Error 1: /born/timespan --> Additional properties are not allowed ('_seconds_since_epoch_begin_of_the_begin', '_seconds_since_epoch_end_of_the_end' were unexpected)
  Error 2: / --> Additional properties are not allowed ('_links' was unexpected)
```

### Physical Objects

- Documentation: https://linked.art/api/1.0/endpoint/physical_object/
- Schema: https://linked.art/api/1.0/schema/object.json 

#### Linked Art Endpoint Example

- https://linked.art/example/object/0

```bash
-----------------------
Processing: https://linked.art/example/object/0
  Validation failed. Validation errors:
  Error 1: /member_of/0 --> 'id' is a required property
```

#### LUX

- https://lux.collections.yale.edu/data/object/020692b3-4dbf-4b72-9933-b34da851454a

```bash
-----------------------
Processing: https://lux.collections.yale.edu/data/object/020692b3-4dbf-4b72-9933-b34da851454a
  Validation failed. Validation errors:
  Error 1: /identified_by/1 --> {'type': 'Identifier', 'content': 'ils:yul:mfhd:5161477', 'attributed_by': [{'type': 'AttributeAssignment', 'carried_out_by': [{'id': 'https://lux.collections.yale.edu/data/group/d07b9b86-0a1e-4026-aa4c-8ecba8bbd9c9', 'type': 'Group', '_label': 'Yale University Library'}]}], 'classified_as': [{'id': 'https://lux.collections.yale.edu/data/concept/89630361-18a3-4c4b-bcd7-16894d95defd', 'type': 'Type', '_label': 'System-Assigned Number'}]} is not valid under any of the given schemas
  Error 2: / --> Additional properties are not allowed ('_links' was unexpected)
```

### Places

- Documentation: https://linked.art/api/1.0/endpoint/place/
- Schema: https://linked.art/api/1.0/schema/place.json

#### Linked Art Endpoint Example

- https://linked.art/example/place/0

```bash
-----------------------
Processing: https://linked.art/example/place/0
  Validation failed. Validation errors:
  Error 1: /member_of/0 --> 'id' is a required property
  Error 2: /approximated_by/0 --> 'id' is a required property
  Error 3: /part_of/0 --> 'id' is a required property
```

#### LUX

- https://lux.collections.yale.edu/data/place/020b2cbd-1f89-463d-8f89-36bec254fb28

```bash
-----------------------
Processing: https://lux.collections.yale.edu/data/object/020692b3-4dbf-4b72-9933-b34da851454a
  Validation failed. Validation errors:
  Error 1: /identified_by/1 --> {'type': 'Identifier', 'content': 'ils:yul:mfhd:5161477', 'attributed_by': [{'type': 'AttributeAssignment', 'carried_out_by': [{'id': 'https://lux.collections.yale.edu/data/group/d07b9b86-0a1e-4026-aa4c-8ecba8bbd9c9', 'type': 'Group', '_label': 'Yale University Library'}]}], 'classified_as': [{'id': 'https://lux.collections.yale.edu/data/concept/89630361-18a3-4c4b-bcd7-16894d95defd', 'type': 'Type', '_label': 'System-Assigned Number'}]} is not valid under any of the given schemas
  Error 2: / --> Additional properties are not allowed ('_links' was unexpected)
```

### Textual Work

- Documentation: https://linked.art/api/1.0/endpoint/textual_work/
- Schema: https://linked.art/api/1.0/schema/text.json 

#### Linked Art Endpoint Example

- https://linked.art/example/text/0.json

```bash
-----------------------
Processing: https://linked.art/example/text/0.json
  Validation failed. Validation errors:
  Error 1: /created_by/carried_out_by/0 --> {'type': 'Person', '_label': 'Hayes, John'} is not valid under any of the given schemas
  Error 2: /used_for/0/took_place_at/0 --> 'id' is a required property
  Error 3: /used_for/0/carried_out_by/0 --> {'type': 'Group', '_label': 'Phaidon'} is not valid under any of the given schemas
```

#### LUX

- https://lux.collections.yale.edu/data/text/0000075c-f59a-419e-8d92-cb41565b5a18

```bash
-----------------------
Processing: https://lux.collections.yale.edu/data/text/0000075c-f59a-419e-8d92-cb41565b5a18
  Validation failed. Validation errors:
  Error 1: /identified_by/1 --> {'type': 'Identifier', 'content': 'ils:yul:14996707', 'attributed_by': [{'type': 'AttributeAssignment', 'carried_out_by': [{'id': 'https://lux.collections.yale.edu/data/group/d07b9b86-0a1e-4026-aa4c-8ecba8bbd9c9', 'type': 'Group', '_label': 'Yale University Library'}]}], 'classified_as': [{'id': 'https://lux.collections.yale.edu/data/concept/89630361-18a3-4c4b-bcd7-16894d95defd', 'type': 'Type', '_label': 'System-Assigned Number'}]} is not valid under any of the given schemas
  Error 2: / --> Additional properties are not allowed ('_links' was unexpected)
```

### Summary


## Unit to unit consistency (YCBA and YUAG)

Work in progress

## Consistency of concepts between LUX and the Getty Vocabularies 

Work in progress