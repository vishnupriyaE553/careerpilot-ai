from typing import Dict, List


def skill_gap_analyzer(current_skills: str, target_role: str) -> Dict:
    """
    Analyze the user's current skills against the target role
    and return missing skills along with a readiness score.
    """

    skill_database = {

        "software engineer": [
            "Java",
            "Python",
            "DSA",
            "OOP",
            "DBMS",
            "Operating Systems",
            "Computer Networks",
            "SQL",
            "Git",
            "REST API"
        ],

        "ai engineer": [
            "Python",
            "NumPy",
            "Pandas",
            "Matplotlib",
            "Scikit-Learn",
            "TensorFlow",
            "PyTorch",
            "Deep Learning",
            "Machine Learning",
            "SQL",
            "Git"
        ],

        "full stack developer": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Node.js",
            "Express",
            "MongoDB",
            "SQL",
            "Git",
            "REST API"
        ],

        "cloud engineer": [
            "AWS",
            "Azure",
            "Docker",
            "Kubernetes",
            "Linux",
            "Terraform",
            "Networking",
            "Git"
        ],

        "embedded engineer": [
            "C",
            "C++",
            "Microcontrollers",
            "Embedded C",
            "RTOS",
            "UART",
            "SPI",
            "I2C",
            "ARM",
            "PCB Design"
        ]
    }

    role = target_role.lower().strip()

    if role not in skill_database:
        return {
            "error": f"Role '{target_role}' is currently not supported."
        }

    current = [
        skill.strip().lower()
        for skill in current_skills.split(",")
    ]

    required = skill_database[role]

    known = []
    missing = []

    for skill in required:

        if skill.lower() in current:
            known.append(skill)
        else:
            missing.append(skill)

    readiness = round(
        (len(known) / len(required)) * 100,
        1
    )

    return {

        "Target Role": target_role,

        "Known Skills": known,

        "Missing Skills": missing,

        "Readiness Score": f"{readiness}%",

        "Recommendation":
            "Focus on learning the missing skills in the suggested order."
    }