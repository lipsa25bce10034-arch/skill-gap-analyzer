import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
try:
    df = pd.read_csv("jobs.csv")
except:
    print(" Error: jobs.csv file not found!")
    exit()

# Check columns
if "Job Role" not in df.columns or "Skills" not in df.columns:
    print(" Error: jobs.csv must contain 'Job Role' and 'Skills' columns")
    exit()

# User input
print("\n=== SKILL GAP ANALYZER ===")
student_skills = input("Enter your skills (space separated): ").lower().strip()

if student_skills == "":
    print(" No input provided!")
    exit()

# Prepare data
documents = df["Skills"].astype(str).tolist()
documents.append(student_skills)

# TF-IDF
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(documents)

# Similarity
similarity = cosine_similarity(vectors[-1], vectors[:-1])

print("\n--- Job Match Results ---\n")

results = []

# Display results
for i in range(len(df)):
    job_role = df.iloc[i]["Job Role"]
    score = similarity[0][i] * 100
    results.append((job_role, score))
    print(f"{job_role}: {score:.2f}% match")

# Best match
best_index = similarity.argmax()
best_job = df.iloc[best_index]["Job Role"]

print("\nBest Matched Job Role:", best_job)

# Skill gap analysis
print("\n--- Skill Gap Analysis ---\n")

student_set = set(student_skills.split())

for i in range(len(df)):
    job_role = df.iloc[i]["Job Role"]
    job_skills = set(str(df.iloc[i]["Skills"]).split())

    matched = job_skills.intersection(student_set)
    missing = job_skills - student_set

    print(f"{job_role}:")
    print("Matched Skills:", ", ".join(matched) if matched else "None")
    print("Missing Skills:", ", ".join(missing))
    print()

# Top 3 jobs
print("--- Top 3 Recommended Roles ---\n")

results.sort(key=lambda x: x[1], reverse=True)

for role, score in results[:3]:
    print(f"{role} ({score:.2f}%)")

print("\n✅ Done!")
