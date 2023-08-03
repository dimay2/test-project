# Sample code to send data to Azure Monitor using Logs ingestion API
# commit 3

# information needed to send data to the DCR endpoint
dce_endpoint = "https://log-ingestion-a4bc.eastus-1.ingest.monitor.azure.com" # ingestion endpoint of the Data Collection Endpoint object
dcr_immutableid = "dcr-5c3a252188194e1a973615bdd8fb7752" # immutableId property of the Data Collection Rule
stream_name = "Custom-MyTableRawData" #name of the stream in the DCR that represents the destination table

# Import required modules
import os
from azure.identity import DefaultAzureCredential
from azure.monitor.ingestion import LogsIngestionClient
from azure.core.exceptions import HttpResponseError

credential = DefaultAzureCredential()
client = LogsIngestionClient(endpoint=dce_endpoint, credential=credential, logging_enable=True)

body = [
        {
        "Time": "2023-03-12T15:04:48.423211Z",
        "Computer": "Computer1",
            "AdditionalContext": {
                "InstanceName": "user1",
                "TimeZone": "Pacific Time",
                "Level": 4,
                "CounterName": "AppMetric2",
                "CounterValue": 35.3    
            }
        },
        {
            "Time": "2023-03-12T15:04:48.794972Z",
            "Computer": "Computer2",
            "AdditionalContext": {
                "InstanceName": "user2",
                "TimeZone": "Central Time",
                "Level": 3,
                "CounterName": "AppMetric2",
                "CounterValue": 43.5     
            }
        }
    ]

try:
    client.upload(rule_id=dcr_immutableid, stream_name=stream_name, logs=body)
except HttpResponseError as e:
    print(f"Upload failed: {e}")