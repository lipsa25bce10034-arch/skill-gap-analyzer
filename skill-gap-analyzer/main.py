import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("jobs.csv")

student_skills = input("Enter your skills: ").lower()

documents = df["Skills"].tolist() + [student_skills]

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(documents)

similarity = cosine_similarity(vectors[-1], vectors[:-1])

print("\nJob Match Results:\n")
for i, row in df.iterrows():
    print(f"{row['Job Role']}: {similarity[0][i]*100:.2f}% match")

best_index = similarity.argmax()
print("\nBest Job Role:", df.iloc[best_index]["Job Role"])

print("\nSkill Gap:\n")
student_set = set(student_skills.split())

for i, row in df.iterrows():
    job_skills = set(row["Skills"].split())
    missing = job_skills - student_set

    print(f"{row['Job Role']}: {', '.join(missing)}")
