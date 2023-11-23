import pandas as pd
from bs4 import BeautifulSoup

# Assuming you have already created the BeautifulSoup object 'soup' containing the web page content

# Find all tr tags
tr_tags = soup.find_all('tr')

# Initialize an empty list to store dictionaries for each row
data_list = []

# Loop through each tr tag
for tr_tag in tr_tags:
    # Extract the relevant data from each td tag within the tr tag
    tds = tr_tag.find_all('td')
    if len(tds) == 9:  # Ensure it's the correct row with 9 td elements
        department = tds[0].text.strip()
        dept_seq = tds[1].find('div', class_='dept_seq').text.strip()
        course_code = tds[1].contents[2].strip()
        department_type = tds[3].text.strip()
        course_name = tds[4].find('a').text.strip()
        credit = tds[5].text.strip()
        instructor = tds[6].text.strip()
        enrollment_status = tds[7].text.strip()
        location = tds[8].text.strip()
        
        # Create a dictionary for each row and append it to the data_list
        data_dict = {
            'Department': department,
            'Department Sequence': dept_seq,
            'Course Code': course_code,
            'Department Type': department_type,
            'Course Name': course_name,
            'Credit': credit,
            'Instructor': instructor,
            'Enrollment Status': enrollment_status,
            'Location': location
        }
        data_list.append(data_dict)

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data_list)

# Display the DataFrame as a table in Jupyter Notebook
df
