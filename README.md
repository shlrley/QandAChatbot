# Simple Q and A Chatbot


![QandA](https://github.com/shlrley/QandAChatbot/assets/70875076/93c39c52-8ad3-491a-803e-4b6c7e26aed2)

Visit the page here: [huggingface.co/spaces/shlrley/QandAChatbot](https://huggingface.co/spaces/shlrley/QandAChatbot)


## About 

**This project implements a Chatbot that users can ask simple questions to.** The responses are generated using the power of large language models (LLMs), specifically the `gpt-3.5-turbo-instruct` model from OpenAI. The app utilizes tools from the LangChain framework, and is deployed on Huggingface Spaces. 

This project was created by following this [tutorial](https://www.youtube.com/watch?v=qMIM7dECAkc&list=PLZoTAELRMXVORE4VF7WQ_fAl0L1Gljtar&index=5) by Krish Naik on YouTube. 

## Requirements 

```
langchain
openai
huggingface_hub
python-dotenv
streamlit
```

## Usage 

If you would like to run the `app.py` script from this repository locally, please follow the steps below:

1. Clone the repository and move into the directory 

```
$ git clone https://github.com/shlrley/QandAChatbot.git
```

2. Create and activate the virtual environment 

```
$ conda create -p venv python==3.9 --y
$ conda activate venv
```

3. Install the requirements

```
$ pip install -r requirements.txt
```

4. Run the application

```
$ streamlit run app.py
```

*To tun the Jupyter Lab Notebook (Optional):*

5. Open the Jupyter Lab notebook, and make sure the correct environment is chosen (top right, `venv`)

6. Replace the `"ENTER-YOUR-API-KEY-HERE"` sections with your own OpenAI and Huggingface api keys (see [steps.md](/steps.md) for more details) 

7. Run each cell one by one 

For detailed step-by-step instructions on how this repository was created, please see: [steps.md](/steps.md)

## References 

Code, notebooks, and ideas in this repository were adapted from the following [YouTube tutorial](https://www.youtube.com/watch?v=qMIM7dECAkc&list=PLZoTAELRMXVORE4VF7WQ_fAl0L1Gljtar&index=5) by Krish Naik. 
