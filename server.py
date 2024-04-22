from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from GoogleNews import GoogleNews
import json
from googlenews import search_google_news

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the query from the URL
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        query = query_params.get('q', [''])[0]

        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Call the Google News search function
        search_results = search_google_news(query)
        
        # Send the search results as the response
        self.wfile.write(search_results.encode())

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
