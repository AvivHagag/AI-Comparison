import requests
# Import os to set API key
import os
# Import OpenAI as main LLM service
from langchain.llms import OpenAI
from Apikey import Apikey
from AmazonReq import get_amazon_reviews, count_amazon_reviews
from langchain import PromptTemplate, LLMChain
import re
import json
import threading

def process_url(url, val, result_array):
    try:
        if count_amazon_reviews(url) >= 50:
            reviews = get_amazon_reviews(url, val)
            result_array.append(reviews)
        else:
            return("Error1")
    except Exception as e:
        print(f"Error getting reviews: {e}")
        return (f"Error for {url}")
    
def function(name, val):
    # Convert the JSON data string to a Python dictionary
    data = json.loads(name)

    # Extract the links from the dictionary under the key "links"
    urls = data['links']
    
    threads = []
    results = []

    for url in urls:
        thread = threading.Thread(target=process_url, args=(url, val, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    array = results
    processed_reviews = []
    for product_index, reviews_list in enumerate(array, 1):
        processed_reviews_for_product = []
        
        for review in reviews_list:
            processed_review = review.replace(".", "").strip()
            processed_reviews_for_product.append(processed_review)
        
        product_text = f"Product {product_index}: " + ", ".join(processed_reviews_for_product)
        processed_reviews.append(product_text)

    return processed_reviews
# def function(name,val):
#     # Convert the JSON data string to a Python dictionary
#     data = json.loads(name)

#     # Extract the links from the dictionary under the key "links"
#     urls = data['links']
#     array = []
#     # urls = [
#     #     "https://www.amazon.com/-/he/FIRSTBLOOD-%D7%92%D7%99%D7%99%D7%9E%D7%99%D7%A0%D7%92-AJ52-Watcher-%D7%90%D7%A8%D7%92%D7%95%D7%A0%D7%95%D7%9E%D7%99%D7%AA/dp/B01M2U8JU9/ref=d_pd_day0_sccl_4_2/134-7459010-8430367?pd_rd_w=RKmBf&content-id=amzn1.sym.8ca997d7-1ea0-4c8f-9e14-a6d756b83e30&pf_rd_p=8ca997d7-1ea0-4c8f-9e14-a6d756b83e30&pf_rd_r=6G328HH1Z0FENG8DHDKZ&pd_rd_wg=sS8YU&pd_rd_r=f90daf46-f158-4f81-885f-d59f83e79046&pd_rd_i=B01M2U8JU9&th=1",
#     #     "https://www.amazon.com/Logitech-%D7%92%D7%99%D7%99%D7%9E%D7%99%D7%A0%D7%92-%D7%91%D7%99%D7%A6%D7%95%D7%A2%D7%99%D7%9D-%D7%9E%D7%A9%D7%A7%D7%95%D7%9C%D7%95%D7%AA-%D7%9E%D7%AA%D7%9B%D7%95%D7%95%D7%A0%D7%A0%D7%95%D7%AA/dp/B07GS6ZS8J/ref=sxin_25_pa_sp_search_thematic-asin_sspa?content-id=amzn1.sym.177726c2-fdbe-4911-809a-75f891c4e015%3Aamzn1.sym.177726c2-fdbe-4911-809a-75f891c4e015&crid=2RCQGNZQF7824&cv_ct_cx=mouse&keywords=mouse&pd_rd_i=B07GS6ZS8J&pd_rd_r=e8a5ec2b-4ca4-4828-a86e-79af9201b794&pd_rd_w=z2yDc&pd_rd_wg=Ec3zl&pf_rd_p=177726c2-fdbe-4911-809a-75f891c4e015&pf_rd_r=95RG4WXV85GD2KD92E37&qid=1690639893&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=mo%2Caps%2C809&sr=1-2-5c1882be-cde7-4e07-b6b0-da12dbf89fb6-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM&th=1"
#     # ]
#     for url in urls:
#         reviews = None
#         while reviews is None:
#             try:
#                 if(count_amazon_reviews(url)>=50):
#                     reviews = get_amazon_reviews(url,val)
#                 else:
#                     return("Error1")
#             except Exception as e:
#                 print(f"Error getting reviews: {e}")
#             if reviews is None:
#                 return (f"Error for {url}")

#             array.append(reviews)

#     processed_reviews = []
#     for product_index, reviews_list in enumerate(array, 1):
#         processed_reviews_for_product = []
        
#         for review in reviews_list:
#             processed_review = review.replace(".", "").strip()
#             processed_reviews_for_product.append(processed_review)
        
#         product_text = f"Product {product_index}: " + ", ".join(processed_reviews_for_product)
#         processed_reviews.append(product_text)

#     return processed_reviews


def function1(processed_reviews):
    number=0
    for i in processed_reviews:
        number+=1

    processed_reviews_str = "\n".join(processed_reviews)
    print(processed_reviews_str)
    Ques="i have "+ str(number) +" products review, identify differences or similarities between them\n"+processed_reviews_str

    # Set APIkey for OpenAI Service
    # Can sub this out for other LLM providers
    os.environ['OPENAI_API_KEY'] = Apikey

    """
    This code demonstrates the usage of the `langchain.llms` module to interact with the OpenAI language model.
    """


    # Define a template for the prompt
    template = """Question: {question}
    Answer: Identify the similarities and differences between the products with the help of the reviews, write the answer step by step"""

    # Create a PromptTemplate with the defined template and input variables
    prompt = PromptTemplate(template=template, input_variables=["question"])

    # Create an instance of the OpenAI language model
    llm = OpenAI()  

    # Create an instance of LLMChain with the prompt and OpenAI language model
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    # Define a question to be processed by the language model
    question = Ques
    Result=llm_chain.run(question)
    # updated_text = Result.replace(".", ".\n")

    print("############# End of Function #################")
    # return(updated_text)
    return Result


def function2(processed_reviews):
    number=0
    for i in processed_reviews:
        number+=1

    processed_reviews_str = "\n".join(processed_reviews)
    print(processed_reviews_str)
    Ques="i have "+ str(number) +" products review, return which product you recommend the most\n"+processed_reviews_str

    # Set APIkey for OpenAI Service
    # Can sub this out for other LLM providers
    os.environ['OPENAI_API_KEY'] = Apikey

    """
    This code demonstrates the usage of the `langchain.llms` module to interact with the OpenAI language model.
    """


    # Define a template for the prompt
    template = """Question: {question}
    Answer: Return which product you recommend the most with the help of the reviews, list the reasons for the answer step by step"""

    # Create a PromptTemplate with the defined template and input variables
    prompt = PromptTemplate(template=template, input_variables=["question"])

    # Create an instance of the OpenAI language model
    llm = OpenAI()  

    # Create an instance of LLMChain with the prompt and OpenAI language model
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    # Define a question to be processed by the language model
    question = Ques
    Result=llm_chain.run(question)
    # updated_text = Result.replace(".", ".\n")

    print("############# End of Function #################")
    # return(updated_text)
    return Result

