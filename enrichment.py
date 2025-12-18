import requests

class DataEnrichment:
    def __init__(self, hunter_api_key=None):
        self.hunter_key = hunter_api_key
        self.use_mock = True  # Set to False when you have Hunter.io API key
    
    def find_email(self, first_name, last_name, company_domain):
        """Find business email for a person"""
        
        if self.use_mock:
            # Mock email generation for demo
            if first_name and last_name and company_domain:
                return f"{first_name[0].lower()}.{last_name.lower()}@{company_domain}"
            return None
        
        # Real Hunter.io API implementation
        try:
            url = "https://api.hunter.io/v2/email-finder"
            params = {
                'domain': company_domain,
                'first_name': first_name,
                'last_name': last_name,
                'api_key': self.hunter_key
            }
            
            response = requests.get(url, params=params)
            data = response.json()
            
            return data.get('data', {}).get('email')
        except Exception as e:
            print(f"Error finding email: {e}")
            return None
    
    def get_company_info(self, company_name):
        """Get company location, funding info, etc."""
        
        # For now, return None - this data is already in our LinkedIn/Apollo results
        # In a real system, you'd use Crunchbase or Clearbit API
        return {
            'hq_location': None,
            'funding_stage': None,
            'raised_amount': None
        }


class LocationParser:
    def __init__(self):
        self.hub_cities = [
            'Boston', 'Cambridge', 'San Francisco', 'Bay Area',
            'Basel', 'Oxford', 'Cambridge UK', 'South San Francisco',
            'San Diego', 'Seattle', 'Research Triangle', 'London',
            'Tarrytown', 'New York'
        ]
    
    def is_hub_location(self, location):
        """Check if location is in a major biotech hub"""
        if not location:
            return False
        
        location_lower = location.lower()
        for hub in self.hub_cities:
            if hub.lower() in location_lower:
                return True
        return False
    
    def parse_location(self, person_location, company_hq):
        """Distinguish between person's location and company HQ"""
        
        is_hub = self.is_hub_location(person_location) or self.is_hub_location(company_hq)
        
        # Check if person is remote (different location than company HQ)
        is_remote = False
        if person_location and company_hq:
            is_remote = person_location.lower() != company_hq.lower()
        
        return {
            'person_location': person_location,
            'company_hq': company_hq,
            'is_hub': is_hub,
            'is_remote': is_remote
        }