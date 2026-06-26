import json
data = '{"city":"Bangalore","state":"Karnataka","pincode":560001}'
result = json.loads(data)
print(result)
print("City =", result["city"])