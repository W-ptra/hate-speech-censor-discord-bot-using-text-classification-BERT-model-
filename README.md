# hate-speech-censor-discord-bot-using-text-classification-BERT-model
Discord bot integrated with Transformer base model BERT for Text classification detect hate speech on Discord channel. Any user message that classified as hate speech will be deleted.  
# Model  
There are 4 model available:  
1. [BERT base](https://huggingface.co/wisnu001binus/hate_speech_detection_BERTbase)
2. [DistilBERT base](https://huggingface.co/wisnu001binus/hate_speech_detection_DistilBERTbase)
3. [ALBERT base](https://huggingface.co/wisnu001binus/hate_speech_detection_ALBERTbase)
4. [RoBERTa base](https://huggingface.co/wisnu001binus/hate_speech_detection_RoBERTabase)

Each Model have been fine-tuned using 726.120 text sample for text classification  
# How to Use?
1. Clone repository  
``git clone https://github.com/W-ptra/hate-speech-censor-discord-bot-using-text-classification-BERT-model.git``  
2. Edit ``.env`` file replace ``TOKEN`` with your real discord bot token  