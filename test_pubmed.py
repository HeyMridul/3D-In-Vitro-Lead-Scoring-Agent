from pubmed_scraper import PubMedScraper

pubmed = PubMedScraper()
keywords = ["DILI", "drug-induced liver injury", "hepatotoxicity"]
papers = pubmed.search_authors(keywords)

print(f"\n📄 Found {len(papers)} papers")
for i, paper in enumerate(papers[:3]):
    print(f"\n{i+1}. {paper['title'][:80]}...")
    print(f"   Authors: {len(paper['authors'])}")
    print(f"   Date: {paper['pub_date']}")