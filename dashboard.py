import json
import streamlit as st


st.set_page_config(
    page_title="Intel Source Monitor",
    page_icon="🛰️",
    layout="wide"
)


@st.cache_data
def load_articles():

    try:

        with open(
            "articles.json",
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except FileNotFoundError:

        return []


articles = load_articles()


st.title("🛰️ Intel Source Monitor")

st.caption(
    "Automated open-source information monitoring dashboard"
)


# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.header("Filters")


search = st.sidebar.text_input(
    "Search"
)


priority_filter = st.sidebar.selectbox(
    "Priority",
    [
        "ALL",
        "HIGH",
        "MEDIUM",
        "LOW"
    ]
)


category_options = sorted({

    category

    for article in articles

    for category in article.get(
        "categories",
        []
    )

})


category_filter = st.sidebar.selectbox(
    "Category",
    ["ALL"] + category_options
)


location_options = sorted({

    location

    for article in articles

    for location in article.get(
        "locations",
        []
    )

})


location_filter = st.sidebar.selectbox(
    "Location",
    ["ALL"] + location_options
)


# -----------------------------
# FILTER ARTICLES
# -----------------------------

filtered_articles = []


for article in articles:

    if search:

        searchable_text = " ".join([

            article.get("title", ""),

            " ".join(
                article.get(
                    "categories",
                    []
                )
            ),

            " ".join(
                article.get(
                    "locations",
                    []
                )
            ),

            " ".join(
                article.get(
                    "keywords",
                    []
                )
            )

        ]).lower()

        if search.lower() not in searchable_text:
            continue


    if priority_filter != "ALL":

        if article.get(
            "priority"
        ) != priority_filter:

            continue


    if category_filter != "ALL":

        if category_filter not in article.get(
            "categories",
            []
        ):

            continue


    if location_filter != "ALL":

        if location_filter not in article.get(
            "locations",
            []
        ):

            continue


    filtered_articles.append(article)


# -----------------------------
# STATISTICS
# -----------------------------

total = len(articles)

high = sum(
    1
    for article in articles
    if article.get("priority") == "HIGH"
)

medium = sum(
    1
    for article in articles
    if article.get("priority") == "MEDIUM"
)

low = sum(
    1
    for article in articles
    if article.get("priority") == "LOW"
)


col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "Total Articles",
    total
)

col2.metric(
    "HIGH",
    high
)

col3.metric(
    "MEDIUM",
    medium
)

col4.metric(
    "LOW",
    low
)


st.divider()


st.subheader(
    f"Articles ({len(filtered_articles)})"
)


# -----------------------------
# DISPLAY ARTICLES
# -----------------------------

for article in filtered_articles:

    priority = article.get(
        "priority",
        "LOW"
    )


    if priority == "HIGH":

        emoji = "🔴"

    elif priority == "MEDIUM":

        emoji = "🟠"

    else:

        emoji = "🟢"


    with st.container():

        st.markdown(
            f"### {emoji} {article.get('title', 'No title')}"
        )


        col1, col2 = st.columns(
            [3, 1]
        )


        with col1:

            st.write(
                f"**Source:** "
                f"{article.get('source', 'Unknown')}"
            )

            st.write(
                f"**Published:** "
                f"{article.get('published', 'Unknown')}"
            )

            st.write(
                f"**Categories:** "
                f"{', '.join(article.get('categories', []))}"
            )

            locations = article.get(
                "locations",
                []
            )

            st.write(
                f"**Locations:** "
                f"{', '.join(locations) if locations else 'None detected'}"
            )


        with col2:

            st.metric(
                "Score",
                f"{article.get('score', 0)}/100"
            )

            st.write(
                f"**Priority:** {priority}"
            )


        st.write(
            "**Keywords:** "
            + ", ".join(
                article.get(
                    "keywords",
                    []
                )
            )
        )


        link = article.get(
            "link",
            ""
        )


        if link:

            st.link_button(
                "Read Original Article",
                link
            )


        st.divider()
