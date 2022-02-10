import requests, json

def geturl2(**kwargs):
    if kwargs.get("mcversion"):
        url = f"https://nitroxenon-minecraft-forge-v1.p.rapidapi.com/optifine/{kwargs.get('mcversion')}"
        headers = {
            'x-rapidapi-key': "a6f51f9ea2mshf179951f6fc0d97p1b476ejsndba62ed12b1d",
            'x-rapidapi-host': "nitroxenon-minecraft-forge-v1.p.rapidapi.com"
            }
        try:
            r = requests.get(url, headers=headers,timeout=5)
            data = json.loads(r.text)
            liURL = []
            for info in data:
                url = f'https://optifine.net/download?f={info.get("filename")}'
                liURL.append(url)  
                if kwargs.get('single'):
                    break
            return(liURL)
        except requests.exceptions.Timeout:
            print("Connection Timeout! Retrying...")
            geturl2(kwargs)
    else:
        raise ValueError("Missing Argument: MCVersion!")