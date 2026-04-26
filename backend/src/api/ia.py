from transformers import pipeline


class AIHandler:
    def __init__(self, model_name="distilgpt2"):
        self.generator = pipeline("text-generation", model=model_name)

    def process_input(self, text):
        results = self.generator(
            text, max_length=100, truncation=True, pad_token_id=50256
        )
        return results[0]["generated_text"]


ai_engine = AIHandler()
