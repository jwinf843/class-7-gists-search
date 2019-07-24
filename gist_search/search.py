# from gist_search.utils import get_gists
from utils import get_gists

def search_gists(username, description=None, file_name=None, ID=None, url=None):
    if not description and not file_name:
        print("At least one search parameter must be specified")
        return
    
    gists = get_gists(username)
    results = []
  
    for gist in gists:
        if description and description.lower() not in gist['description'].lower():
            continue
        
        if ID and ID.lower() not in gist['id'].lower():
            continue
            
        if url and url.lower() not in gist['url'].lower():
            continue
            
        if file_name:
            found = False
            for fname in gist['files']:
                if file_name.lower() in fname.lower():
                    found = True
                    break
            if not found:
                continue      
        
        results.append(gist)
        
    return results


results = search_gists('santiagobasulto', description='Humble')

print(results)