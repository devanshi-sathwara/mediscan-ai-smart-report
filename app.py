from flask import Flask, render_template, request
from langchain_groq import ChatGroq

app = Flask(__name__)

# 🔥 Add your Groq API Key here
llm = ChatGroq(
    api_key="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",
    model="llama-3.3-70b-versatile"
)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("report")

        if not file:
            return render_template("index.html", error="No file uploaded")

        try:
            report = file.read().decode("utf-8")

            # 🔥 AI PROMPT
            prompt = f"""
            You are a medical expert.
            Analyze the following medical report and give:
            - Possible disease
            - Symptoms
            - Suggestions

            Report:
            {report}
            """

            response = llm.invoke(prompt)

            final_diagnosis_text = response.content

            return render_template("index.html", diagnosis=final_diagnosis_text)

        except Exception as e:
            return render_template("index.html", error=str(e))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)