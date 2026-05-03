def validate_order(data):
    if not data:
        return "Invalid request"

    if "item" not in data:
        return "Item is required"

    if "quantity" not in data:
        return "Quantity is required"

    if not isinstance(data["quantity"], int):
        return "Quantity must be integer"

    return None