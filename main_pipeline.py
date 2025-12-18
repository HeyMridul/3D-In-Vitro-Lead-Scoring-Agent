from linkedin_scraper import LinkedInScraper
from pubmed_scraper import PubMedScraper
from enrichment import DataEnrichment, LocationParser
from scoring_engine import PropensityScorer
import pandas as pd
from datetime import datetime

class LeadGenerator:
    def __init__(self, config=None):
        self.linkedin = LinkedInScraper(api_key=config.get('apollo_api') if config else None)
        self.pubmed = PubMedScraper()
        self.enrichment = DataEnrichment(hunter_api_key=config.get('hunter_api') if config else None)
        self.location_parser = LocationParser()
        self.scorer = PropensityScorer()
        self.leads = []
    
    def run_full_pipeline(self, job_titles, pubmed_keywords):
        """Run the complete lead generation pipeline"""
        
        print("\n" + "="*60)
        print("🚀 STARTING LEAD GENERATION PIPELINE")
        print("="*60)
        
        # Stage 1: Identification
        print("\n📍 STAGE 1: IDENTIFICATION")
        linkedin_leads = self.linkedin.search_people(job_titles)
        print(f"   ✅ Found {len(linkedin_leads)} LinkedIn profiles")
        
        pubmed_papers = self.pubmed.search_authors(pubmed_keywords)
        print(f"   ✅ Found {len(pubmed_papers)} PubMed papers")
        
        # Stage 2: Enrichment
        print("\n💎 STAGE 2: ENRICHMENT")
        enriched_leads = self.run_enrichment(linkedin_leads, pubmed_papers)
        print(f"   ✅ Enriched {len(enriched_leads)} leads")
        
        # Stage 3: Scoring
        print("\n🎯 STAGE 3: SCORING & RANKING")
        scored_leads = self.score_leads(enriched_leads)
        print(f"   ✅ Scored and ranked {len(scored_leads)} leads")
        
        
        self.save_results(scored_leads)
        
        return scored_leads
    
    def run_enrichment(self, linkedin_leads, pubmed_papers):
        """Stage 2: Enrich leads with emails, locations, and publications"""
        enriched = []
        
        for lead in linkedin_leads:
            
            location_data = self.location_parser.parse_location(
                lead.get('location', ''),
                lead.get('company_hq', '')
            )
            
            
            if not lead.get('email'):
                email = self.enrichment.find_email(
                    lead.get('first_name', ''),
                    lead.get('last_name', ''),
                    lead.get('company_domain', '')
                )
                lead['email'] = email
            
            
            lead['publications'] = []
            lead_name = lead.get('name', '').lower()
            
            for paper in pubmed_papers:
                authors = paper.get('authors', [])
                for author in authors:
                    author_name = author.get('name', '').lower()
                    
                    if lead_name in author_name or author_name in lead_name:
                        lead['publications'].append({
                            'title': paper.get('title'),
                            'year': int(paper.get('pub_date', '2024')[:4]) if paper.get('pub_date') else 2024,
                            'journal': paper.get('journal'),
                            'url': paper.get('pubmed_url')
                        })
                        break  
            
            
            lead.update(location_data)
            
            enriched.append(lead)
            
            
            print(f"   Enriched: {lead['name']} - Email: {lead.get('email', 'N/A')}, "
                  f"Hub: {location_data['is_hub']}, Pubs: {len(lead['publications'])}")
        
        return enriched
    
    def score_leads(self, leads):
        """Stage 3: Score and rank all leads"""
        scored = []
        
        for lead in leads:
            score, details = self.scorer.calculate_score(lead)
            lead['score'] = score
            lead['scoring_details'] = details
            scored.append(lead)
        
        
        scored.sort(key=lambda x: x['score'], reverse=True)
        
        
        for i, lead in enumerate(scored):
            lead['rank'] = i + 1
        
        return scored
    
    def save_results(self, leads):
        """Save results to CSV"""
        df = pd.DataFrame(leads)
        
        
        columns = [
            'rank', 'score', 'name', 'title', 'company', 'email',
            'person_location', 'company_hq', 'is_hub', 'is_remote',
            'company_funding', 'linkedin_url', 'phone'
        ]
        
        available_columns = [col for col in columns if col in df.columns]
        df_output = df[available_columns]
        
        
        filename = f"leads_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df_output.to_csv(filename, index=False)
        
        print(f"\n💾 Results saved to: {filename}")
        self.print_summary(leads)
    
    def print_summary(self, leads):
        """Print summary statistics"""
        print("\n" + "="*60)
        print("📊 SUMMARY")
        print("="*60)
        
        high_priority = len([l for l in leads if l['score'] >= 80])
        medium_priority = len([l for l in leads if 60 <= l['score'] < 80])
        low_priority = len([l for l in leads if l['score'] < 60])
        
        print(f"Total Leads: {len(leads)}")
        print(f"High Priority (80+): {high_priority}")
        print(f"Medium Priority (60-79): {medium_priority}")
        print(f"Low Priority (<60): {low_priority}")
        
        print("\n🏆 TOP 5 LEADS:")
        for lead in leads[:5]:
            print(f"\n{lead['rank']}. {lead['name']} - Score: {lead['score']}")
            print(f"   {lead['title']} at {lead['company']}")
            print(f"   📧 {lead.get('email', 'N/A')}")
            print(f"   📍 {lead.get('person_location', 'N/A')}")
            if lead.get('scoring_details'):
                print(f"   ⭐ {', '.join(lead['scoring_details'])}")



if __name__ == "__main__":
    config = {
        'apollo_api': None,  # Your Apollo API key (optional)
        'hunter_api': None   # Your Hunter.io API key (optional)
    }
    
    generator = LeadGenerator(config)
    
    
    job_titles = [
        "Director of Toxicology",
        "Head of Safety Assessment",
        "VP Toxicology",
        "Director of Preclinical Safety"
    ]
    
    pubmed_keywords = [
        "DILI",
        "drug-induced liver injury",
        "hepatotoxicity",
        "3D cell culture",
        "hepatic spheroids"
    ]
    
    
    results = generator.run_full_pipeline(job_titles, pubmed_keywords)