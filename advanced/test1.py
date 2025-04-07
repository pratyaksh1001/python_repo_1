from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeResult

endpoint = "https://pratyaksh-test.cognitiveservices.azure.com/"
key = "09dba76a14954211a02331b73884cc45"

docUrl = "C:\\Users\\praty\\Downloads\\Circular_20240106222029_modified_deca_cho_03-01-24.pdf"

document_analysis_client = DocumentIntelligenceClient(endpoint=endpoint,credential=AzureKeyCredential(key))

poller = document_analysis_client.begin_analyze_document_from_url("prebuilt-document", docUrl)
result: AnalyzeResult = poller.result()