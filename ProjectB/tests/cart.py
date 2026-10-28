def total(items):
    print("Items:", items)
    return sum(item.get("price") for item in items)