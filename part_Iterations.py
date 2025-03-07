
def partDescription_count(partList, gt1_count, gt2_count, gt3_count):
    for desc in partList.keys():
        if "GT1" in desc:
            gt1_count += 1
        elif "GT2" in desc:
            gt2_count += 1
        elif "GT3" in desc:
            gt3_count += 1
    return gt1_count, gt2_count, gt3_count

def priceDescription_total(partList, gt1_price, gt2_price, gt3_price):
    for desc, price in partList.items():
        if "GT1" in desc:
            gt1_price += float(price)
        if "GT2" in desc:
            gt2_price += float(price)
        if "GT3" in desc:
            gt3_price += float(price)
    return gt1_price, gt2_price, gt3_price

gt1_count = 0
gt2_count = 0
gt3_count = 0

gt1_price = 0
gt2_price = 0 
gt3_price = 0

rascoParts = {'RASCO,#123, GT1': 150.20, 'RASCO,#145, GT3' : 155.27, 'RASCO,#124, GT2' : 125.78, 'RASCO,#125, GT1': 150.20, 'RASCO,#1425, GT3' : 155.27, 'RASCO,#24, GT2' : 125.78, 'RASCO,#126, GT1': 150.20, 'RASCO,#1445, GT3' : 155.27, 'RASCO,#14, GT2' : 125.78, 'RASCO,#127, GT1': 150.20, 'RASCO,#1465, GT3' : 155.27, 'RASCO,#12, GT2' : 125.78}

gt1_count, gt2_count, gt3_count = partDescription_count(rascoParts, gt1_count, gt2_count, gt3_count)
gt1_price, gt2_price, gt3_price = priceDescription_total(rascoParts, gt1_price, gt2_price, gt3_price)

print(f"GT1 Total Count {gt1_count} : ${gt1_price}")
print(f"GT2 Total Count {gt2_count} : ${gt2_price}")
print(f"GT3 Total Count {gt3_count} : ${gt3_price}")


def inventory_count(part_inventory):
    for dc, inventory in part_inventory.items():
        if inventory == 0:
            print(f"Out of Stock!: {dc}, 0")
        elif inventory < 200:
            print(f"Iventory Low: {dc}, {inventory}")
        elif inventory <= 1000:
            print(f"Inventory Stable: {dc}, {inventory}")
        elif inventory > 1000:
            print(f"Overstocked: {dc}, {inventory}")


part_6990000001 = {'NY': 1500, 'BN': 1250, 'EG': 190, 'DA': 980, 'PO': 654}
part_6990000002 = {'NY': 150, 'BN': 950, 'EG': 2190, 'DA': 80, 'PO': 773}
part_6990000003 = {'NY': 500, 'BN': 250, 'EG': 590, 'DA': 0, 'PO': 954}

inventory_count(part_6990000001)
inventory_count(part_6990000002)
inventory_count(part_6990000003)
