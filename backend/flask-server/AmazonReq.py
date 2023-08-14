import requests
from bs4 import BeautifulSoup
import re

limit =20
def get_amazon_reviews(url,val):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    # Search for ASIN in URL 
    try:
        asin_match = re.search(r'/dp/([A-Z0-9]{10})', url)
        if asin_match:
            asin = asin_match.group(1)
            print("ASIN:", asin)
    except Exception as e:
        return(None)
    # Construct reviews URL
    reviews_url = f"https://www.amazon.com/product-reviews/{asin}/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"

    print(reviews_url)
    all_reviews = []
    page = 1 
    has_more = True
    max_words_limit = 350
    total_words = 0
    all_reviews = []
    flag = False
    if(val=='1'):
        print()
        print("Trying 100")
        print()
        number=100
    else:
        print()
        print("Trying 35")
        print()
        number=35
    while has_more and len(all_reviews) <= number and flag==False:
        if page == 1:
            response = requests.get(reviews_url, headers=headers)
            if response.status_code != 200:
                print(f"Failed to fetch the page. Status code: {response.status_code}")
        else:
            response = requests.get(f"{reviews_url}?pageNumber={page}", headers=headers)
            if response.status_code != 200:
                print(f"Failed to fetch the page. Status code: {response.status_code}")

        soup = BeautifulSoup(response.text, "html.parser")
        reviews = soup.find_all('div', {'data-hook': 'review'})
        page += 1
        
        if (reviews==None):
            has_more = False
        else:
            for review in reviews:
                review_text_element = review.find('a', {'data-hook': 'review-title'})
                review_text = review_text_element.text.strip()
                star_rating_element = review.find('span', {'class': 'a-icon-alt'})
                star_rating = star_rating_element.text.strip()
                
                # Remove the star rating from the review text
                text = review_text.replace(star_rating, "").strip()
                words_in_review = len(text.split())
                
                if total_words + words_in_review <= max_words_limit:
                    all_reviews.append(text)
                    total_words += words_in_review
                else:
                    remaining_words = max_words_limit - total_words
                    truncated_text = ' '.join(text.split()[:remaining_words])
                    all_reviews.append(truncated_text)
                    flag=True
                    break

                if len(all_reviews) >= number:
                    break
                
    while (len(all_reviews)==0 and limit>0):
        limit=-1
        all_reviews=get_amazon_reviews(url)

    return all_reviews

def count_amazon_reviews(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    # Search for ASIN in URL 
    try:
        asin_match = re.search(r'/dp/([A-Z0-9]{10})', url)
        if asin_match:
            asin = asin_match.group(1)
            print("ASIN:", asin)
    except Exception as e:
        return(None)
    # Construct reviews URL
    reviews_url = f"https://www.amazon.com/product-reviews/{asin}/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"

    page = 1 
    has_more = True
    flag = False
    while has_more and flag==False:
        if page == 1:
            response = requests.get(reviews_url, headers=headers)
            if response.status_code != 200:
                print(f"Failed to fetch the page. Status code: {response.status_code}")
        else:
            response = requests.get(f"{reviews_url}?pageNumber={page}", headers=headers)
            if response.status_code != 200:
                print(f"Failed to fetch the page. Status code: {response.status_code}")

        soup = BeautifulSoup(response.text, "html.parser")
        reviews = soup.find('div', {'data-hook': 'cr-filter-info-review-rating-count'})
        if(reviews!=None):  
           # Use regular expression to find all numbers in the text
            numbers = re.findall(r'\d{1,3}(?:,\d{3})*', reviews.text)
            # Remove commas from the number strings and convert to integers
            cleaned_numbers = [int(num.replace(',', '')) for num in numbers]
            
            # Extract the second number if available
            second_number = cleaned_numbers[1] if len(cleaned_numbers) > 1 else None
            print("Reviews number -       ")
            print(second_number)
            print()
            return second_number
            # # Extract the second number if available
            # second_number = int(numbers[1]) if len(numbers) > 1 else None
            # print("Reviews number -       ")
            # print(second_number)
            # print()
            # return second_number