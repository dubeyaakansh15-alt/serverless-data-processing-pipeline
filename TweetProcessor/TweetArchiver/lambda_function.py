# ============================================================
# Lambda Function: TweetArchiver
# Purpose: Archive raw tweet data into Amazon S3
# ============================================================

# Import required Python libraries

import json         # Used to convert the tweet data into JSON format
import boto3        # AWS SDK for Python, used to communicate with Amazon S3


# Create an S3 client to interact with Amazon S3.
s3 = boto3.client("s3")


# Name of the S3 bucket used to archive raw tweet data.
BUCKET_NAME = "tweet-archive-v1"


# AWS Lambda handler function that receives tweet data from TweetProcessor.
def lambda_handler(event, context):

    # Store the received event as the tweet object.
    tweet = event

    # Extract the unique tweet ID from the received tweet.
    tweet_id = tweet["id"]

    # Create a unique JSON filename using the tweet ID.
    file_name = f"tweet-{tweet_id}.json"

    # Upload the complete raw tweet as a JSON object to the S3 bucket.
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=file_name,
        Body=json.dumps(tweet),
        ContentType="application/json"
    )

    # Log the archived filename in Amazon CloudWatch.
    print("Archived:", file_name)

    # Return a success response after the tweet is archived.
    return {
        "statusCode": 200,
        "body": "Tweet archived successfully"
    }
