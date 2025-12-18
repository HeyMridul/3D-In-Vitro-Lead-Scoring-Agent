import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Lead Scoring Agent",
    layout="wide"
)

# ---------------- HEADER ----------------
st.title("🧠 Lead Scoring Agent – 3D In-Vitro Models")
st.markdown("""
This agent identifies and ranks **scientific decision-makers** based on their  
**propensity to adopt 3D in-vitro models for therapy design**.
""")

st.divider()

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    return pd.read_csv("leads.csv")

df = load_data()

# Ensure correct dtypes
df["score"] = pd.to_numeric(df["score"], errors="coerce")
df["is_hub"] = df["is_hub"].astype(bool)
df["is_remote"] = df["is_remote"].astype(bool)

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("🔍 Filters")

search_query = st.sidebar.text_input(
    "Search (Name, Title, Company)"
)

min_score = st.sidebar.slider(
    "Minimum Propensity Score",
    min_value=0,
    max_value=100,
    value=50
)

funding_filter = st.sidebar.multiselect(
    "Company Funding Stage",
    options=sorted(df["company_funding"].dropna().unique())
)

hub_filter = st.sidebar.checkbox("Only Hub Locations")
remote_filter = st.sidebar.checkbox("Only Remote Roles")

location_filter = st.sidebar.multiselect(
    "Person Location",
    options=sorted(df["person_location"].dropna().unique())
)

# ---------------- FILTER LOGIC ----------------
filtered_df = df.copy()

if search_query:
    filtered_df = filtered_df[
        filtered_df.apply(
            lambda row: search_query.lower() in (
                f"{row['name']} {row['title']} {row['company']}".lower()
            ),
            axis=1
        )
    ]

filtered_df = filtered_df[filtered_df["score"] >= min_score]

if funding_filter:
    filtered_df = filtered_df[
        filtered_df["company_funding"].isin(funding_filter)
    ]

if hub_filter:
    filtered_df = filtered_df[filtered_df["is_hub"] == True]

if remote_filter:
    filtered_df = filtered_df[filtered_df["is_remote"] == True]

if location_filter:
    filtered_df = filtered_df[
        filtered_df["person_location"].isin(location_filter)
    ]

filtered_df = filtered_df.sort_values("score", ascending=False)

# ---------------- METRICS ----------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Leads", len(df))
col2.metric("High-Intent Leads", len(filtered_df))
col3.metric(
    "Avg Score",
    round(filtered_df["score"].mean(), 1) if len(filtered_df) > 0 else 0
)

st.divider()

# ---------------- DISPLAY TABLE ----------------
st.subheader("📊 Ranked Lead List")

display_columns = [
    "rank",
    "score",
    "name",
    "title",
    "company",
    "person_location",
    "company_hq",
    "company_funding",
    "email",
    "linkedin_url"
]

st.dataframe(
    filtered_df[display_columns],
    use_container_width=True,
    hide_index=True
)

# ---------------- DOWNLOAD ----------------
st.download_button(
    "⬇️ Download Filtered Leads (CSV)",
    data=filtered_df.to_csv(index=False),
    file_name="ranked_leads.csv",
    mime="text/csv"
)

# ---------------- FOOTER ----------------
st.markdown("""
---
### 🧪 Scoring Signals Used
• Role relevance (Toxicology / Safety / 3D models)  
• Company funding stage  
• Scientific publication intent  
• Geographic hub presence  
• Remote vs HQ alignment  

_MVP built for rapid BD prioritization._
""")
