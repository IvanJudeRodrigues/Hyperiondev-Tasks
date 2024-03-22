
# make a list of items available on the menu
menu_list=["eggs","bacon","toast","tea", "coffee"]
# create a dictionary of items on the menu and how much stock there is
stock_dict={"eggs":72, "bacon":50,"toast":24,"tea":100, "coffee":50}
# ctreate a dictionary of menu items and their purchase cost
prices_dict={"eggs":1, "bacon":2,"toast":0.5,"tea":1.50, "coffee":2}
# initialising total_value_of_stock
total_value_of_stock=0
# for each item on menu list mutiply by stock quantity to get item value
for item in (menu_list):
    value_of_item=stock_dict[item]*prices_dict[item]
# add item values to get total value of stock
    total_value_of_stock+=(value_of_item)
print(total_value_of_stock)



