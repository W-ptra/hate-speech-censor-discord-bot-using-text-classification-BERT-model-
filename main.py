'''
    Model Available:
    +=================+====================================================+
    | Model           | Repository                                         |
    +=================+====================================================+
    | BERT base       | wisnu001binus/hate_speech_detection_BERTbase       |
    | DistilBERT base | wisnu001binus/hate_speech_detection_DistilBERTbase |
    | ALBERT base     | wisnu001binus/hate_speech_detection_ALBERTbase     |
    | RoBERTa base    | wisnu001binus/hate_speech_detection_RoBERTabase    |
    +=================+====================================================+
'''
import os
import discord
from dotenv import load_dotenv
from transformers import pipeline,DistilBertForSequenceClassification, DistilBertTokenizerFast

#load environment variable
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Loading model, tokenizer
model_repository = "wisnu001binus/hate_speech_detection_DistilBERTbase"
model = DistilBertForSequenceClassification.from_pretrained(model_repository)
tokenizer = DistilBertTokenizerFast.from_pretrained(model_repository)

# Create pipeline
predict = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# Create a new bot instance
intent = discord.Intents.default()
intent.messages = True
intent.message_content = True
intent.guild_messages = True

client = discord.Client(intents=intent)

# Event triggered when the bot is ready
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

# Event triggered when a message is received
@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # text classification 
    classification = predict(message.content)
    label = classification[0]["label"]
    score = classification[0]["score"]

    #Message log
    print(f"| {label} with {score*100:.2f}% | {message.content}")
    
    # delete message if classified as hatespeech
    if label == "hatespeech":
        await message.delete()
        await message.channel.send(f"{message.author.mention} message deleted")

# Run the bot with your token
client.run(TOKEN)