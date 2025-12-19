# 🧬 Biotech Lead Generation & Qualification Agent

> An intelligent web crawler that identifies, enriches, and ranks high-quality leads for 3D in-vitro model technologies in drug discovery and therapy development.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🔗 Live Demo

**[Access the Application Here](#)**         *[](https://3d-in-vitro-lead-scoring-agent-twreowfpeba5q3pr6opmfk.streamlit.app/)[]*

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📋 Overview

This project is a specialized business development tool designed to help companies offering **3D in-vitro models** find and prioritize the most qualified prospects in the pharmaceutical and biotechnology industries. Instead of manually searching for potential clients, this agent automates the entire process—from identification to contact enrichment to intelligent ranking.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## The Challenge It Solves

Traditional lead generation in biotech is time-consuming and inefficient. Researchers and business development teams need to:
- Manually search LinkedIn for relevant titles
- Cross-reference scientific publications
- Find contact information
- Guess which leads are most likely to convert

This tool transforms that multi-week process into an automated, data-driven workflow that delivers **ranked, qualified leads in minutes**.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🎯 Key Features

### 1. **Multi-Source Lead Identification**
Automatically discovers prospects from:
- **LinkedIn & Sales Navigator** - Target specific roles and companies
- **PubMed & Google Scholar** - Find researchers publishing relevant papers
- **Conference Attendee Lists** - Access participants from events like Society of Toxicology (SOT)
- **Xing** - Cover European biotech professionals

### 2. **Comprehensive Data Enrichment**
For each identified prospect, the agent gathers:
- ✉️ **Business email addresses** (company domains like @pfizer.com)
- 📞 **Direct phone numbers**
- 📍 **Dual location tracking** - Personal location vs. Company HQ
- 🏢 **Company information** - Funding stage, tech stack, research focus

### 3. **Intelligent Propensity-to-Buy Scoring**
Uses a weighted algorithm (0-100 score) based on:

| Signal | Criteria | Weight | Example |
|--------|----------|--------|---------|
| **Role Fit** | Title contains: Toxicology, Safety, Hepatic, 3D | High (+30) | "Director of Toxicology" |
| **Company Intent** | Recently raised Series A/B funding | High (+20) | $50M Series B in Q3 2024 |
| **Technographic** | Already uses in-vitro models | Medium (+15) | Uses organ-on-chip tech |
| **NAM Adoption** | Open to New Approach Methodologies | Medium (+10) | Published on NAMs |
| **Location** | Based in innovation hub | Medium (+10) | Boston, Basel, SF Bay Area |
| **Scientific Intent** | Published DILI paper (last 2 years) | Very High (+40) | First author on hepatotoxicity study |

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Result Example:**
- 🔴 Junior Scientist at unfunded startup: **15/100**
- 🟢 Director of Safety at Series B biotech in Cambridge who published on liver toxicity: **95/100**

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🏗️ System Architecture

### Three-Stage Pipeline

```
┌─────────────────┐      ┌──────────────────┐      ┌─────────────────┐
│   STAGE 1:      │ ───> │    STAGE 2:      │ ───> │   STAGE 3:      │
│ IDENTIFICATION  │      │   ENRICHMENT     │      │    RANKING      │
│                 │      │                  │      │                 │
│ • LinkedIn      │      │ • Email Finder   │      │ • Score Calc    │
│ • PubMed        │      │ • Phone Lookup   │      │ • Prioritization│
│ • Conferences   │      │ • Location Data  │      │ • Export        │
└─────────────────┘      └──────────────────┘      └─────────────────┘
```

### Stage 1: Identification (The Input)
Scans target profiles based on your criteria:
- **Job Titles:** Director of Toxicology, Head of Preclinical Safety, VP of Drug Discovery
- **Data Sources:** LinkedIn Search, Sales Navigator, PubMed author databases, conference lists

### Stage 2: Enrichment (The Data Gathering)
Queries external databases to enhance each profile:
- **Contact Information:** Business emails and phone numbers
- **Location Intelligence:** Distinguishes between remote work location and company headquarters
- **Company Context:** Funding status, technology stack, research areas

### Stage 3: Ranking (The Probability Engine)
Applies the proprietary "Propensity to Buy" algorithm to score and rank all leads based on weighted criteria.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📊 Output: Lead Generation Dashboard

The tool produces a dynamic, searchable table with the following columns:

| Rank | Score | Name | Title | Company | Person Location | HQ Location | Email | LinkedIn | Action |
|------|-------|------|-------|---------|----------------|-------------|-------|----------|--------|
| 1 | 95 | Dr. Jane Smith | Dir. of Safety | BioCorp | Remote (TX) | Cambridge, MA | jane.smith@... | 🔗 | Contact |
| 2 | 87 | Dr. John Doe | VP Preclinical | PharmaX | Basel, CH | Basel, CH | john.doe@... | 🔗 | Contact |

### Dashboard Features:
- ✅ **Instant Search & Filtering** - Type "Boston" or "Oncology" to filter results
- ✅ **Location Split Display** - See if prospects are remote or office-based
- ✅ **Exportable Formats** - Download to Excel/CSV for CRM integration
- ✅ **Priority Sorting** - Auto-sorted by probability score (highest first)
- ✅ **One-Click Actions** - Direct links to LinkedIn profiles and email templates

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🛠️ Technical Implementation Paths

### Path A: No-Code Solution (Recommended for Fast Deployment)
**Tool:** Clay.io or Apollo.io
- Feed LinkedIn search URLs
- Automated email discovery
- AI reads company descriptions to score relevance
- Outputs to Google Sheets/Dashboard
- **Time to Deploy:** 1-2 days

### Path B: Custom Dashboard (Full Control)
**Stack:** Python + Streamlit + LinkedIn API
- Connect to LinkedIn API or Proxycurl
- Custom scoring algorithm
- Web-based interface
- Database integration (PostgreSQL/MongoDB)
- **Time to Deploy:** 2-4 weeks

### Path C: Your Custom Methodology
Build your own approach using the framework above as a foundation.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🌐 Target Website Categories

The web agent systematically harvests data from these five categories:

### 1. Professional Social Networks
- **Primary:** LinkedIn, Sales Navigator
- **Secondary:** Xing (for European markets)
- **Extracts:** Job titles, tenure, location, company info

### 2. Scientific Publication Databases
- **Sources:** PubMed, Google Scholar, bioRxiv
- **Keywords Tracked:** 
  - Drug-Induced Liver Injury (DILI)
  - 3D cell culture
  - Organ-on-chip
  - Hepatic spheroids
  - Investigative Toxicology
- **Focus:** Papers from last 12-24 months
- **Priority:** Corresponding authors (budget holders) and first authors (key users)

### 3. Company Intelligence Platforms
- Crunchbase (funding data)
- PitchBook (investor info)
- Company websites (tech stack, research focus)

### 4. Conference & Event Databases
- Society of Toxicology (SOT)
- American Association for Cancer Research (AACR)
- Attendee lists and speaker rosters

### 5. Contact Enrichment Services
- Hunter.io (email discovery)
- Clearbit (company data)
- ZoomInfo (contact verification)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🎯 Ideal User Persona

This tool is designed for:
- **Business Development Teams** at biotech tool/service companies
- **Sales Teams** selling 3D in-vitro models, organ-on-chip technology
- **Market Research Analysts** in pharmaceutical innovation
- **Partnership Managers** at CROs focused on predictive toxicology

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📈 Expected Outcomes

From a typical run targeting 500 prospects:
- **High Priority (80-100):** 50-75 leads → Immediate outreach
- **Medium Priority (50-79):** 150-200 leads → Nurture campaign
- **Low Priority (0-49):** 250-275 leads → Newsletter/content marketing

**Average Conversion Improvement:** 3-5x higher meeting acceptance rate compared to cold outreach.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🚀 Getting Started

1. **Define Your Criteria** - Job titles, companies, locations, keywords
2. **Configure Data Sources** - Connect to LinkedIn, PubMed, etc.
3. **Set Scoring Weights** - Adjust the algorithm to your ideal customer profile
4. **Run Initial Crawl** - Test with 50-100 prospects
5. **Refine & Scale** - Optimize based on results, scale to thousands

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📧 Contact

[https://mridulbhardwaj.vercel.app]
mridul.2005.05@gmail.com

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Built for biotech innovators who need qualified leads, not just contact lists.**








