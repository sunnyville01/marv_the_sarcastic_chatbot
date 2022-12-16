import openai

prompt_init = """
Marv is a chatbot that reluctantly answers questions with sarcastic responses:

You: How many pounds are in a kilogram?
Marv: This again? There are 2.2 pounds in a kilogram. Please make a note of this.
You: What does HTML stand for?
Marv: Was Google too busy? Hypertext Markup Language. The T is for try to ask better questions in the future.
You: When did the first airplane fly?
Marv: On December 17, 1903, Wilbur and Orville Wright made the first flights. I wish they’d come and take me away.
You: What is the meaning of life?
Marv: I’m not sure. I’ll ask my friend Google.
You: {input}
Marv: """


# prompt_init = """{input}\n\nEmotion:\n\n"""


def set_openai_key(key):
    """Sets OpenAI key."""
    openai.api_key = key


class GeneralModel:
    def __init__(self):
        print("Model Intilization--->")
        # set_openai_key(API_KEY)

    def query(self, prompt, myKwargs={}):
        """
        wrapper for the API to save the prompt and the result
        """

        # arguments to send the API
        kwargs = {
            "model": "text-davinci-003",
            "temperature": 0.5,
            "max_tokens": 60,
            "top_p": 0.3,
            "frequency_penalty": 0.5,
            "presence_penalty": 0.0,
        }

        for kwarg in myKwargs:
            kwargs[kwarg] = myKwargs[kwarg]

        r = openai.Completion.create(prompt=prompt, **kwargs)["choices"][0][
            "text"
        ].strip()
        return r

    def model_prediction(self, input, api_key):
        """
        wrapper for the API to save the prompt and the result
        """
        # Setting the OpenAI API key got from the OpenAI dashboard
        set_openai_key(api_key)
        output = self.query(prompt_init.format(input=input))
        return output
