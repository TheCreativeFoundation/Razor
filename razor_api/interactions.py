import boto3
import json

def complete_challenge(context, event):
    status_code = 505
    data = {"message":"An error occured!"}
