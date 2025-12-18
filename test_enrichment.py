from enrichment import DataEnrichment, LocationParser

# Test Email Finder
print("Testing Email Finder...")
enrichment = DataEnrichment()

email = enrichment.find_email("Sarah", "Chen", "biogen.com")
print(f"✅ Generated email: {email}")

# Test Location Parser
print("\nTesting Location Parser...")
location_parser = LocationParser()

# Test 1: Person in hub location
result1 = location_parser.parse_location("Cambridge, MA", "Cambridge, MA")
print(f"\n1. Same location (Cambridge):")
print(f"   Is hub: {result1['is_hub']}")
print(f"   Is remote: {result1['is_remote']}")

# Test 2: Remote person
result2 = location_parser.parse_location("Denver, CO", "Boston, MA")
print(f"\n2. Remote worker (Denver → Boston):")
print(f"   Is hub: {result2['is_hub']}")
print(f"   Is remote: {result2['is_remote']}")

# Test 3: Non-hub location
result3 = location_parser.parse_location("Austin, TX", "Austin, TX")
print(f"\n3. Non-hub location (Austin):")
print(f"   Is hub: {result3['is_hub']}")
print(f"   Is remote: {result3['is_remote']}")