import json

def lambda_handler(event, context):
    print('test')
    print('test2')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda 444!')
    }