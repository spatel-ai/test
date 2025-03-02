import json

def lambda_handler(event, context):
    print('test')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda 3!')
    }