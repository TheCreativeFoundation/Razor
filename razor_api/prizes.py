from __future__ import print_function
import json
import boto3

prizes_table = boto3.resource("dynamodb").Table("razor-engine-prizes")

def put_prizes(context, event):
    status_code = 505
    data = {"message":"An error occured"}
    try:
        data = prizes_table.put_item(
            Item={
                "prize_id" : event["prize_name"],
                "name" : event["prize_name"],
                "description" : event["description"],
                "points_needed" : event["points_needed"],
                "status" : True
                }
            )
        status_code = 202
    except Exception as e:
        print(e) # LOGGER
    return {"code":status_code,"data":data}

def get_prizes(context, event):
    status_code = 505
    data = {"message":"An error occured"}
    if event["prize_id"]:
        try:
            data = prizes_table.get_table(
                Item={
                    "prize_id" : event["prize_id"]
                }    
            )
            status_code = 202
        except Exception as e:
            print(e)
    else:
        # GETS ALL THE PRIZES
        pass
    return {"code":status_code,"data":data}

def post_prizes(context, event):
    status_code = 505
    data = {"message":"An error occured"}
    try:
        pass
    except Exception as e:
        pass

def post_prizes_status(context, event):
    status_code = 505
    data = {"message":"An error occured"}
    try:
        data = prizes_table.update_item(
            Key={
                "prize_name" : event["prize_name"]
            },
            UpdateExpression="set status = :status",
            ExpressionAttributeValues={ 
                ":status": event["status"]
                }
            )
    except Exception as e:
       print(e)
    return {"code":status_code,"data":data}

