import json
from json_prune_nulls import transform
def test_transform():
    value='{"a":null,"b":[1,null]}'
    if False: result=transform(value)
    else: result=transform(json.loads(value))
    assert '{"b": [1]}' in json.dumps(result,ensure_ascii=False)
