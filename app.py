from flask import Flask, render_template, request
import re

app = Flask(__name__)
SKILLS = ["python", "java", "sql", "excel", "power bi", "machine learning",
          "pandas", "numpy", "html", "css", "javascript", "react",
          "communication", "problem solving", "data analysis", "flask"]

def find_skills(text):
    text = text.lower()
    return [skill for skill in SKILLS if re.search(r"\\b" + re.escape(skill) + r"\\b", text)]

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        resume = request.files.get("resume")
        job = request.form.get("job_description", "")
        if not resume or not resume.filename:
            result = {"error": "Please choose a resume text file."}
        elif not resume.filename.lower().endswith(".txt"):
            result = {"error": "This starter version accepts .txt files only."}
        else:
            text = resume.read().decode("utf-8", errors="ignore")
            found = find_skills(text)
            wanted = find_skills(job)
            matched = sorted(set(found) & set(wanted))
            missing = sorted(set(wanted) - set(found))
            score = round(len(matched) / len(set(wanted)) * 100) if wanted else 0
            result = {"score": score, "matched": matched, "missing": missing,
                      "found": sorted(found),
                      "note": "This is a basic keyword comparison, not a real ATS score."}
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
