import json
import time
import pandas as pd
from requests import get, post

def recognizer2DF(post_url, apim_key, headers, data_bytes, confidence_threshold = 0, query_interval=5):
    """
    Submits Table or Form to recognizer asyncronously and processes the response
    queryInterval amount of time to wait between checking whether a job is done
    Optional confidence_threshold to deterimine whether to process a extracted feild
    """
    try:
        # Submit Async Table Job to Form Recognizer Endpoint
        resp = post(url = post_url, data = data_bytes, headers = headers)
        if resp.status_code == 202:
            # Query Submit Table Job
            get_url = resp.headers["operation-location"]
            resp = get(url = resp.headers["operation-location"], headers = {"Ocp-Apim-Subscription-Key": apim_key})
            resp_json = json.loads(resp.text)
            while resp_json["status"] == "running":
                resp = get(url = get_url, headers = {"Ocp-Apim-Subscription-Key": apim_key})
                resp_json = json.loads(resp.text)
                time.sleep(query_interval)
            if resp_json["status"] == "succeeded":
                # Process Documents
                docResults = resp_json['analyzeResult']['tables'][0]
                cols = docResults['columnCount']
                rows = docResults['rowCount']
                docs = [([""] * cols) for j in range(rows)]
                for doc in docResults['cells']:
                    content = doc['content']
                    ci = doc['columnIndex']
                    ri = doc['rowIndex']
                    docs[ri][ci] = content
                return pd.DataFrame(docs)
            elif resp_json["status"] == "failed":
                print("Layout analyze failed:\n%s" % resp_json)
        else:
            print("POST analyze failed:\n%s" % resp.text)
    except Exception as e:
        print("Code Failed analyze failed:\n%s" % str(e))

# Endpoint URL
with open('.env/apim_key.txt', "r") as f:
    apim_key = f.readline()
endpoint =  r"https://formlinger.cognitiveservices.azure.com/"
source = r"./image.png"
url = endpoint + r"/formrecognizer/documentModels/prebuilt-layout:analyze?api-version=2022-08-31"

headers = {
    # Request headers
    # 'Content-Type': r'<form file type - application/pdf, image/jpeg, image/png, or image/tiff>',
    'Content-Type': r'image/png',
    'Ocp-Apim-Subscription-Key': apim_key,
}

with open(source, "rb") as f:
    data_bytes = f.read()

df = recognizer2DF(url, apim_key, headers, data_bytes)
df.to_csv(".output/form_data.csv") # can now be processed with excel
