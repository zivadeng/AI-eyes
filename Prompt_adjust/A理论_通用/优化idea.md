## python 验证json schema是否符合要求,不符合再调用LLM修改。
```python
import jsonschema
from jsonschema import validate

# 定义 JSON Schema
schema = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "minLength": 2,
            "maxLength": 50
        },
        "age": {
            "type": "integer",
            "minimum": 0,
            "maximum": 150
        },
        "email": {
            "type": "string",
            "format": "email"
        },
        "hobbies": {
            "type": "array",
            "items": {
                "type": "string"
            }
        }
    },
    "required": ["name", "age", "email"]
}

# 定义要验证的 JSON 数据
data = {
    "name": "John Doe",
    "age": 30,
    "email": "johndoe@example.com",
    "hobbies": ["reading", "swimming"]
}

try:
    validate(instance=data, schema=schema)
    print("JSON 数据符合 Schema")
except jsonschema.exceptions.ValidationError as e:
    print(f"JSON 数据不符合 Schema: {e}")
    ```