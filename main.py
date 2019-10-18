import base64
import json
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()
service = discovery.build('compute', 'v1', credentials=credentials)

"""
Supported products for labels are:
BigQuery | Cloud Bigtable | Cloud Dataproc | Cloud Deployment Manager | Cloud Functions | Cloud Healthcare API | Cloud Key Management Service | Cloud Pub/Sub | Cloud Spanner | Cloud SQL | Cloud Storage | Compute Engine | Google Kubernetes Engine | Cloud Run (fully managed) | Networking |  Resource Manager
Function Currently Supports:
GCE | Cloud SQL | Cloud Functions | Big Query | PubSub

Default tags:
Created By, Instance Name, Created Date/Time
"""

def autotag(event, context):
    print("""This Function was triggered by messageId {} published at {}
    """.format(context.event_id, context.timestamp))

    if 'data' in event:
        name = base64.b64decode(event['data']).decode('utf-8')
    else:
        name = 'World'
    print('Hello {}!'.format(name))


def AddPubSub(LabelList,Project,Target,Zone):
    instances_set_labels_request_body = json.dumps(LabelList)
    request = settings.userLabels


def AddBQLabel(LabelList,Project,Target,Zone):
    instances_set_labels_request_body = json.dumps(LabelList)
    request = settings.userLabels


def AddGCELabel(LabelList,Project,Target,Zone):
    instances_set_labels_request_body = json.dumps(LabelList)

    request = service.instances().setLabels(project=Project, zone=Zone, instance=Target, body=instances_set_labels_request_body)
    response = request.execute()

def AddCSQLLabel(LabelList,Project,Target,Zone):
    instances_set_labels_request_body = json.dumps(LabelList)
    request = settings.userLabels

def AddCFLabel(LabelList,Project,Target,Zone):

    instances_set_labels_request_body = json.dumps(LabelList)
    request = settings.userLabels

def main():
  print("Hello World!")

if __name__== "__main__":
  AddGCELabel({"creator":"rick"},"ricks-sandbox","instance-1","us-west1")
