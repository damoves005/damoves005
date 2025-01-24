import os
from datetime import datetime
from dateutil import relativedelta
import requests
from lxml import etree

def update_svg(mode):
    svg_file = f"{mode}_mode.svg"
    tree = etree.parse(svg_file)
    root = tree.getroot()
    
    # Update dynamic content
    age = calculate_age()
    update_text_element(root, 'age_data', age)
    
    # Save updated SVG
    tree.write(svg_file, encoding='utf-8', xml_declaration=True)

def calculate_age():
    birthday = datetime(1995, 1, 1)  # Replace with your birthday
    today = datetime.now()
    diff = relativedelta.relativedelta(today, birthday)
    return f"{diff.years} Years"

def update_text_element(root, element_id, new_text):
    element = root.find(f".//*[@id='{element_id}']")
    if element is not None:
        element.text = str(new_text)

if __name__ == '__main__':
    update_svg('dark')
    update_svg('light')