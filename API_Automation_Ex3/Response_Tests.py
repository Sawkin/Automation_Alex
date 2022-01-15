import requests
# Test Cases: Create - post; Read - get; Update - put/patch; Delete - delete

# testing basic response and getting values:
resp = requests.get("https://ipinfo.io/161.185.160.93/geo")
print(resp.json())
# basic response code validation
code = resp.status_code
assert code == 200, "code doesn't match"
# json response and data validation:
json_response = resp.json()
assert json_response['ip'] == "161.185.160.93", "ip do not match 161.185.160.93"
assert json_response['city'] == "New York City", "city do not match New York City"
assert json_response['region'] == "New York", "region do not match New York"
assert json_response['country'] == "US", "country do not match US"
assert json_response['loc'] == "40.7152,-73.9877", "loc do not match 40.7152,-73.9877"
assert json_response['org'] == "AS22252 The City of New York", "org do not match AS22252 The City of New York"
assert json_response['postal'] == "10002", "postal do not match 10002"
assert json_response['readme'] == "https://ipinfo.io/missingauth", "readme do not match"

# testing filtering responses
resp2 = requests.get("https://ipinfo.io/8.8.8.8/org")
code2 = resp2.status_code
assert resp2.status_code == 200, "code doesn't match"
print(resp2.text)
assert resp2.text == "AS15169 Google LLC", "not matches text"






