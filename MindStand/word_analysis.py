import spacy

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

nlp = spacy.load("en_core_web_sm")

MODEL_INPUT_KEY = "model_input"
MODEL_OUTPUT_KEY_SENT = "model_output_sent"
MODEL_OUTPUT_KEY_NOUN = "model_output_noun"
MODEL_OUTPUT_KEY_VERB = "model_output_verb"
MODEL_OUTPUT_KEY_ADJ = "model_output_adj"
MODEL_OUTPUT_KEY_COMP = "model_output_comp"
MODEL_OUTPUT_KEY_NEG = "model_output_neg"
MODEL_OUTPUT_KEY_NEU = "model_output_neu"
MODEL_OUTPUT_KEY_POS = "model_output_pos"
input_data = "there"


class SpacyAnalysis:
    def __init__(self):
        pass
    
    def run(self,input_data):
        
           self.model_input = input_data
           model_input = nlp(self.model_input)
           
           model_output_nouns = [token.text for token in model_input if token.pos_ == "NOUN"]
           model_output_verbs = [token.text for token in model_input if token.pos_ == "VERB"]
           model_output_adj = [token.text for token in model_input if token.pos_ == "ADJ"]
           
           ret_spacy = {MODEL_OUTPUT_KEY_NOUN:model_output_nouns,
                        MODEL_OUTPUT_KEY_VERB:model_output_verbs,
                        MODEL_OUTPUT_KEY_ADJ:model_output_adj}         
           
           return ret_spacy


class SentimentAnalysis:
    
    def __init__(self):
        pass
    
    def run(self,input_data):
        
           sid_obj = SentimentIntensityAnalyzer()
           sentiment_dict = sid_obj.polarity_scores
           
           self.model_input = input_data
           model_input = self.model_input
           
           model_output_neg = sentiment_dict(model_input)['neg']
           model_output_pos = sentiment_dict(model_input)['neu']
           model_output_neu = sentiment_dict(model_input)['pos']
           model_output_com = sentiment_dict(model_input)['compound']
           
           ret_sentiment = {MODEL_OUTPUT_KEY_COMP:model_output_com,
                            MODEL_OUTPUT_KEY_NEG:model_output_neg,
                            MODEL_OUTPUT_KEY_NEU:model_output_pos,
                            MODEL_OUTPUT_KEY_POS:model_output_neu}
          
           return ret_sentiment
       
rec1 = SentimentAnalysis()
rec2 = SpacyAnalysis()
print(rec1.run(input_data))
print(rec2.run(input_data))