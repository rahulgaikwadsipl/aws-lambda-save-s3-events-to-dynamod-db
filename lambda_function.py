import boto3 #you need to download boto3 sdk in same folder of you function
from uuid import uuid4

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event,context):
        print (event)
        for record in event['Records']:
              bucket_name = record['s3']['bucket']['name']
              object_key = record['s3']['object']['key']
              size = record['s3']['object'].get('size', -1)
              event_name = record['eventName']
              event_time = record['eventTime']
              dynamodb.Table('my-table').put_item(Item={'RequestId':str(uuid4()),'Bucket': bucket_name, 'Object': object_key, 'Size':    size, 'Event': event_name, 'EventTime':event_time } )
              #here you need to put your dynamoDB table name in place of my-table  
