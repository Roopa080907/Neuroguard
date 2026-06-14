import requests

url = "http://127.0.0.1:5000/predict"

files = {
    "file": open(r"C:\Users\roopa\OneDrive\Desktop\neuroguard\data\test\Moderate Dementia\OAS1_0308_MR1_mpr-1_100.jpg", "rb")
}

response = requests.post(url, files=files)

print(response.json())