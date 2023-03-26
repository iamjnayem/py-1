bd_division_info ={}
bd_division_info["barisal"] = {"district": 6, "upazilla": 39, "council": 333}
bd_division_info["chittagong"] = {"district": 11, "upazilla": 97, "council": 336}
bd_division_info["dhaka"] = {"district": 13, "upazilla": 93, "council": 1833}
bd_division_info["khulna"] = {"district": 10, "upazilla": 59, "council": 270}
bd_division_info["mymensingh"] = {"district": 4, "upazilla": 34, "council": 350}
bd_division_info["rajshahi"] = {"district": 8, "upazilla": 70, "council": 558}
bd_division_info["rangpur"] = {"district": 8, "upazilla": 58, "council": 536}
bd_division_info["barisal"] = {"district": 4, "upazilla": 38, "council": 334}

print(bd_division_info)


divisions = bd_division_info.keys()
print(divisions)
for division in divisions:
    print("Division", division)

for division in divisions:
    print(division, "upazilla", bd_division_info[division]["upazilla"])

for item in bd_division_info:
    print(item)

for key in bd_division_info:
    print(key)
    print(bd_division_info[key])


for key, value in bd_division_info.items():
    print(key)
    print(value)