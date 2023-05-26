import requests
# Import os to set API key
import os
# Import OpenAI as main LLM service
from langchain.llms import OpenAI

from langchain import PromptTemplate, LLMChain
import re


def function(name):
    # Extract the URLs
    matches = re.findall(r'https?://\S+', name)
    # Remove the "]}" characters from the last URL
    last_url = matches[-1].rstrip(']}"')

    # Create the URL list by appending the last URL to the other URLs
    urls = matches[:-1] + [last_url]
    # urls examples 
    # urls = [
    #     "https://drive.google.com/file/d/1yw-NCAtbj-6ZBZoAMrqlfZJ7hqAJjdXu/view?usp=sharing",
    #     "https://drive.google.com/file/d/1YyDUejDkItv12Z9mcN4K5KSBdsSI73pv/view?usp=sharing",
    #     "https://drive.google.com/file/d/1GPhbmxkWm_9ANx3EqeYCxkrNqsYIsjH_/view?usp=sharing",
    #     "https://drive.google.com/file/d/1FkZFUcEnesw8EZVXPWgdwaLQm_JbEU8c/view?usp=sharing",
    #     "https://drive.google.com/file/d/16vKzWx6SDIzaEUe8a6iMVmkT6pkwMZLG/view?usp=sharing"
    # ]

    # Create an array to store the JSON data
    json_array = []

    for url in urls:
        while True:
            try:
                # Find the start and end positions of the ID
                start_pos = url.find("/d/") + 3
                end_pos = url.find("/view")

                # Extract the ID from the link
                file_id = url[start_pos:end_pos]

                # Create the URL with the file ID
                url = "https://drive.google.com/uc?id=" + file_id + "&export=download"

                # Send a request to get the file content
                response = requests.get(url)
                # Append the JSON response to the array
                json_array.append(response.json())
                break  # Break out of the while loop if the code block executes successfully
            
            except Exception as e:
                print(f"An error occurred: {e}")
                continue  # Continue to the next iteration of the while loop if an error occurs

# The code outside the loop (if any) will continue executing after the loop completes
    # List to store the generated responses for each product
    generated_responses = []

    # Generate responses for each product's reviews
    for product_reviews in json_array:
        product_responses = []
            # Loop through the reviews of the product
        for review in product_reviews:
            review_text = review[1]  # Extract the review text from the JSON data 

    processed_reviews = []
    for product_index, product_reviews in enumerate(json_array, 1):
        product_text = f"Product {product_index}:\n"

        # Concatenate all the review texts for the product into a single string with commas
        review_count = 0  # Counter to keep track of the number of reviews processed for the product

        # Concatenate all the review texts for the product into a single string with commas
        for review in product_reviews:
            if review_count >= 100:
                break  # Exit the loop if the review limit for the product is reached

            review_text = review[1]  # Extract the review text from the JSON data
            # Skip if the review text is empty
            if not review_text:
                continue
            # Replace periods with commas and add commas where there are no periods
            if "." in review_text:
                review_text = review_text.replace(".", ",")
            else:
                review_text += ","
            
            product_text += f" {review_text}"
            review_count += 1
        # Add the processed product text to the list
        processed_reviews.append(product_text)

    number=0
    for i in processed_reviews:
        number+=1

    processed_reviews_str = "\n".join(processed_reviews)
    Ques="i have "+ str(number) +" products review, identify differences or similarities between them\n"+processed_reviews_str
    # print(Ques)

    # Set APIkey for OpenAI Service
    # Can sub this out for other LLM providers
    os.environ['OPENAI_API_KEY'] = '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'

    """
    This code demonstrates the usage of the `langchain.llms` module to interact with the OpenAI language model.
    """


    # Define a template for the prompt
    template = """Question: {question}
    Answer: Identify the similarities and differences between the products with the help of the reviews, write the answer step by step and at the end of the answer return the product you recommend the most"""

    # Create a PromptTemplate with the defined template and input variables
    prompt = PromptTemplate(template=template, input_variables=["question"])

    # Create an instance of the OpenAI language model
    llm = OpenAI()  

    # Create an instance of LLMChain with the prompt and OpenAI language model
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    # Define a question to be processed by the language model
    question = Ques
    Result=llm_chain.run(question)

    return(Result)
    print("############# End of Function #################")
    
