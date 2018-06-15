# Razor

## A Complete Rewards Engine

A simple and serverless rewards system thats easy to implement and use!

This system used AWS Lambda and AWS DynamobDB, so if you want to use this you'll need your AWS Credentials. Because this system works with the [Serverless Framework](https://github.com/serverless/serverless) you could implement the code with Microsoft Azure, Google Cloud, IBM OpenWhisk, etc.

---

Razor supports two different earning models:

- Challenge based earning, where consumers earn points when completing Razor refers to as a challenge

    E.g. "Fill out the survey to recieve 100 points..."

- Purchase based earning, where consumers earn points when spending a certain amount

    E.g. "For every $1 spent in-store, you can earn 2 points..."

Both earning models are implemented in the Razor API with different end points to whichever one you are refering too.

Because there is a single endpoint to give a certain user points, its the same method for both earning models... the only differnce is in the front end.

---

### Documentation

#### Interactions

These are the different actions you will be able to do out-of-the box using this Rewards Engine. All of these become serverless functions that you can interface with over HTTP as a RESTful API service.

Some interactions will be both Private and Public like "View Challenges", however what both sides see could be different.

##### Private Interactions

- View challenges (GET)

`GET ../challenges`

Returns:

```[json]
{
    "challenges" : [
        {
            "challenge_id" : string,
            "challenge_secret" : string,
            "name" : string,
            "points" : int
        },
        {
            ...
        }
    ]
}
```

- Create challenges
- Delete challenges
- Change challenges

- Create users
- Delete users
- Change user information

##### Public Interactions

- View challenges
- Earn Points
- Redeem Points