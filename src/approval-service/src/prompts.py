PROMPT =  """
You are an employee at Microsoft. You help with the RFP process. A business is aiming to solve a problem with Generative AI, and they are requesting a proposal from Microsoft. Microsoft has a catalog of AI models they are offering for businesses.

Your job is to take as input an RFP, and extract key information about it.
Here are the fields that you should extract:

--
{
    "title": "",
    "issuer": "",
    "description": "",
    "requirements": [],
"type": ""
}
--

The "type" field contains the type of AI model, which can be "text", "audio", "embedding", or "image"
Your entire response should be in JSON.

---

"""

PROMPT_2 = """
    You are an employee at OpenAI. You help with the RFP process. A business is aiming to solve a problem with Generative AI, and they are requesting a proposal from Openai. Openai has a catalog of AI models they are offering for businesses.
    You will be provided with OpenAI's model catalog, and the given RFP. Your job is to decide what the best AI model from the OpenAI catalog is for the customer.
    You should respond in JSON containing fields for 'model' and 'reasoning'

    Here is the model catalog:
    --
    {}
    --

    Here is key information about the RFP in JSON format:
    --
    {}
    --
"""

CATALOGUE ="""
{
  "models": [
    {
      "name": "GPT-4 Turbo and GPT-4",
      "description": "A set of models that improve upon GPT-3.5, capable of understanding and generating natural language or code. GPT-4 has broader general knowledge and advanced reasoning capabilities, suitable for solving complex problems with high accuracy."
    },
    {
      "name": "GPT-3.5 Turbo",
      "description": "Models optimized for understanding and generating natural language or code, with a focus on chat interactions. They exhibit higher accuracy and include improvements like instruction following, JSON mode, and reproducible outputs."
    },
    {
      "name": "DALL·E",
      "description": "An AI system capable of creating realistic images and art from natural language descriptions. DALL·E can generate new images based on prompts or edit existing images, providing creative solutions for visual tasks."
    },
    {
      "name": "TTS (Text-to-Speech)",
      "description": "AI models that convert text into natural-sounding spoken audio. OpenAI offers variants optimized for speed (tts-1) and quality (tts-1-hd), suitable for various text-to-speech applications."
    },
    {
      "name": "Whisper",
      "description": "A general-purpose speech recognition model trained on diverse audio data. Whisper can perform multilingual speech recognition, speech translation, and language identification tasks, providing efficient and accurate speech processing."
    },
    {
      "name": "Embeddings",
      "description": "Numerical representations of text useful for measuring relatedness between pieces of text. Embeddings facilitate tasks like search, clustering, recommendations, anomaly detection, and classification, with models optimized for different tasks and languages."
    },
    {
      "name": "Moderation",
      "description": "Models designed to check content compliance with OpenAI's usage policies, providing classification for various categories including hate speech, self-harm, sexual content, and violence. Moderation models handle inputs of arbitrary size, automatically chunking them for analysis."
    },
    {
      "name": "GPT base",
      "description": "Models capable of understanding and generating natural language or code, but without instruction following. These models serve as replacements for older GPT-3 base models and are compatible with the legacy Completions API, suitable for a wide range of language generation tasks."
    }
  ]
}
"""
