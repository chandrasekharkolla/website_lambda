import boto3
import json

client = boto3.client('dynamodb')
var_title = 'view_count'
def lambda_handler(event, context):
  viewcount = client.get_item(
    TableName='user_count',
    Key={
    "Id":{"N":"0"}
    }
  )
  views = viewcount["Item"]["view_count"]["N"]
  views = int(views)
  views += 1
  views = str(views)
  data = client.update_item(
    TableName='user_count',
    Key={
    "Id":{"N":"0"}
    },
    UpdateExpression="set view_count=:vc",
        ExpressionAttributeValues={
            ':vc': {"N": views}
        },
        ReturnValues="UPDATED_NEW"
  )
  # json_data=json.dumps(data)
  # print(json_data)
  # views = json_data['Items']
  response = {
      'statusCode': 200,
      'body': views,
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
  return response