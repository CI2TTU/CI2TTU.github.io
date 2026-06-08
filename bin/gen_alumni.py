#!/usr/bin/env python3
"""Generate _data/alumni.yml from alumni.csv.

CSV columns: Student, Project Title, Points. The Points value is the degree type:
  0.03125 -> M.Sc. Thesis
  0.0625  -> M.Sc. Project
  0.04    -> Undergraduate Project

Rules:
  - Deduplicate by student name. If a person has more than one row, the
    highest-ranked degree wins: thesis > M.Sc. project > undergraduate project
    (degree + title both come from the winning row).
  - Skip people who are current lab members (listed in _data/members.yml) so
    nobody appears as both a current member and an alumnus.
  - "FNU" (a placeholder for a missing name) is dropped from display names.

Re-run after editing alumni.csv:  python3 bin/gen_alumni.py
"""
import csv
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, "alumni.csv")
OUT_PATH = os.path.join(ROOT, "_data", "alumni.yml")

# Points value -> degree category, with rank for dedup (higher wins).
THESIS_POINTS = 0.03125
MASTERS_PROJECT_POINTS = 0.0625
UNDERGRAD_PROJECT_POINTS = 0.04
CATEGORY_RANK = {"thesis": 3, "masters_project": 2, "undergrad_project": 1}

# Current members (from _data/members.yml) — excluded from alumni.
CURRENT_MEMBERS = {"makarenko volodymyr", "volodymyr makarenko"}

# The roster lists most names "Surname Given [Given2 ...]", so the default
# First-Last normalization moves the first token to the end. These two sets
# handle the exceptions:
#   KEEP_AS_IS    — already in First-Last order (or a single name), leave alone.
#   NAME_OVERRIDES — the simple flip is wrong (e.g. Hispanic two-surname names).
KEEP_AS_IS = {"Phu Nguyen", "Jihyeok Choi", "Anas Muhammad", "Alavi Khan", "Ankur"}
NAME_OVERRIDES = {
    "Blas Urrutia Wilber": "Wilber Blas Urrutia",
    "Melarcode Kallampad Vaishak": "Vaishak Melarcode Kallampad",
}

# M.Sc. thesis students, looked up on SJSU ScholarWorks (scholarworks.sjsu.edu).
# Keyed by the raw CSV name; "name" is the authoritative name from the thesis page
# (overrides the best-effort First-Last flip), plus graduation year and thesis URL.
# Add more rows as theses are found; projects aren't on ScholarWorks so they have none.
THESIS_INFO = {
    "Alavi Khan":     {"name": "Alavi Ahmed Khan", "year": 2023, "url": "https://scholarworks.sjsu.edu/etd_theses/5452/"},
    "Phu Nguyen":     {"name": "Phu C. Nguyen",    "year": 2023, "url": "https://scholarworks.sjsu.edu/etd_theses/5466/"},
    "Sharma Suruchi": {"name": "Suruchi Sharma",   "year": 2023, "url": "https://scholarworks.sjsu.edu/etd_theses/5473/"},
    "Kaya Ezgi":      {"name": "Ezgi Kaya",        "year": 2024, "url": "https://scholarworks.sjsu.edu/etd_theses/5512/"},
    "Mello Paul Jason": {"name": "Paul Jason Mello", "year": 2024, "url": "https://scholarworks.sjsu.edu/etd_theses/5517/"},
    "Papala Himaja":  {"name": "Himaja Papala",    "year": 2024, "url": "https://scholarworks.sjsu.edu/etd_theses/5522/"},
    "Pal Ankit":      {"name": "Ankit Pal",        "year": 2024, "url": "https://scholarworks.sjsu.edu/etd_theses/5603/"},
    "Shrestha Enosh": {"name": "Enosh Shrestha",   "year": 2024, "url": "https://scholarworks.sjsu.edu/etd_theses/5608/"},
}

# Public LinkedIn profiles, found via web search and confirmed against SJSU + field.
# Keyed by raw CSV name. Applies to thesis and project alumni alike.
ALUMNI_LINKEDIN = {
    "Kaya Ezgi":      "https://www.linkedin.com/in/ezgi-kaya-a6b3a2127/",
    "Mello Paul Jason": "https://www.linkedin.com/in/pauljasonmello",
    "Phu Nguyen":     "https://www.linkedin.com/in/phu-nguyen-560747146/",
    "Papala Himaja":  "https://www.linkedin.com/in/papala-himaja/",
    "Sharma Suruchi": "https://www.linkedin.com/in/suruchi22sharma",
    "Shrestha Enosh": "https://www.linkedin.com/in/enoshshr",
    "Bains Simran":   "https://www.linkedin.com/in/simran-bains-87833b164/",
    "Bhavsar Janmejay Umeshkumar": "https://www.linkedin.com/in/janmejaybhavsar27/",
    "Jihyeok Choi":   "https://www.linkedin.com/in/jihyeok-choi/",
    "Edupuganti Naga Venkata Sai Sathwik": "https://www.linkedin.com/in/sathwikedupuganti/",
    "Gujavarthy Prabhath Reddy": "https://www.linkedin.com/in/prabhath-gujavarthy/",
    "Gumphekar Mugdha Shailesh": "https://www.linkedin.com/in/mugdha-gumphekar/",
    "Kadiyala Anjali Sreeja": "https://www.linkedin.com/in/anjalikadiyala19/",
    "Melarcode Kallampad Vaishak": "https://www.linkedin.com/in/vaishak-kallampad/",
    "Kulkarni Anish Shriram": "https://www.linkedin.com/in/anish-kulkarni-90a598162/",
    "Leeper Matthew": "https://www.linkedin.com/in/matthewleeper/",
    "Mahmood Muhammed Hassan": "https://www.linkedin.com/in/muhammed-hassan-mahmood/",
    "Mathakar Aomkar Anant": "https://www.linkedin.com/in/aomkar-mathakar-0575b7168/",
    "Mathew Abraham": "https://www.linkedin.com/in/abe-mathew-se/",
    "Mok Maximilian": "https://www.linkedin.com/in/max-mok-024146180/",
    "Naredla Divija": "https://www.linkedin.com/in/divijanaredla/",
    "Natarajan Kishore Kumaar": "https://www.linkedin.com/in/kishorekumaar/",
    "Nekkanti Srikara Mohana Sai Sachin": "https://www.linkedin.com/in/sachin-nekkanti/",
    "Padhye Prasanjit": "https://www.linkedin.com/in/prasanjit-padhye/",
    "Penmatsa Tirupati Venkata Sri Sai Rama": "https://www.linkedin.com/in/rajuptvs/",
    "Tati Sudheer":   "https://www.linkedin.com/in/sudheer-tati-975756167/",
    "Vallabhaneni Viswamithra": "https://www.linkedin.com/in/viswamithra-vallabhaneni/",
    "Yella Subhadra Ranga Swamy": "https://www.linkedin.com/in/subhadray",
    "Yenugadhati Abhiram": "https://www.linkedin.com/in/abhiram-yenuga/",
}


def clean_name(raw):
    tokens = [t for t in raw.strip().split() if t.upper() != "FNU"]
    return " ".join(tokens)


def classify(points):
    """Map the Points value to a degree category."""
    try:
        p = float(points)
    except (TypeError, ValueError):
        return "masters_project"
    if abs(p - THESIS_POINTS) < 1e-9:
        return "thesis"
    if abs(p - UNDERGRAD_PROJECT_POINTS) < 1e-9:
        return "undergrad_project"
    return "masters_project"  # 0.0625 (and any unexpected value)


def to_first_last(name):
    """Best-effort 'Surname Given...' -> 'Given... Surname'."""
    if name in NAME_OVERRIDES:
        return NAME_OVERRIDES[name]
    if name in KEEP_AS_IS:
        return name
    toks = name.split()
    if len(toks) < 2:
        return name
    return " ".join(toks[1:] + toks[:1])


def main():
    people = {}  # name -> {"title": str, "category": str}
    with open(CSV_PATH, newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            name = clean_name(row.get("Student", ""))
            if not name:
                continue
            title = (row.get("Project Title") or "").strip()
            category = classify(row.get("Points"))

            prev = people.get(name)
            if prev is None or CATEGORY_RANK[category] > CATEGORY_RANK[prev["category"]]:
                # Higher-ranked degree wins (thesis > M.Sc. project > undergrad project).
                people[name] = {"title": title, "category": category}

    groups = {"thesis": [], "masters_project": [], "undergrad_project": []}
    for name, rec in people.items():
        if name.lower() in CURRENT_MEMBERS:
            continue
        info = THESIS_INFO.get(name, {})
        entry = {"name": info.get("name") or to_first_last(name), "title": rec["title"]}
        if info.get("year"):
            entry["year"] = info["year"]
        if info.get("url"):
            entry["url"] = info["url"]
        if ALUMNI_LINKEDIN.get(name):
            entry["linkedin"] = ALUMNI_LINKEDIN[name]
        groups[rec["category"]].append(entry)

    # Sort each group by surname (last word of the display name), then full name.
    sort_key = lambda p: (p["name"].split()[-1].lower(), p["name"].lower())
    for group in groups.values():
        group.sort(key=sort_key)

    lines = [
        "# Auto-generated by bin/gen_alumni.py from alumni.csv — do not edit by hand.",
        "# Re-run after editing alumni.csv:  python3 bin/gen_alumni.py",
    ]
    for key in ("thesis", "masters_project", "undergrad_project"):
        lines.append(f"{key}:")
        for p in groups[key]:
            lines.append(f"  - name: {json.dumps(p['name'], ensure_ascii=False)}")
            lines.append(f"    title: {json.dumps(p['title'], ensure_ascii=False)}")
            if p.get("year"):
                lines.append(f"    year: {p['year']}")
            if p.get("url"):
                lines.append(f"    url: {json.dumps(p['url'], ensure_ascii=False)}")
            if p.get("linkedin"):
                lines.append(f"    linkedin: {json.dumps(p['linkedin'], ensure_ascii=False)}")
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print("Wrote {}: {} thesis, {} M.Sc. project, {} undergrad project".format(
        OUT_PATH, len(groups["thesis"]), len(groups["masters_project"]),
        len(groups["undergrad_project"])))


if __name__ == "__main__":
    main()
