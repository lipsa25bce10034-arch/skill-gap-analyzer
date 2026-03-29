# Simple Skill Gap Analyzer (No libraries required)

# Job dataset (inside code)
jobs = {
    "Data Scientist": ["python", "machine learning", "statistics", "pandas", "numpy"],
    "Web Developer": ["html", "css", "javascript", "react", "nodejs"],
    "Data Analyst": ["python", "sql", "excel", "powerbi", "statistics"],
    "Software Engineer": ["java", "python", "data structures", "algorithms"],
    "AI Engineer": ["python", "machine learning", "deep learning", "tensorflow"]
}

print("\n=== SKILL GAP ANALYZER ===")

# User input
student_input = input("Enter your skills (space separated): ").lower()

if student_input.strip() == "":
    print("No skills entered!")
    exit()

student_skills = student_input.split()

print("\n--- Job Match Results ---\n")

results = []

# Compare skills
for job, skills in jobs.items():
    matched = set(student_skills).intersection(skills)
    match_percent = (len(matched) / len(skills)) * 100

    results.append((job, match_percent))

    print(f"{job}: {match_percent:.2f}% match")

# Best match
best_job = max(results, key=lambda x: x[1])[0]
print("\nBest Matched Job Role:", best_job)

# Skill gap
print("\n--- Skill Gap Analysis ---\n")

for job, skills in jobs.items():
    matched = set(student_skills).intersection(skills)
    missing = set(skills) - set(student_skills)

    print(f"{job}:")
    print("Matched Skills:", ", ".join(matched) if matched else "None")
    print("Missing Skills:", ", ".join(missing))
    print()

# Top 3 roles
print("--- Top 3 Recommended Roles ---\n")

results.sort(key=lambda x: x[1], reverse=True)

for job, score in results[:3]:
    print(f"{job} ({score:.2f}%)")

print("\nDone!")
