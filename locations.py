LOCATIONS = {

    "United States": [
        "united states",
        "u.s.",
        "america"
    ],

    "Russia": [
        "russia",
        "russian"
    ],

    "Ukraine": [
        "ukraine",
        "ukrainian"
    ],

    "China": [
        "china",
        "chinese"
    ],

    "North Korea": [
        "north korea",
        "north korean"
    ],

    "South Korea": [
        "south korea",
        "south korean"
    ],

    "Iran": [
        "iran",
        "iranian"
    ],

    "Israel": [
        "israel",
        "israeli"
    ],

    "Palestinian Territories": [
        "palestine",
        "palestinian",
        "gaza",
        "west bank"
    ],

    "Taiwan": [
        "taiwan",
        "taiwanese"
    ],

    "Syria": [
        "syria",
        "syrian"
    ],

    "Iraq": [
        "iraq",
        "iraqi"
    ],

    "Afghanistan": [
        "afghanistan",
        "afghan"
    ],

    "Turkey": [
        "turkey",
        "turkish"
    ],

    "United Kingdom": [
        "united kingdom",
        "britain",
        "british"
    ],

    "Australia": [
        "australia",
        "australian"
    ],

    "India": [
        "india",
        "indian"
    ],

    "Pakistan": [
        "pakistan",
        "pakistani"
    ],

    "NATO": [
        "nato"
    ]
}


def find_locations(text):

    text = text.lower()

    found = []

    for location, keywords in LOCATIONS.items():

        for keyword in keywords:

            if keyword in text:

                found.append(location)
                break

    return found
