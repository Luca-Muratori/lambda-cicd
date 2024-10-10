import json

def lambda_handler(event, function):
    return {
        'statusCode': 200,
        body: json.dump('hello from cicid lambda')
    }