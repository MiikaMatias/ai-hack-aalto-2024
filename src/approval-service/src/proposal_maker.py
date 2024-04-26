from openai import OpenAI
from prompts import CATALOGUE, PROMPT, PROMPT_2

client = OpenAI(api_key="sk-proj-r6qI3ffFPEIgw6scPNCwT3BlbkFJ0ZStgrw6ir1TySzYcyef")

def get_proposals(path_to_rfp):

    with open(path_to_rfp, 'r') as file:
      rfp_contents = file.read()

    prompt = PROMPT + rfp_contents

    response = client.chat.completions.create(
      model="gpt-4",
      messages=[
        {
          "role": "user",
          "content": prompt
        },
      ],
      temperature=1,
      max_tokens=670,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    extracted = response.choices[0].message.content

    prompt2 = PROMPT_2.format(CATALOGUE, extracted)


    response2 = client.chat.completions.create(
      model="gpt-4",
      messages=[
        {
          "role": "user",
          "content": prompt2
        },
      ],
      temperature=1,
      max_tokens=670,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    proposal = response2.choices[0].message.content

    return proposal
