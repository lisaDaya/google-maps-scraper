thonimport json
from extractors.google_maps_parser import GoogleMapsParser
from outputs.exporters import Exporter

def run_scraper():
    # Sample configuration, can be extended for dynamic parameters
    config = {
        "location": "New York",
        "max_results": 5000
    }
    
    # Initialize parser
    parser = GoogleMapsParser(config)
    data = parser.scrape_data()
    
    # Export results to JSON format
    exporter = Exporter()
    exporter.export_to_json(data, "output.json")

if __name__ == "__main__":
    run_scraper()