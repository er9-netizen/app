from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key="AIzaSyCdJRJCzznS8hiRdl84_M1mPiwlYGdbK3Y")

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    user_input = ""

    if request.method == "POST":
        user_input = request.form["message"]

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )

        response = completion.choices[0].message.content

    return render_template("index.html", response=response, user_input=user_input)

