import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------------
# Load Dataset
# -------------------------------
try:
    df = pd.read_csv("jobs.csv")
except:
    print("Error: jobs.csv file not found!")
    exit()

# -------------------------------
# User Input
# -------------------------------
print("\n=== Skill Gap Analyzer ===")
student_skills = input("Enter your skills (separated by space): ").lower().strip()

if student_skills == "":
    print("Please enter at least one skill!")
    exit()

# -------------------------------
# Text Processing using TF-IDF
# -------------------------------
documents = df["Skills"].tolist() + [student_skills]

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(documents)

# -------------------------------
# Similarity Calculation
# -------------------------------
similarity = cosine_similarity(vectors[-1], vectors[:-1])

# -------------------------------
# Display Job Match Results
# -------------------------------
print("\n=== Job Match Results ===\n")

results = []

for i, row in df.iterrows():
    score = similarity[0][i] * 100
    results.append((row["Job Role"], score))
    print(f"{row['Job Role']}: {score:.2f}% match")

# -------------------------------
# Best Match
# -------------------------------
best_index = similarity.argmax()
best_job = df.iloc[best_index]["Job Role"]

print("\nBest Matched Job Role:", best_job)

# -------------------------------
# Skill Gap Analysis
# -------------------------------
print("\n=== Skill Gap Analysis ===\n")

student_set = set(student_skills.split())

for i, row in df.iterrows():
    job_skills = set(row["Skills"].split())
    missing_skills = job_skills - student_set
    matched_skills = job_skills.intersection(student_set)

    print(f"{row['Job Role']}:")
    print(f"Matched Skills: {', '.join(matched_skills) if matched_skills else 'None'}")
    print(f"Missing Skills: {', '.join(missing_skills)}\n")

# -------------------------------
# Top 3 Recommendations
# -------------------------------
print("=== Top 3 Recommended Roles ===\n")

results.sort(key=lambda x: x[1], reverse=True)

for role, score in results[:3]:
    print(f"{role} ({score:.2f}%)")

print("\nThank you for using Skill Gap Analyzer!")
