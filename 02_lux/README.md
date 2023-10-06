# 2. LUX Data Consistency

## Syntax

Testing the Linked Art JSON validator and the schemas with data coming from the [Linked Art API Endpoints](https://linked.art/api/1.0/endpoint/) and [LUX](https://lux.collections.yale.edu/).

### Concept

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

### Digital Object

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

### Event

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



## Unit to unit consistency (YCBA and YUAG)

Work in progress

## Consistency of concepts between LUX and the Getty Vocabularies 

Work in progress