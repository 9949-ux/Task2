inventory = []

def find_item(item_id):
    return next((item for item in inventory if item["id"] == item_id), None)

def update_item(item_id, new_data):
    item = find_item(item_id)
    if item:
        item.update(new_data)
        return item
    return None

def delete_item(item_id):
    global inventory
    item = find_item(item_id)
    if item:
        inventory = [i for i in inventory if i["id"] != item_id]
        return {"message": "Item deleted", "id": item_id}
    return None
