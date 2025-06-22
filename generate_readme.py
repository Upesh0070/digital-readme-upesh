def collect_info():
    print("\n🎤 Welcome to your Digital README Generator\n")
    name = input("🧑 What’s your name (e.g., Upesh)? ")
    tagline = input("🌟 Your personal tagline (e.g., Exploring AI x Storytelling)? ")
    bio = input("📜 Short bio (1–2 lines about you): ")
    socials = input("🔗 Links (comma-separated, e.g., Instagram, Twitter): ")
    skills = input("🛠️ Skills (comma-separated, e.g., Python, AI, Branding): ")
    projects = input("🚀 Projects (comma-separated, e.g., AI File Assistant, Digital Menu): ")
    current_goal = input("🎯 Current goal (what you’re building/learning): ")

    return {
        "name": name,
        "tagline": tagline,
        "bio": bio,
        "socials": socials.split(","),
        "skills": skills.split(","),
        "projects": projects.split(","),
        "goal": current_goal
    }

def format_readme(info):
    socials_formatted = " | ".join(f"[{s.strip()}](https://{s.strip()})" for s in info['socials'])

    return f"""# 👋 Hey, I'm {info['name']}

**{info['tagline']}**

{info['bio']}

---

## 🔧 Skills
{', '.join(f'`{skill.strip()}`' for skill in info['skills'])}

## 🚀 Projects
{chr(10).join(f"- {proj.strip()}" for proj in info['projects'])}

## 🌐 Socials
{socials_formatted}

## 🎯 Current Goal
> {info['goal']}

---

_This README was auto-generated using a Python script._ ✨
"""

def save_readme(content):
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("\n✅ README.md successfully created!")

if __name__ == "__main__":
    user_info = collect_info()
    final_markdown = format_readme(user_info)
    save_readme(final_markdown)
