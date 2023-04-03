import requests


# r = requests.get("http://127.0.0.1:5000")
# print(r.status_code)
# print(r.text)

# r = requests.get("http://127.0.0.1:5000/time")
# print(r.status_code)
# print(r.text)

# r = requests.get("http://127.0.0.1:5000/date")
# print(r.status_code)
# print(r.text)

# out_data = {"date": "10/10/1999", "units": "years"}
# r = requests.post("http://127.0.0.1:5000/age", json=out_data)
# print(r.status_code)
# print(r.text)

r = requests.get("http://127.0.0.1:5000/until_next_meal/lunch")
print(r.status_code)
print(r.text)
