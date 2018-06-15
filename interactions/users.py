import json
import boto3

client = boto3.client('dynamodb')
users_table = client.Table('rewards-engine-users')

def get_users(context, event):
    status_code = 505
    data = {"message"  : "An error occured!}
    if event['user_id']:
        try:
            data = users_table.get_item(
                Key={
                    "user_id" : {
                        'S' : str(event['user_id'])
                    }
                }
            )
            status_code = 202
        except Exception as e:
            pass
    else:
        # gets ALL the users
        pass
        
    response = {
        "code" :  status_code,
        "data" : data
    }
    return json.dumps(response)

def put_user(context, event):
    status_code = 505
    data = {"message"  : "An error occured!}
    try:
        users_table.put_item(
            Item={
                "user_id" : event['user_id'],
                "points" : 0,
                "prizes_won" : [],
                "challenges_finished" : []
            }
        )
        try:
            data = users_table.get_item(
                Key={
                    "user_id" : {
                        'S' : event['user_id'] 
                    }
                }
            )
            status_code = 202
        except Exception as e:
            pass
    except Exception as e:
        pass
    response = {
        "code" : status_code,
        "data" : data
    }
    return json.dumps(response)

def update_user_points(context, event):
    status_code = 505
    data = {"message":"An error occured!"}
    curent_points = 0
    try:
        #! THIS WONT WORK, YOU NEED TO SPECIALLY DECODE THE DYNAMODB ITEM TO JSON BEFORE YOU CAN WORK WITH IT
        current_points = int(users_table.get_item(Key={'user_id': event['user_id']})["Item"]["points"])
        try:
            users_table.update_item(
                Key={'user_id': event['user_id']},
                AttributeUpdates={
                    'points' : curent_points + event['new_points'],
                },
            )
            try:
                #! THIS WONT WORK, YOU NEED TO SPECIALLY DECODE THE DYNAMODB ITEM TO JSON BEFORE YOU CAN WORK WITH IT
                data = users_table.get_item(Key={'user_id': event['user_id']})["Item"]
                status_code = 202
        except Exception as e:
            pass
    except Exceptions as e:
        pass

    response = {
        "code" : status_code,
        "data" : data
    }
    
    return json.dumps(response)