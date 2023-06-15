import openai
from flask import Flask, render_template, request

# Set up your OpenAI API key
openai.api_key = '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'

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
