# -*- coding: utf-8 -*-
"""chat_bot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qnjyskPXAmXpTT10Mzp32P5HDq2j6Vm-
"""

pip install openai

import openai

openai.api_key = "Your API"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me 3 ideas for apps I could build with openai apis "}])
print(completion.choices[0].message.content)

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give the roadmap to become the best software engineer "}])
print(completion.choices[0].message.content)