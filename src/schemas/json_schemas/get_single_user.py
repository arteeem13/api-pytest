SINGLE_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {"type": "integer", "enum": [2]},
                "email": {"type": "string"},
                "first_name": {"type": "string", "enum": ["Janet"]},
                "last_name": {"type": "string", "enum": ["Weaver"]},
                "avatar": {"type": "string"}
            },
            "required": ["id", "email", "first_name", "last_name", "avatar"]
        },
        "support": {
            "type": "object",
            "properties": {
                "url": {"type": "string"},
                "text": {"type": "string"}
            },
            "required": ["url", "text"]
        }
    },
    "required": ["data", "support"]
}
