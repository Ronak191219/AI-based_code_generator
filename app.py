from flask import Flask, render_template, request
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Secure API key
client = OpenAI(api_key=os.getenv("self-openai-api-key"))

@app.route("/", methods=["GET", "POST"])
def index():
    generated_code = ""

    if request.method == "POST":
        prompt = request.form["prompt"]

        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": "You are a Python code generator."},
                    {"role": "user", "content": prompt}
                ]
            )

            generated_code = response.choices[0].message.content

        except Exception as e:
            print("Error:", e)  # terminal में error दिखेगा
            generated_code = "⚠️ Error: API quota exceeded or invalid key"

    return render_template("index.html", code=generated_code)

if __name__ == "__main__":
    app.run(debug=True)