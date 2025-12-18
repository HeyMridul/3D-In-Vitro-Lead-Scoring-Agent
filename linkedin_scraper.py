# PROXYCURL was not working 
# RapidAPI's subscription Button was disabled 
# Apollo.io's free plan doesn't give API access to /people/search. This is a common limitation.
# For a quick Solution I used mock data

import requests
import time

class LinkedInScraper:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.use_mock = True  # Toggle this when you get real API access
    
    def search_people(self, job_titles):
        """Search for people - uses mock data for demo"""
        
        if self.use_mock:
            return self._get_mock_data(job_titles)
        else:
            return self._search_real_api(job_titles)
    
    def _get_mock_data(self, job_titles):
        """Generate realistic mock data based on job titles"""
        print("📊 Using sample data for demonstration...")
        
        # Realistic sample leads
        mock_database = [
            {
                'name': 'Dr. Sarah Chen',
                'first_name': 'Sarah',
                'last_name': 'Chen',
                'title': 'Director of Toxicology',
                'email': 's.chen@biogen.com',
                'phone': '+1-617-555-0123',
                'company': 'BioGen Therapeutics',
                'company_domain': 'biogen.com',
                'location': 'Cambridge',
                'state': 'MA',
                'country': 'United States',
                'linkedin_url': 'https://linkedin.com/in/sarah-chen',
                'company_funding': 'Series B',
                'company_hq': 'Cambridge, MA'
            },
            {
                'name': 'Dr. Michael Torres',
                'first_name': 'Michael',
                'last_name': 'Torres',
                'title': 'Head of Safety Assessment',
                'email': 'm.torres@apexpharma.com',
                'phone': '+1-720-555-0156',
                'company': 'Apex Pharma',
                'company_domain': 'apexpharma.com',
                'location': 'Denver',
                'state': 'CO',
                'country': 'United States',
                'linkedin_url': 'https://linkedin.com/in/michael-torres',
                'company_funding': 'Series A',
                'company_hq': 'Boston, MA'
            },
            {
                'name': 'Jennifer Walsh',
                'first_name': 'Jennifer',
                'last_name': 'Walsh',
                'title': 'VP Toxicology',
                'email': 'j.walsh@medtech.com',
                'phone': '+1-415-555-0198',
                'company': 'MedTech Solutions',
                'company_domain': 'medtech.com',
                'location': 'San Francisco',
                'state': 'CA',
                'country': 'United States',
                'linkedin_url': 'https://linkedin.com/in/jennifer-walsh',
                'company_funding': 'Series C',
                'company_hq': 'San Francisco, CA'
            },
            {
                'name': 'Dr. Raj Patel',
                'first_name': 'Raj',
                'last_name': 'Patel',
                'title': 'Director of Preclinical Safety',
                'email': 'r.patel@novacure.ch',
                'phone': '+41-61-555-0234',
                'company': 'NovaCure Bio',
                'company_domain': 'novacure.ch',
                'location': 'Basel',
                'state': 'Basel-Stadt',
                'country': 'Switzerland',
                'linkedin_url': 'https://linkedin.com/in/raj-patel',
                'company_funding': 'Series B',
                'company_hq': 'Basel, Switzerland'
            },
            {
                'name': 'Dr. Emily Rodriguez',
                'first_name': 'Emily',
                'last_name': 'Rodriguez',
                'title': 'Senior Scientist - Hepatic Safety',
                'email': 'e.rodriguez@startuplabs.com',
                'phone': '+1-512-555-0167',
                'company': 'StartUp Labs',
                'company_domain': 'startuplabs.com',
                'location': 'Austin',
                'state': 'TX',
                'country': 'United States',
                'linkedin_url': 'https://linkedin.com/in/emily-rodriguez',
                'company_funding': 'Seed',
                'company_hq': 'Austin, TX'
            },
            {
                'name': 'Dr. Thomas Anderson',
                'first_name': 'Thomas',
                'last_name': 'Anderson',
                'title': 'Head of Toxicology',
                'email': 't.anderson@astrazeneca.com',
                'phone': '+44-20-555-0145',
                'company': 'AstraZeneca',
                'company_domain': 'astrazeneca.com',
                'location': 'Cambridge',
                'state': 'Cambridgeshire',
                'country': 'United Kingdom',
                'linkedin_url': 'https://linkedin.com/in/thomas-anderson',
                'company_funding': 'Public',
                'company_hq': 'Cambridge, UK'
            },
            {
                'name': 'Dr. Lisa Wang',
                'first_name': 'Lisa',
                'last_name': 'Wang',
                'title': 'Director of Safety Assessment',
                'email': 'l.wang@genentech.com',
                'phone': '+1-650-555-0189',
                'company': 'Genentech',
                'company_domain': 'genentech.com',
                'location': 'South San Francisco',
                'state': 'CA',
                'country': 'United States',
                'linkedin_url': 'https://linkedin.com/in/lisa-wang',
                'company_funding': 'Acquired',
                'company_hq': 'South San Francisco, CA'
            },
            {
                'name': 'David Kim',
                'first_name': 'David',
                'last_name': 'Kim',
                'title': 'Associate Director - Toxicology',
                'email': 'd.kim@regeneron.com',
                'phone': '+1-914-555-0123',
                'company': 'Regeneron Pharmaceuticals',
                'company_domain': 'regeneron.com',
                'location': 'Tarrytown',
                'state': 'NY',
                'country': 'United States',
                'linkedin_url': 'https://linkedin.com/in/david-kim',
                'company_funding': 'Public',
                'company_hq': 'Tarrytown, NY'
            }
        ]
        
        # Filter based on job titles
        results = []
        for person in mock_database:
            for title in job_titles:
                if title.lower() in person['title'].lower():
                    results.append(person)
                    break
        
        print(f"✅ Found {len(results)} sample profiles")
        return results
    
    def _search_real_api(self, job_titles):
        """Real API implementation (for when you upgrade)"""
        # PROXYCURL was not working 
        # RapidAPI's subscription Button was disabled 
        # Apollo.io's free plan doesn't give API access to /people/search. This is a common limitation.
        # For a quick Solution I used mock data  
        pass