import os
import json
import time
import requests
from dotenv import load_dotenv



def check_job_status(job_id, headers):
    max_retries = 3
    retry_delay = 3
    attempt = 0

    while attempt < max_retries:
        try:
            response = requests.get(f'https://api.runpod.ai/v2/enk70ps1zefqmp/status/{job_id}', headers=headers)
            response.raise_for_status()

            request_status = response.json().get("status")

            if request_status != "COMPLETED":
                print("Sabar miskin, masih diproses, santai, Santai, SANTAI")
                time.sleep(retry_delay)
                attempt += 1
            else:
                request_output = response.json().get("output")
                print("Terimakasih sudah sabar Bos!")
                print("HEEDOOP JOKOWIIIII !!!")
                print(request_output)
                return request_output

        except Exception as e:
            print(f"Request gagal (percobaan {attempt + 1}/{max_retries}): {str(e)}")
            attempt += 1
            if attempt < max_retries:
                time.sleep(retry_delay)
            else:
                print(f"Gagal ngefetch api setelah {max_retries} percobaan")
                return None

dotenv_path = "env/.env"
load_dotenv(dotenv_path=dotenv_path)

api_key = os.getenv("api_key")

headers = {
    'Content-Type': 'application/json',
    'Authorization': api_key
}

data = {
    'input': {"prompt":"Your Fist Serverless Endpoint Bruh"}
}

response = requests.post('https://api.runpod.ai/v2/enk70ps1zefqmp/run', headers=headers, json=data)

job_id = response.json().get("id")
request_status = response.json().get("status")

headers = {
    'Authorization': api_key
}

check_job_status(job_id, headers)