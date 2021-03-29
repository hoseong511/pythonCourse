# mutable sequence

days = ["mon", "tue", "wed", "thur", "fri"]

print("mon" in days)

# immutable sequence : tuple

days = ("mon", "tue", "wed", "thur", "fri")

# dictionary, object Mgmt
hoho = {
  "name" : "ho",
  "age" : "20",
  "fav_food" : ["kimchi","ham"],
  "car" : False
}
hoho["fav_food"].append("chicken")
hoho["age"] = 25
print(hoho)