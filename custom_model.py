
from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
import json

load_dotenv()

endpoint = os.getenv("endpoint")
key = os.getenv("key")


model_id = "Mouser"
formUrl = "https://docintelnomaddemo.blob.core.windows.net/docinteldocs/mouser_quote_QF13C4C.pdf"

document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

# Make sure your document's type is included in the list of document types the custom model can analyze
poller = document_analysis_client.begin_analyze_document_from_url(model_id, formUrl)
result = poller.result()

docs = result.documents[0]
document_dict = docs.to_dict()
# Extracting specific fields
confidence = document_dict.get("confidence")
doc_type = document_dict.get("doc_type")

#print(f"Confidence: {confidence}")
#print(f"Document Type: {doc_type}")

# List available fields
available_fields = document_dict.keys()

#print("Available fields:")
#for field in available_fields:
#    print(field)

# List fields within the 'fields' dictionary
fields_dict = document_dict.get("fields", {})
#available_subfields = fields_dict.keys()

#print("Available subfields in 'fields':")


json_file = "rows.json"
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(fields_dict, f, ensure_ascii=False, indent=4)

