from newsapi import NewsApiClient
import secrets
# Init
def get_headlines():
    newsapi = NewsApiClient(api_key=secrets.news_key)

    # /v2/top-headlines
    top_headlines = newsapi.get_everything(q='tesla')

    # Convert headlines to printable format
    printable_headlines = []
    article_count = 0
    for article in top_headlines['articles']:
        try:
            title = article['title']
            description = article['description']
            # Combine title and description and add to the list
            combined_text = f"{title}: {description}"
            printable_headlines.append(combined_text.encode('utf-8', 'ignore').decode('utf-8'))
            article_count += 1
            if article_count == 3:
                break  # Stop the loop after adding three articles
        except UnicodeEncodeError:
            print("Unable to print this headline due to encoding issue.")
    
    # Return the printable headlines
    return printable_headlines