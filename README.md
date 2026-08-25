# Building a Serverless Data Processing Pipeline Using AWS

## Project Overview

This project implements a serverless data processing pipeline using Amazon Web Services (AWS).

The system simulates real-time tweets related to a company. A Python producer script generates 500 fake tweets and sends them to Amazon SQS. AWS Lambda automatically processes the messages, extracts hashtags using Regular Expressions (Regex), stores structured metadata in Amazon DynamoDB, and invokes another Lambda function to archive the complete raw tweet data in Amazon S3.

Amazon CloudWatch is used to monitor the execution of the Lambda functions and verify successful processing.

## Architecture

The pipeline follows this flow:

**Python Producer → Amazon SQS → AWS Lambda (TweetProcessor) → Amazon DynamoDB**

**TweetProcessor → AWS Lambda (TweetArchiver) → Amazon S3**

**AWS Lambda → Amazon CloudWatch Logs**

## AWS Services Used

- Amazon SQS – buffers incoming tweet messages.
- AWS Lambda – processes and archives tweets without managing servers.
- Amazon DynamoDB – stores Tweet IDs and extracted hashtags.
- Amazon S3 – archives complete tweet data as JSON files.
- Amazon CloudWatch – monitors Lambda execution and logs.
- AWS IAM – provides required permissions to the Lambda functions.

## Technologies Used

- Python
- Boto3
- JSON
- Regular Expressions (Regex)
- Amazon Web Services (AWS)

## Project Components

### producer.py

Generates 500 simulated tweets containing:

- Tweet ID
- Username
- Message
- Hashtag
- Timestamp

Each tweet is converted into JSON and sent to the Amazon SQS queue.

### TweetProcessor

The TweetProcessor Lambda function is triggered by Amazon SQS.

It:

1. Reads the SQS message.
2. Parses the JSON data.
3. Extracts hashtags using Regex.
4. Stores the Tweet ID and hashtags in DynamoDB.
5. Asynchronously invokes the TweetArchiver Lambda function.

### TweetArchiver

The TweetArchiver Lambda function receives the complete tweet from TweetProcessor and stores it in Amazon S3 as a JSON file.

Example:

`tweet-451.json`

## Verification

The pipeline was tested using 500 simulated tweets.

The final test successfully produced:

- 500 processed items in the DynamoDB `Tweets` table.
- 500 archived JSON objects in the S3 `tweet-archive-v1` bucket.
- Successful processing logs in Amazon CloudWatch.
- Successful SQS message delivery from the Python producer.

Verification screenshots are available in the `screenshots` directory.

## Error Handling

The TweetProcessor Lambda handles malformed JSON and messages with missing required fields using exception handling.

Invalid messages are logged in Amazon CloudWatch instead of interrupting the complete processing workflow.

## Security

AWS IAM roles are used to provide the Lambda functions with permissions required to access SQS, DynamoDB, S3, Lambda, and CloudWatch.

No AWS access keys or secret credentials are included in this repository.

## Result

The project successfully demonstrates an event-driven serverless architecture capable of receiving, buffering, processing, storing, archiving, and monitoring simulated real-time tweet data using AWS managed services.
