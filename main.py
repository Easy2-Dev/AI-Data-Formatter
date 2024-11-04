
from dotenv import load_dotenv, find_dotenv
import os

from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import MessagesPlaceholder
from langchain_core.messages import HumanMessage, SystemMessage

from langchain_openai import ChatOpenAI


import json




# Load environment variables from .env file
load_dotenv(find_dotenv())

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=os.getenv("OPENAI_API_KEY"))

parser = StrOutputParser()


# Define directories
input_dir = './input'  # Directory with input JSON files
output_dir = './output'  # Directory for saving output JSON files

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

prompt = ChatPromptTemplate.from_messages(
                [
                    SystemMessage(content="""
                Category List = Macbook Air, Macbook Pro, Mac Mini, iMac, Mac Studio, iPad Air, iPad Pro, iPad 9th Gen, iPad 10th Gen, iPhone 11 Series, iPhone 12 Series, iPhone 13 Series, iPhone 14 Series, iPhone 15 Series, iPhone 16 Series, Refurbished, Apple watch series 8, Apple Watch Ultra, Apple Watch Series 9, Apple watch SE, Series 6, Series 10, AirPods Pro (2nd Generation), AirPods (2nd Generation), AirPods (3rd Generation), AirPods Max, Genuine, Samsung Galaxy M Series, Samsung Galaxy A Series, Samsung F series, Samsung Tabs, Samsung S Series, Z Series, Galaxy watch, Galaxy Buds, Google Pixel 6 Series, Google Pixel 7 Series, Google Pixel 8 Series, Google Pixel Fold, Google Pixel 9 Series, Redmi A Series, Redmi Note Series, C Series, Realme, Huawei Y Series, Huawei 9 Series, Oppo A Series, OnePlus 9 Series, OnePlus 10 Series, OnePlus Nord, Nokia 105, Tabs, G5 Series, T Series, A Series, 50 Series, 40 Series, Acer Laptops, ASUS Laptops, DELL Laptops, HP Laptops, Lenovo Laptops, MSI Laptops, UPS, For Home, For Work, For Gaming, Ink Tank Printer, Dot Matrix Printer, Plotter, Speaker, Microphones, Headset, Ear Buds, Handfree, CCTV Camera's, DVR Kits, Webcam and Accessories, Joyroom, Wireless Key Board & Mouse, KeyBoard & Mouse, Pen Drive, Micro SD Card, Converter & Cable, OTG PEN DRIVE - TYPE C l MICRO DUCO, Internal Hard Drive, External Hard Drive, RAM, SSD, Adapter And Cable, Cover & Cases, Power Bank, Tempered Glass, Cartridge, Toner, Ink Bottle, Laptop Adaptors, Laptop Display, Laptop Battery, Laptop Keyboards, OEM, MacBook Battery, MacBook Display, MacBook Motherboard, iPhone (Pre Owned / Used), Pre Owned DELL Laptops, Pre Owned HP Laptops, Pre Owned LENOVO Laptops, MacBook Air (Pre-owned / Used), MackBook Pro (Pre-Owned / Used), iPad Air Pre-owned (Used), Apple watch Pre-owned (Used), Pre-owned DELL Monitors, iPhone 11 Series (Daily Deals), iPhone 13 Series (Daily Deals), iPhone 14 Series (Daily Deals), Macbook.
                
                1.Assign a relevant category from the provided Category List to product in the JSON map, using the product's image URL as a reference to determine its category.
                2.Assign a random price for each product.
                3.Generate random values for each product's product_name and description.
                4.Keep the "id" and "image_list" exact same as the provided one.
                5.Format the attributes field like this:[{"name": "Size", "values": ["20", "30"]},{"name": "Capacity", "values": ["120GB", "320GB"]}].
                6.Format the colors field like this:[{"name": "blue", "hex_code": "0000FF"},{"name": "red", "hex_code": "FF0000"}].
                7.Keep raw string only. remove "/" and "/n".
                8.Ensure only contain the map other any texts shuld remove. like json etc..
                """),
            
            
                MessagesPlaceholder(variable_name="inputPrompt"),

                
                ]
            )

def chat_with_ai(human_input):
   
    # Define the LLM chain
    llm_chain = prompt | llm | parser


    # Predict the output
    output = llm_chain.invoke({"inputPrompt": [HumanMessage(content=human_input)]})
   
    return output


for filename in os.listdir(input_dir):
    if filename.endswith('.json'):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)  # Same name for output file in output directory
        
        
        with open(input_path, 'r') as file:
            data = json.load(file)

            # Initialize an empty list to store responses
        responses = []

         # Process each map in the JSON file
        for idx, map_data in enumerate(data):
            human_message = HumanMessage(content=json.dumps(map_data))

                # Get the response for the current map
            output = chat_with_ai(human_message.content)
                
                # # Store the response in a dictionary
            responses.append(output)
            print(f"Processed map {idx+1}/{len(data)}  in file {filename}")


            # Save the responses to the output JSON file
                # Save the responses to an output JSON file
        with open(output_path, 'w') as outfile:
            outfile.write("[\n") 
            for i, item in enumerate(responses): 
                if i < len(responses) - 1: 
                    outfile.write("%s,\n" % item) 
                else: 
                    outfile.write("%s\n" % item) 
            outfile.write("]")
        print(f"Finished processing {filename}, output saved to {output_path}")







   







