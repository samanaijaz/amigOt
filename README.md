# amigOt
A chatbot made using OpenAI and Python

These are basically three chat bots made with Python and OpenAI. Installing the openai module is must for all of them.
One needs to add their API key in the code in order to run it.
Describing all of them one by one:

1) Basic.1: It is a simple chatbot which contains only 4 lines of code.
   It has no memory of the previously asked question but gives smart answer to every question by the user just like chatGPT.
   The only restriction with this one is that the question needs to be specified in the code itself and cannot be enterered as input by the user.
   The code stops executing when the answer is provided to the user.

2) Custom Assiatnt: It is another simple but efficient chatbot. The user uses the latest chatGPT model and can ask as many questions as they want.
   They first need to respond to how they want their chatbot to be, e.g., smart, funny, lazy, etc.
   The code execution stops with the "goodbye" input, until then the while loops enables us to ask the questions again and again.

3) Custom ChatGPT: This one works totally like chatGPT. User can ask the question in one section and the output is geneated on the other once the question is submitted.
   It keeps track of the questions asked and provides the output according to the query. The image of the interface is/will be provided in the repository.
