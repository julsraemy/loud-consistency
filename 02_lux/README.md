# 2. LUX Data Consistency

## Testing the Linked Art JSON Validator

### Textual Work

#### Linked Art Endpoint

```bash
-----
Processing: https://linked.art/example/text/0.json
  /created_by/carried_out_by/0 --> {'type': 'Person', '_label': 'Hayes, John'} is not valid under any of the given schemas 
  /used_for/0/took_place_at/0 --> 'id' is a required property 
  /used_for/0/carried_out_by/0 --> {'type': 'Group', '_label': 'Phaidon'} is not valid under any of the given schemas 
```

#### LUX

