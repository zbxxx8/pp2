import json
print("Interface Status")
print('=======================================================================================')
print('DN                                                 Description           Speed    MTU  ')
print('-------------------------------------------------- --------------------  ------  ------')
with open("1.json","r") as f:
    data=json.load(f)
all=data["imdata"]
for i in all:
    for j in i.values():
        if j["attributes"]["dn"][-3] == "/":
            print(j["attributes"]["dn"], "                             ", j["attributes"]["speed"], " ", j["attributes"]["mtu"])
        else:
            print(j["attributes"]["dn"], "                            ", j["attributes"]["speed"], " ", j["attributes"]["mtu"])