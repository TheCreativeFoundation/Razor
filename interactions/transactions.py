import boto3
import hashlib
import datetime

transactions_table = boto3.resource("dynamodb").Table("razor_transactions")
client = boto3.client('dynamodb')
paginator = client.get_paginator('scan')

def put_transactions(context, event):
    status_code = 505
    data = {"message":"An error occured!"}
    try:
        data = transactions_table.put_item(
            Item={
                "transaction_id" : hashlib.sha256(str(event["user_id"] + datetime.datetime.now())).hexdigest(),
                "metadata" : {
                    "user_id" : event["user_id"],
                    "points_before" : event["points_before"],
                    "points_after" : event["points_after"],
                    "event" : event["event"]
                    } 
                }
            )
        status_code = 202
    except Exceptiono as e:
        pass
    return {"code":status_code, "data":data}