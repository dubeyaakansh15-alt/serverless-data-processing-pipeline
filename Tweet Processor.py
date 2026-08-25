# ============================================================
# Lambda Function: TweetProcessor
# Purpose: Process tweets from SQS, extract hashtags,
#          store metadata in DynamoDB, and invoke TweetArchiver
# ============================================================

# Import required Python libraries

import json         # Used to convert JSON messages into Python objects
import re           # Used to extract hashtags from tweet messages using Regex
import boto3        # AWS SDK for Python, used to communicate with AWS services


# Create a DynamoDB resource to interact with Amazon DynamoDB.
dynamodb = boto3.resource("dynamodb")

# Connect to the DynamoDB table used to store processed tweet metadata.
table = dynamodb.Table("Tweets")


# Create a Lambda client to invoke the TweetArchiver function.
lambda_client = boto3.client("lambda")


# Lambda handler function triggered by messages arriving in Amazon SQS.
def lambda_handler(event, context):

    # Process each SQS message received by the Lambda function.
    for record in event["Records"]:

        try:
            # Convert the SQS message body from JSON into a Python dictionary.
            tweet = json.loads(record["body"])

            # Display the Tweet ID and SQS Message ID for tracking in CloudWatch.
            print(
                "Tweet ID:",
                tweet["id"],
                "| SQS Message ID:",
                record["messageId"]
            )

            # Extract hashtags from the tweet message using a regular expression.
            hashtags = re.findall(r"#\w+", tweet["message"])

            # Store the Tweet ID and extracted hashtags in DynamoDB.
            table.put_item(
                Item={
                    "TweetID": tweet["id"],
                    "hashtags": hashtags
                }
            )

            # Invoke TweetArchiver asynchronously and send the raw tweet
            # so that it can be archived in Amazon S3.
            lambda_client.invoke(
                FunctionName="TweetArchiver",
                InvocationType="Event",
                Payload=json.dumps(tweet).encode("utf-8")
            )

            # Log successful processing in Amazon CloudWatch.
            print(
                "Stored in DynamoDB and sent to archiver:",
                tweet["id"]
            )

        # Handle malformed JSON or messages with missing required fields.
        except (json.JSONDecodeError, KeyError) as error:
            print("Invalid message skipped:", error)

    # Return a success response after processing the SQS messages.
    return {
        "statusCode": 200,
        "body": "Processing completed"
    }
