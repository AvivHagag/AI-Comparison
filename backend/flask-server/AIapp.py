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
import threading
import json

# Shared flag to indicate cancellation
cancel_flag = threading.Event()

def process_url(url, val, result_array, index):
    try:
        if count_amazon_reviews(url) >= 50:
            reviews = get_amazon_reviews(url, val)
            result_array[index] = reviews
        else:
            cancel_flag.set()  # Set the flag to signal cancellation
    except Exception as e:
        print(f"Error getting reviews: {e}")
        return (f"Error for {url}")

def function(name, val):
    # Convert the JSON data string to a Python dictionary
    data = json.loads(name)

    # Extract the links from the dictionary under the key "links"
    urls = data['links']

    results = [None] * len(urls)  # Create a list to store results, one per URL

    threads = []
    
    for index, url in enumerate(urls):
        if not cancel_flag.is_set():  # Check if cancellation flag is not set
            thread = threading.Thread(target=process_url, args=(url, val, results, index))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    if cancel_flag.is_set():
        cancel_flag.clear()  # Reset the flag
        return "Error1"

    processed_reviews = []
    for product_index, reviews_list in enumerate(results, 1):
        if isinstance(reviews_list, list):
            processed_reviews_for_product = [review.replace(".", "").strip() for review in reviews_list]
            product_text = f"Product {product_index}: " + ", ".join(processed_reviews_for_product)
            processed_reviews.append(product_text)
        else:
            processed_reviews.append(reviews_list)

    return processed_reviews


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

