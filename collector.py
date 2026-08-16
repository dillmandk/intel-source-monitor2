import json
import os
from datetime import datetime, timezone

import feedparser

from sources import SOURCES
from filters import find_categories
from scoring import calculate_score, priority_level
from locations import find_locations


OUTPUT_FILE = "articles.json"


def load_existing_articles():

    if not os.path.exists(OUTPUT_FILE):
        return []

    try:

        with open(OUTPUT_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, FileNotFoundError):

        return []


def save_articles(articles):

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            articles,
            file,
            indent=2,
            ensure_ascii=False
        )


def collect_articles():

    existing_articles = load_existing_articles()

    existing_links = {
        article["link"]
        for article in existing_articles
    }

    new_articles = []

    total_scanned = 0
    relevant_articles = 0

    for source in SOURCES:

        print(f"Collecting: {source['name']}")

        feed = feedparser.parse(source["url"])

        print(
            f"Articles available: {len(feed.entries)}"
        )

        for entry in feed.entries:

            total_scanned += 1

            title = entry.get(
                "title",
                "No title"
            )

            link = entry.get(
                "link",
                ""
            )

            published = entry.get(
                "published",
                "Unknown"
            )

            summary = entry.get(
                "summary",
                ""
            )

            text = f"{title} {summary}"

            categories = find_categories(text)

            if not categories:
                continue

            relevant_articles += 1

            locations = find_locations(text)

            score, matched_keywords = calculate_score(text)

            priority = priority_level(score)

            article = {
                "source": source["name"],
                "title": title,
                "published": published,
                "link": link,
                "categories": categories,
                "locations": locations,
                "keywords": matched_keywords,
                "score": score,
                "priority": priority,
                "collected_at": datetime.now(
                    timezone.utc
                ).isoformat()
            }

            if link and link not in existing_links:

                new_articles.append(article)

                existing_links.add(link)

                print(
                    f"NEW: {title}"
                )

    all_articles = new_articles + existing_articles

    # Keep newest 500 articles
    all_articles = all_articles[:500]

    save_articles(all_articles)

    print()
    print("==============================")
    print("COLLECTION COMPLETE")
    print("==============================")
    print(
        f"Total scanned: {total_scanned}"
    )
    print(
        f"Relevant: {relevant_articles}"
    )
    print(
        f"New articles: {len(new_articles)}"
    )
    print(
        f"Database size: {len(all_articles)}"
    )


if __name__ == "__main__":

    collect_articles()
