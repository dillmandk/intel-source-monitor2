KEYWORD_WEIGHTS = {

    "military": 10,
    "troops": 15,
    "soldiers": 10,
    "army": 10,
    "navy": 10,
    "air force": 15,

    "missile": 25,
    "missiles": 25,
    "drone": 20,
    "drones": 20,
    "artillery": 20,

    "tank": 15,
    "tanks": 15,

    "weapon": 15,
    "weapons": 15,

    "war": 20,
    "attack": 15,
    "attacks": 20,
    "strike": 20,
    "strikes": 20,

    "airstrike": 25,
    "invasion": 30,
    "fighting": 15,
    "combat": 15,
    "offensive": 25,
    "bombing": 25,
    "shelling": 25,

    "sanctions": 15,
    "diplomatic": 10,
    "diplomacy": 10,
    "treaty": 10,

    "terrorist": 25,
    "terrorism": 30,
    "extremist": 20,
    "militant": 20,
    "hostage": 25,

    "cyberattack": 25,
    "cyber attack": 25,
    "hacker": 15,
    "hackers": 15,
    "ransomware": 25,
    "malware": 20,
    "data breach": 20
}


def calculate_score(text):

    text = text.lower()

    score = 0
    matched_keywords = []

    for keyword, weight in KEYWORD_WEIGHTS.items():

        if keyword in text:

            score += weight
            matched_keywords.append(keyword)

    if score > 100:
        score = 100

    return score, matched_keywords


def priority_level(score):

    if score >= 75:
        return "HIGH"

    elif score >= 40:
        return "MEDIUM"

    else:
        return "LOW"
