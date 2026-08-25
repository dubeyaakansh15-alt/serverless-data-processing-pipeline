#============================================================================================================================================================================================
#Title:- Building a Serverless Data Processing Pipeline Using AWS
#Domain:- Cloud Computing
#Platform:- Amazon Web Services (AWS)
#Language:- Python
#============================================================================================================================================================================================

# Import required Python libraries

import random       # Used to randomly select usernames, messages, and hashtags
import json         # Used to convert Python dictionaries into JSON format
import boto3        # AWS SDK for Python, used to communicate with Amazon SQS

from datetime import datetime  # Used to generate the timestamp for each tweet

# Create an SQS client in the AWS region where the queue is deployed.
sqs = boto3.client("sqs", region_name="ap-southeast-2")

# URL of the SQS queue used to buffer incoming tweet messages.
queue_url = "YOUR_SQS_QUEUE_URL"

# Sample usernames used to generate fake tweets.
username = ["rahul123","tech_lover","alex45","coffee_addict","priya_codes","rohan_07","sammywrites","daily_avi","neha_tech","coding_ninja","arjunrocks","travel_with_me","dev_guy99","ananya_18",
  "foodie_forever","mike_dev","random_thoughts","shreya_22","cloud_learner","vicky_online","techie_101","music_fan","aditya_codes","movie_buff","sneha_world","python_beginner",
  "rohit_1999","gaming_zone","kriti_says","data_enthusiast","aman_here","bookworm_21","startup_mind","ishita_07","curious_mind","devraj_codes","nature_lover","varun_tech","weekend_vibes",
  "kavya_writes","cloud_explorer","sid_rocks","coding_daily","megha_23","future_dev","harsh_tweets","tech_world","nikhil_101","just_chillin"]

# Sample tweet messages used for the simulation.
messages = ["The company launched a redesigned mobile application today.","The company's customer support team resolved my issue quickly.",
            "The latest product update introduced several useful features.","The company's website seems much faster after the recent update.",
            "Really impressed with the company's new mobile app design.","The company announced a new product launch for next month.",
            "Customer service responded to my complaint within a few hours.","The company's latest software update fixed the login problem.",
            "The new dashboard released by the company looks clean and simple.","The company added several new features to its online platform.",
            "Had a great experience contacting the company's support team today.","The company's website was temporarily unavailable this morning.",
            "The latest app update seems more stable than the previous version.","The company announced improvements to its customer support system.",
            "The company's new interface is much easier to navigate.","Waiting for the company to fix the payment issue on its website.",
            "The company released an update addressing several reported bugs.","The new product from the company looks interesting so far.",
            "The company's customer service team was very helpful today.","The company's mobile application crashed while I was placing an order.",
            "The company has improved the loading speed of its website.","Really enjoying the features introduced in the company's latest update.",
            "The company announced scheduled maintenance for its platform tonight.","The company's support team answered all my questions clearly.",
            "The new website design from the company looks much better than before.","The company's application needs some improvement in performance.",
            "The company introduced a new feature based on customer feedback.","The company's latest update made the application easier to use.",
            "Customer support took longer than expected to respond today.","The company fixed the issue I reported earlier this week.",
            "The company's new product received a major update today.","The company is testing several new features on its platform.",
            "The company's website navigation has improved significantly.","The latest company update added better security features.",
            "The company's support team handled my refund request smoothly.","The company announced changes to its mobile application today.",
            "The company's website is experiencing some performance issues today.","The latest product update from the company looks promising.",
            "The company added a new payment option to its website.","The company's customer support experience has improved recently.",
            "The company released a patch to fix several application bugs.","The company's new dashboard provides useful information.",
            "The company announced that its services will be upgraded this weekend.","The company's application is working much better after the update.",
            "The new feature introduced by the company saved me a lot of time.","The company's website checkout process is much smoother now.",
            "The company responded quickly to reports about the recent service issue.","The company's latest product release has some interesting features.",
            "The company improved the search feature on its website.","Overall, I had a good experience using the company's service today."]

# Hashtags corresponding to the sample tweet messages.
hashtags = ["#MobileApp","#CustomerSupport","#ProductUpdate","#WebsitePerformance","#AppDesign","#ProductLaunch","#CustomerService","#BugFix","#Dashboard","#NewFeatures","#SupportTeam",
            "#WebsiteDown","#AppUpdate","#CustomerSupport","#UserInterface","#PaymentIssue","#BugFix","#NewProduct","#CustomerService","#AppCrash","#WebsiteSpeed","#NewFeatures",
            "#Maintenance","#SupportTeam","#WebsiteDesign","#AppPerformance","#CustomerFeedback","#AppUpdate","#CustomerSupport","#IssueResolved","#ProductUpdate","#NewFeatures",
            "#WebsiteUpdate","#SecurityUpdate","#CustomerSupport","#AppChanges","#WebsitePerformance","#ProductUpdate","#PaymentOption","#CustomerSupport","#BugFix","#Dashboard",
            "#ServiceUpgrade","#AppUpdate","#NewFeature","#Checkout","#ServiceIssue","#ProductLaunch","#WebsiteSearch","#CustomerExperience"]
# Generate and send 500 simulated tweets to Amazon SQS.
for i in range(500):
    # Select a random message while keeping its corresponding hashtag.
    index = random.randrange(len(messages))
    # Generate the timestamp for the current tweet.
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Create the tweet as a Python dictionary.
    tweet = {
    "id": i + 1,
    "username": random.choice(username),
    "message": messages[index] + " " + hashtags[index],
    "timestamp": timestamp
    }
    # Convert the Python dictionary into JSON format.
    tweet_json = json.dumps(tweet)
    # Send the JSON tweet to the Amazon SQS queue.
    response = sqs.send_message(QueueUrl=queue_url,MessageBody=tweet_json)
    # Display confirmation and the unique SQS Message ID.
    print("Tweet_number :-",i + 1,"sent! Message ID :-",response["MessageId"])
    print("\ntweet sent successfully.")
    print("-"*75)



