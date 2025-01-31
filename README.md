# hate_speech_censor_discord_bot_using_text_classification_BERT_model
![img](https://drive.google.com/uc?export=view&id=16kJCIRHLISAEROuRtgPGk20SA78eonYG)  
Discord bot integrated with Transformer base model BERT for Text classification detect hate speech on Discord channel. Any user message that classified as hate speech will be deleted.  
## Model  
There are 4 model available:  
1. [BERT base](https://huggingface.co/wisnu001binus/hate_speech_detection_BERTbase)
2. [DistilBERT base](https://huggingface.co/wisnu001binus/hate_speech_detection_DistilBERTbase)
3. [ALBERT base](https://huggingface.co/wisnu001binus/hate_speech_detection_ALBERTbase)
4. [RoBERTa base](https://huggingface.co/wisnu001binus/hate_speech_detection_RoBERTabase)
  
Each Model have been fine-tuned using **726.120** text sample for text classification  
Dataset Source: [Research paper](https://www.sciencedirect.com/science/article/pii/S2352340922010356) and [Repository](https://data.mendeley.com/datasets/9sxpkmm8xn/1)
## Prerequisite
min of ``python version 3.11.2`` or ``Docker`` installed  on your device 
## How to Use?
1. Clone repository  
```
git clone https://github.com/W-ptra/hate_speech_censor_discord_bot_using_text_classification_BERT_model.git
```  
2. Edit ``.env`` file replace ``TOKEN`` with your real discord bot token  (token can be received thru [Discord Developer Portal](https://www.bing.com/ck/a?!&&p=ebee8242a8cac48dJmltdHM9MTcyODQzMjAwMCZpZ3VpZD0zYjI0MmFhYi0yY2U5LTZkMjktMmRhYy0zZmI4MmRlODZjODEmaW5zaWQ9NTE5NQ&ptn=3&ver=2&hsh=3&fclid=3b242aab-2ce9-6d29-2dac-3fb82de86c81&psq=discord+developer+portal&u=a1aHR0cHM6Ly9kaXNjb3JkLmNvbS9kZXZlbG9wZXJz&ntb=1))
3. Run following script to change directory and run the application
```
cd hate_speech_censor_discord_bot_using_text_classification_BERT_model
python main.py
```

# Docker Usage
Run following script, replace ``TOKEN`` with your actual discord bot token (token can be received thru [Discord Developer Portal](https://www.bing.com/ck/a?!&&p=ebee8242a8cac48dJmltdHM9MTcyODQzMjAwMCZpZ3VpZD0zYjI0MmFhYi0yY2U5LTZkMjktMmRhYy0zZmI4MmRlODZjODEmaW5zaWQ9NTE5NQ&ptn=3&ver=2&hsh=3&fclid=3b242aab-2ce9-6d29-2dac-3fb82de86c81&psq=discord+developer+portal&u=a1aHR0cHM6Ly9kaXNjb3JkLmNvbS9kZXZlbG9wZXJz&ntb=1))
```
docker run -d -e TOKEN={your discord bot token} --name bot wisnup001binus/hate_speech_censor_discord_bot:1.0
```
the proccess will be done in average 5 minutes or depending on your internet collection
