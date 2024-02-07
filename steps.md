# Steps 


> *These are the steps which were followed when creating this project and repository. Based on [this YouTube tutorial](https://www.youtube.com/watch?v=qMIM7dECAkc) by Krish Naik.*


## 1. Environment set-up 

### Create a conda environment and activate it

```
$ conda create -p venv python==3.9 --y
$ conda activate venv
```

### Download the requirements 

First, create the `requirements.txt` file: 

```
# requirements.txt
langchain
openai
huggingface_hub
python-dotenv
streamlit
```

Download the requirements:

```
$ pip install -r requirements.txt 
```

**Separately** install `ipykernel`:
(we need this library to run Jupyter Lab notebooks, but we do not need it for the deployment in the cloud) 

```
$ pip install ipykernel
```

### Create an `.env` file that will hold our keys 

Create the file:

```
$ vi .env
```

For now, write the following (we will fill it out with our key later): 

```
# .env
OPENAI_API_KEY=""
```

### Create a Jupyter Lab notebook for practice

Create a notebook, and name it `langchain.ipynb`.


## 2. Create an OpenAI secret key and a Huggingface token

### OpenAI secret key 

1. Go to [openai.com/blog/openai-api](https://openai.com/blog/openai-api)
2. Sign up or sign into your account
3. Go to "Usage" - make sure you have some credits
    - If not, add $5.00 or so 
4. Go to "API Keys" - create a secret key
5. Copy the secret key, and paste it into the `.env` file (you will need to paste it into the Jupyter Lab notebook later too)

### Huggingface token 

1. Go to [huggingface.co/](https://huggingface.co/)
2. Sign up or sign into your account
3. Go to "Settings" --> "Access Tokens"
4. Generate a new token
5. Copy the secret key, and paste it into the `.env` file (you will need to paste it into the Jupyter Lab notebook later too)


## 3. Work on the Jupyter Lab notebook for practice 

(Follow the YouTube tutorial) 

Complete notebook: [/langchain.ipynb](/langchain.ipynb)


## 4. Create the application 

(Follow the YouTube tutorial) 

Complete script: [/app.py](/app.py)


## 5. Deploy to Huggingface

1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Click on "Create new Space"
3. Enter the details
    - Name the space
    - No license 
    - Choose "Streamlit"
    - Choose the free CPU tier (`CPU basic 2 vCPU 16 GB FREE`)
    - Choose public 
4. Go to settings, and scroll down to **Variables and secrets**
   - Create a "New secret"
   - Add the API key 
5. Go to the "Files" page and add:
   - `app.py`
   - `requirements.txt`
6. Go the "App" page, the application should start building and running 
