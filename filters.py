KEYWORDS = {
    "military": [
        "military",
        "troops",
        "soldiers",
        "army",
        "navy",
        "air force",
        "missile",
        "missiles",
        "drone",
        "drones",
        "artillery",
        "tank",
        "tanks",
        "weapon",
        "weapons",
        "defense",
        "defence"
    ],

    "conflict": [
        "war",
        "attack",
        "attacks",
        "strike",
        "strikes",
        "airstrike",
        "invasion",
        "fighting",
        "combat",
        "offensive",
        "bombing",
        "shelling"
    ],

    "political": [
        "government",
        "president",
        "prime minister",
        "election",
        "sanctions",
        "diplomatic",
        "diplomacy",
        "treaty"
    ],

    "terrorism": [
        "terrorist",
        "terrorism",
        "extremist",
        "militant",
        "hostage"
    ],

    "cyber": [
        "cyberattack",
        "cyber attack",
        "hacker",
        "hackers",
        "ransomware",
        "malware",
        "data breach"
    ]
}


def find_categories(text):

    text = text.lower()

    matches = []

    for category, keywords in KEYWORDS.items():

        for keyword in keywords:

            if keyword in text:
                matches.append(category)
                break

    return matches
