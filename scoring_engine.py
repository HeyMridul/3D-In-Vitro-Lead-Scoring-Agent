class PropensityScorer:
    def __init__(self):
        self.weights = {
            'role_fit': 30,
            'company_funding': 20,
            'tech_usage': 15,
            'nam_interest': 10,
            'hub_location': 10,
            'recent_publication': 40
        }
        
        self.hub_cities = [
            'boston', 'cambridge', 'san francisco', 'south san francisco',
            'bay area', 'basel', 'oxford', 'cambridge uk', 'san diego',
            'seattle', 'research triangle', 'london'
        ]
    
    def calculate_score(self, lead):
        """Calculate propensity to buy score (0-100)"""
        score = 0
        scoring_details = []
        
        # 1. Role Fit (30 points)
        role_score = self.score_role_fit(lead.get('title', ''))
        score += role_score
        if role_score > 0:
            scoring_details.append(f"Role fit: +{role_score}")
        
        # 2. Company Funding (20 points)
        funding_score = self.score_funding(lead.get('company_funding', ''))
        score += funding_score
        if funding_score > 0:
            scoring_details.append(f"Funding stage: +{funding_score}")
        
        # 3. Tech Usage (15 points)
        tech_score = self.score_tech_usage(lead.get('company', ''))
        score += tech_score
        if tech_score > 0:
            scoring_details.append(f"Tech usage: +{tech_score}")
        
        # 4. NAM Interest (10 points)
        nam_score = self.score_nam_interest(lead.get('title', ''))
        score += nam_score
        if nam_score > 0:
            scoring_details.append(f"NAM interest: +{nam_score}")
        
        # 5. Hub Location (10 points)
        location_score = self.score_location(lead.get('location', ''), lead.get('company_hq', ''))
        score += location_score
        if location_score > 0:
            scoring_details.append(f"Hub location: +{location_score}")
        
        # 6. Recent Publication (40 points)
        pub_score = self.score_publication(lead.get('publications', []))
        score += pub_score
        if pub_score > 0:
            scoring_details.append(f"Recent publication: +{pub_score}")
        
        return min(score, 100), scoring_details
    
    def score_role_fit(self, title):
        """Score based on job title keywords (0-30 points)"""
        if not title:
            return 0
        
        title_lower = title.lower()
        
        # High-value keywords
        director_keywords = ['director', 'head', 'vp', 'vice president', 'chief']
        technical_keywords = ['toxicology', 'safety', 'hepatic', '3d', 'preclinical', 'dili']
        
        director_match = any(kw in title_lower for kw in director_keywords)
        technical_match = sum(1 for kw in technical_keywords if kw in title_lower)
        
        if director_match and technical_match >= 2:
            return 30  
        elif director_match and technical_match >= 1:
            return 25  
        elif technical_match >= 2:
            return 20  
        elif director_match or technical_match >= 1:
            return 10  
        
        return 0
    
    def score_funding(self, funding_stage):
        """Score based on company funding (0-20 points)"""
        if not funding_stage:
            return 0
        
        funding_lower = funding_stage.lower()
        
        if 'series a' in funding_lower or 'series b' in funding_lower:
            return 20  
        elif 'series c' in funding_lower or 'series d' in funding_lower:
            return 15  
        elif 'seed' in funding_lower:
            return 10  
        elif 'public' in funding_lower or 'acquired' in funding_lower:
            return 12  
        
        return 0
    
    def score_tech_usage(self, company):
        """Score if company likely uses similar tech (0-15 points)"""
        if not company:
            return 0
        
        company_lower = company.lower()
        
        # Companies known for innovative approaches
        innovative_keywords = ['bio', 'therapeutics', 'pharma', 'biotech', 'research', 'sciences']
        
        matches = sum(1 for kw in innovative_keywords if kw in company_lower)
        
        if matches >= 2:
            return 15
        elif matches >= 1:
            return 10
        
        return 0
    
    def score_nam_interest(self, title):
        """Score if interested in New Approach Methodologies (0-10 points)"""
        if not title:
            return 0
        
        title_lower = title.lower()
        nam_keywords = ['alternative', 'nam', '3d', 'in vitro', 'model']
        
        if any(kw in title_lower for kw in nam_keywords):
            return 10
        
        return 0
    
    def score_location(self, person_location, company_hq):
        """Score based on biotech hub location (0-10 points)"""
        locations_to_check = [person_location, company_hq]
        
        for location in locations_to_check:
            if location:
                location_lower = location.lower()
                for hub in self.hub_cities:
                    if hub in location_lower:
                        return 10
        
        return 0
    
    def score_publication(self, publications):
        """Score based on recent relevant publications (0-40 points)"""
        if not publications or len(publications) == 0:
            return 0
        
        # Keywords that indicate relevant research
        relevant_keywords = [
            'dili', 'liver injury', 'hepatotoxicity', '3d', 'spheroid',
            'organoid', 'in vitro', 'cell culture', 'hepatic', 'toxicity'
        ]
        
        current_year = 2024
        max_score = 0
        
        for pub in publications:
            pub_year = pub.get('year', 0)
            title = pub.get('title', '').lower()
            
            
            relevance = sum(1 for kw in relevant_keywords if kw in title)
            
            
            if pub_year >= current_year - 1:  
                if relevance >= 2:
                    max_score = max(max_score, 40)  
                elif relevance >= 1:
                    max_score = max(max_score, 30)
            elif pub_year >= current_year - 2:  
                if relevance >= 2:
                    max_score = max(max_score, 35)
                elif relevance >= 1:
                    max_score = max(max_score, 25)
        
        return max_score