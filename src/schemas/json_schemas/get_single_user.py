SINGLE_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {"type": "integer", "enum": [1, 2, 3, 4, 5, 6]},
                "email": {"type": "string"},
                "first_name": {"type": "string", "enum": ["George", "Janet", "Emma", "Eve", "Charles", "Tracey"]},
                "last_name": {"type": "string", "enum": ["Bluth", "Weaver", "Wong", "Holt", "Morris", "Ramos"]},
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
