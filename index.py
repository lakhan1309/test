import os
import boto3
from boto3 import Session
import json

session= Session();
client = session.client(service_name="secretsmanager")


def update_Secret(secretValue):
    token_arn='MasheryRegion1' if (os.environ['AWS_REGION']=='ap-south-1') else 'MasheryRegion2'
    mashery_arn=os.environ[token_arn];
    secret_string={"accessToken":secretValue}
    client.update_secret(SecretId=mashery_arn, SecretString=json.dumps(secret_string));
    print(client.get_secret_value(SecretId=mashery_arn)['SecretString'])
    return "success";


def renew_access_token(event,_):
    #print(client.get_Secret_value('Mashery')).
    return update_Secret("news");





