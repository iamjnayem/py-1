marks = {"DH1001": {"Bangla": 74, "English": 73}, "DH1002": {"Bangla": 70, "English": 75}}
print(marks["DH1001"])
print(marks["DH1001"]["English"])
marks["DH1003"] = {"Bangla": 68, "English": 72}
print(marks)
print(marks["DH1003"])
print(marks["DH1003"]["Bangla"])