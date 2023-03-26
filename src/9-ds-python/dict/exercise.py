bd_division_info ={}
bd_division_info["barisal"] = {"district": 6, "upazilla": 39, "council": 333}
bd_division_info["chittagong"] = {"district": 11, "upazilla": 97, "council": 336}
bd_division_info["dhaka"] = {"district": 13, "upazilla": 93, "council": 1833}
bd_division_info["khulna"] = {"district": 10, "upazilla": 59, "council": 270}
bd_division_info["mymensingh"] = {"district": 4, "upazilla": 34, "council": 350}
bd_division_info["rajshahi"] = {"district": 8, "upazilla": 70, "council": 558}
bd_division_info["rangpur"] = {"district": 8, "upazilla": 58, "council": 536}
bd_division_info["shylet"] = {"district": 4, "upazilla": 38, "council": 334}

zilla = 0
upazilla = 0
union = 0

for item in bd_division_info:
    zilla += bd_division_info[item]['district']
    upazilla += bd_division_info[item]['upazilla']
    union  += bd_division_info[item]['council']

print(zilla, upazilla, union)