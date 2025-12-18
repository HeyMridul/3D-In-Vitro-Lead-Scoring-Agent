import requests
from datetime import datetime, timedelta

class PubMedScraper:
    def __init__(self):
        self.base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
    
    def search_authors(self, keywords, months_back=24):
        """Find authors who published papers on specific topics"""
        print(f"🔬 Searching PubMed for: {', '.join(keywords)}")
        
        # Calculate date range
        end_date = datetime.now()
        start_date = end_date - timedelta(days=months_back*30)
        
        # Build search query
        query = f"({' OR '.join(keywords)}) AND {start_date.year}:{end_date.year}[pdat]"
        
        try:
            # Search PubMed
            search_url = f"{self.base_url}/esearch.fcgi"
            params = {
                'db': 'pubmed',
                'term': query,
                'retmax': 50,
                'retmode': 'json'
            }
            
            response = requests.get(search_url, params=params)
            data = response.json()
            paper_ids = data.get('esearchresult', {}).get('idlist', [])
            
            print(f"✅ Found {len(paper_ids)} relevant papers")
            
            # Get details for each paper
            authors = []
            for paper_id in paper_ids[:10]:  # Limit to first 10 for speed
                paper_data = self.get_paper_details(paper_id)
                if paper_data:
                    authors.append(paper_data)
            
            return authors
            
        except Exception as e:
            print(f"❌ Error searching PubMed: {e}")
            return []
    
    def get_paper_details(self, paper_id):
        """Get author and paper details"""
        try:
            fetch_url = f"{self.base_url}/esummary.fcgi"
            params = {
                'db': 'pubmed',
                'id': paper_id,
                'retmode': 'json'
            }
            
            response = requests.get(fetch_url, params=params)
            data = response.json()
            
            result = data.get('result', {}).get(paper_id, {})
            
            return {
                'paper_id': paper_id,
                'title': result.get('title', ''),
                'authors': result.get('authors', []),
                'pub_date': result.get('pubdate', ''),
                'journal': result.get('source', ''),
                'pubmed_url': f"https://pubmed.ncbi.nlm.nih.gov/{paper_id}/"
            }
            
        except Exception as e:
            print(f"Error fetching paper {paper_id}: {e}")
            return None