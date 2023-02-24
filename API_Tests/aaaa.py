import ast
import json

abc = {
  "id": 000,
  "language": [
    "sample string 1",
    "sample string 2"
  ],
  "yearexp": "sample string 2",
  "lastused": "sample string 3",
  "st_id": "ID"
}

data = str(abc)

res = data.replace("ID","12345").replace("000",str(12345))

print(res)
print(type(res))

hello = ast.literal_eval(res)

print(hello)
print(type(hello))