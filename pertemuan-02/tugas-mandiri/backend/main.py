import requests

BASE = "https://httpbin.org"

print("--- 1. Testing GET Request ---")
r_get = requests.get(f"{BASE}/get", params={"nama": "Umar", "nim": "018"})
print(r_get.json())

print("\n--- 2. Testing POST Request ---")
r_post = requests.post(f"{BASE}/post", json={"kegiatan": "Praktikum PBP", "modul": "HTTP API"})
print(r_post.json())

print("\n--- 3. Testing PUT Request ---")
r_put = requests.put(f"{BASE}/put", json={"status": "Update data", "semester": 4})
print(r_put.json())

print("\n--- 4. Testing PATCH Request ---")
r_patch = requests.patch(f"{BASE}/patch", json={"status": "Partial update"})
print(r_patch.json())

print("\n--- 5. Testing DELETE Request ---")
r_delete = requests.delete(f"{BASE}/delete", params={"id": "18"})
print(r_delete.json())