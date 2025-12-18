from linkedin_scraper import LinkedInScraper

linkedin = LinkedInScraper()

job_titles = ["Director of Toxicology", "Head of Safety Assessment"]
results = linkedin.search_people(job_titles)

print(f"\n🎯 Total Leads Found: {len(results)}")
print("="*60)

for i, person in enumerate(results[:5]):
    print(f"\n{i+1}. {person['name']}")
    print(f"   Title: {person['title']}")
    print(f"   Company: {person['company']}")
    print(f"   Email: {person['email']}")
    print(f"   Location: {person['location']}, {person['state']}")