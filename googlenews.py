from GoogleNews import GoogleNews
import json

def search_google_news(query):
    googlenews = GoogleNews()
    googlenews.setlang('pt')
    googlenews.search(query)
    result = googlenews.result()
    
    # Transforma a lista de dicionários em um objeto JSON
    json_results = json.dumps(result, ensure_ascii=False)
    
    return json_results
