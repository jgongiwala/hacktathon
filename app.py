import openai
from flask import Flask, render_template, request
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Read the API key from environment variable
api_key = os.getenv('API_KEY')

# Set the API key
openai.api_key = api_key

# # Set up your OpenAI API key
# openai.api_key = 'YOUR_API_KEY'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['search_query']

    # Use ChatGPT for search response
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f"Search: {query}\n",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    search_result = response.choices[0].text.strip()

    return render_template('index.html', search_result=search_result)

if __name__ == '__main__':
    app.run()
