import os
import discord
from dotenv import load_dotenv
from transformers import pipeline,BertForSequenceClassification, BertTokenizer

#load environment variable
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Loading model, tokenizer
model_path = "BERT model"
model = BertForSequenceClassification.from_pretrained(model_path)
tokenizer = BertTokenizer.from_pretrained(model_path)

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
    
    # delete message if classified as hatespeech
    if label == "hatespeech":
        await message.delete()
        await message.channel.send("message deleted")
    
# Run the bot with your token
client.run(TOKEN)