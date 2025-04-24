import requests
inspirationQuote_url = "https://api.quotable.io/random?tags=inspirational"   # URL for the quote API
print ("📘 Here’s a Quote:")

try:
    Quote = requests.get(inspirationQuote_url)
    Quote.raise_for_status()
    Quote = Quote.json()  
    print(Quote.json()['content'])
    print(Quote.json()['author'])
except requests.exceptions.RequestException as e:
  print(f"Error fetching Quote: {e}")
