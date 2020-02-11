def reorder(inventory):
    ret = []
    for sku in inventory:
        if inventory[sku] < 20:
            ret.append(sku)
    return ret
inventory = {"100AJ":16,"151BR":0,"203YW":85,"063PQ":57}
print(reorder(inventory))