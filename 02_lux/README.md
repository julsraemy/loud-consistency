# 2. LUX Data Consistency

## Syntax

Testing the Linked Art JSON validator and the schemas with data coming from the [Linked Art API Endpoints](https://linked.art/api/1.0/endpoint/) and [LUX](https://lux.collections.yale.edu/).

### Concept

#### Linked Art Endpoint

#### LUX

- https://lux.collections.yale.edu/data/concept/000052b6-a350-4bcb-afca-15dceb72920a

```bash
-----
Processing: https://lux.collections.yale.edu/data/concept/000052b6-a350-4bcb-afca-15dceb72920a
  Validated!
```

### Textual Work

- Documentation: https://linked.art/api/1.0/endpoint/textual_work/
- Schema: https://linked.art/api/1.0/schema/text.json 

#### Linked Art Endpoint

```bash
-----
Processing: https://linked.art/example/text/0.json
  /created_by/carried_out_by/0 --> {'type': 'Person', '_label': 'Hayes, John'} is not valid under any of the given schemas 
  /used_for/0/took_place_at/0 --> 'id' is a required property 
  /used_for/0/carried_out_by/0 --> {'type': 'Group', '_label': 'Phaidon'} is not valid under any of the given schemas 
```

#### LUX

- https://lux.collections.yale.edu/data/text/0000075c-f59a-419e-8d92-cb41565b5a18

```bash

-----
Processing: https://lux.collections.yale.edu/data/text/0000075c-f59a-419e-8d92-cb41565b5a18
  /identified_by/1 --> {'type': 'Identifier', 'content': 'ils:yul:14996707', 'attributed_by': [{'type': 'AttributeAssignment', 'carried_out_by': [{'id': 'https://lux.collections.yale.edu/data/group/d07b9b86-0a1e-4026-aa4c-8ecba8bbd9c9', 'type': 'Group', '_label': 'Yale University Library'}]}], 'classified_as': [{'id': 'https://lux.collections.yale.edu/data/concept/89630361-18a3-4c4b-bcd7-16894d95defd', 'type': 'Type', '_label': 'System-Assigned Number'}]} is not valid under any of the given schemas
```

- https://lux.collections.yale.edu/data/text/00001cef-e016-418e-ba8d-84d2375d663a

```bash
---
Processing: https://lux.collections.yale.edu/data/text/00001cef-e016-418e-ba8d-84d2375d663a
  Validation failed. Validation errors:
errs: [<ValidationError: "Additional properties are not allowed ('_links' was unexpected)">]

```

## Unit to unit consistency (YCBA and YUAG)

Work in progress

## Consistency of concepts between LUX and the Getty Vocabularies 

Work in progress