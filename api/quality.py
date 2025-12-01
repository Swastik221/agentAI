from urllib.parse import urlparse

class CitationEvaluator:
    def __init__(self):
        self.trusted_domains = ['.gov', '.edu', '.org']

    def evaluate_url(self, url: str) -> float:
        """
        Evaluates the credibility of a URL based on its domain.
        
        Args:
            url (str): The URL to evaluate.
            
        Returns:
            float: A score between 0.0 and 1.0.
        """
        try:
            domain = urlparse(url).netloc
            if any(domain.endswith(t) for t in self.trusted_domains):
                return 1.0
            return 0.7 # Default score for commercial/other sites
        except:
            return 0.0

    def validate_json_structure(self, data: dict, required_keys: list) -> bool:
        """
        Validates if the dictionary contains all required keys.
        """
        return all(key in data for key in required_keys)

if __name__ == "__main__":
    evaluator = CitationEvaluator()
    print(evaluator.evaluate_url("https://www.cdc.gov")) # Should be 1.0
    print(evaluator.evaluate_url("https://example.com")) # Should be 0.7
