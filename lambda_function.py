import boto3
import json
import os
import logging
import sys

logger = logging.getLogger(__name__)
out_hdlr = logging.StreamHandler(sys.stdout)
out_hdlr.setLevel(logging.INFO)
logger.addHandler(out_hdlr)
logger.setLevel(logging.INFO)

record = os.environ['ENV_VAR_DYN_DB_VALUE']

client = boto3.client('dynamodb')
var_title = 'view_count'
def lambda_handler(event, context):
  logger.info('Update the counter by 1')
  data = client.update_item(
    TableName='siteVisits',
    Key={
      'id':{'S':record}
    },
    UpdateExpression='SET visits = visits + :inc',
      ExpressionAttributeValues={
        ':inc': {'N': '1'}
      },
      ReturnValues="UPDATED_NEW"
  )
  # response = {
  #     'statusCode': 200,
  #     'body': data,
  #     'headers': {
  #       'Content-Type': 'application/json',
  #       'Access-Control-Allow-Origin': '*'
  #     },
  # }
  
  # return response