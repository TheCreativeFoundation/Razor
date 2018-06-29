from __future__ import print_function
import json
import boto3
import hashlib
from boto.dynamodb2.table import Table

users_table = boto3.resource("dynamodb").Table("razor-users-test")
deserializer = boto3.dynamodb.types.TypeDeserializer()

def get_users(context, event):
    status_code = 505
    data = {"message": "An error occured!"}
    if event["user_id"]:
        try:
            data = users_table.get_item(Key={"user_id": event["user_id"]})
            status_code = 202
        except Exception as e:
            print(e)
    else:
        # gets ALL the users
        # BATCH GET or something
        pass
    return json.dumps({"code": status_code, "data": data})

def put_users(context, event):
    status_code = 505
    data = {"message": "An error occured!"}
    try:
        data = users_table.put_item(
            Item={
                "user_id": event["user_id"],
                "current__points": 0,
                "prizes_won": [],
                "challenges_finished": [],
                }
        )
        status_code = 202
    except Exception as e:
        pass
    return json.dumps({"code": status_code, "data": data})

def post_user_prizes_won(context, event):
    pass

def post_user_challenges_finished(context, event):
    pass

def post_user_points(context, event):
    status_code = 505
    data = {"message": "An error occured!"}
    curent_points = 0
    try:
        #! THIS WONT WORK, YOU NEED TO SPECIALLY DECODE THE DYNAMODB ITEM TO JSON BEFORE YOU CAN WORK WITH IT
        current_points = int(
            users_table.get_item(Key={"user_id": event["user_id"]})["Item"]["current_points"]
        )
        try:
            data = users_table.update_item(
                Key={"user_id": event["user_id"]},
                AttributeUpdates={"current_points": curent_points + event["new_points"]},
            )
            status_code = 202
        except Exception as e:
            pass
    except Exception as e:
        pass
    return {"code": status_code, "data": data}