import pandas as pd
from _parser import list_to_string
import ast

# Function to convert string representation of a list to a dictionary
def string_to_dict(value):
    s = ast.literal_eval(value)
    filtered = [{k: v for k, v in d.items() if v is not None} for d in s]
    return [d for d in filtered if d]


def remove_unncessary(value):
    value = value.replace('\n\n\n', "\n")
    print(value)
    return value

# Function to clean the email dataframe
def clean_df(df):
    df = df[df['emails'] != "[]"]  # Remove rows where emails are empty lists
    df = df.drop_duplicates()  # Remove duplicates
    df['emails'] = df['emails'].apply(string_to_dict)  # Convert string to dictionary
    df['emails'] = df['emails'].apply(list_to_string)  # Convert dict/list to string format
    df['emails'] = df['emails'].apply(remove_unncessary) # remove uncessary string such as multiple \n

    return df


def main(df, main_df):
    # Clean the email dataframe
    cleaned_df = clean_df(df)

    # Merge the two dataframes using a left join to keep all rows from main_df
    temp_df = pd.merge(left=main_df, right=cleaned_df, left_on="Website", right_on="company", how="left")

    # Remove the 'company' column after the merge
    del temp_df['company']

    # Define the columns to keep
    cols = ['Company Name', 'Website', 'emails', 'Current program status', 'Customer type',
        'Description', 'Country', 'Aws certifications count', 'Partner active',
        'References nested', 'Technology expertise', 'Solutions nested',
        'Solutions practice count', 'Industry', 'Refiners',
        'Target client base', 'Language', 'Numberofemployees',
        'Solutions solution count', 'Customer launches count', 'Services count',
        'Literal name', 'Professional service types',
        'References reference count', 'Solution count',
        'Socio economic categories count', 'Timestamp', 'Is saas vendor',
        'Programs count', 'Brief description', 'Solutions',
        'Competencies count', 'Public sector categories count',
        'References casestudy count', 'Office address',
        'Public sector program categories', 'Office address aka',
        'Program membership', 'Public sector contract count', 'Domain',
        'Partner validated', 'Name aka', 'Reference count',
        'Use case expertise', 'Partner path.path detail',
        'Partner path.primary path', 'Public sector contract urls',
        'Public sector contract names', 'Aws certifications', 'References',
        'Software infrastructure', 'Segment', 'Download url',
        'Business software', 'What aws products software uses',
        'Socio economic categories', 'Service membership', 'Developer tools',
        'Competency membership', 'Partner tags', 'Gdpr practice tag',
        'Gdpr practice url', 'Devices']

    # Keep only the specified columns
    temp_df = temp_df[cols]

    # Rename the 'emails' column to 'Email'
    temp_df = temp_df.rename(columns={"emails": "Email"})

    # Replace NaN values in the 'Email' column with an empty string (i.e., leave it blank where no email is found)
    temp_df['Email'] = temp_df['Email'].fillna('')
    temp_df = temp_df.sort_values(by=['Email'], na_position='last')

    temp_df = temp_df[::-1]
    temp_df.reset_index(inplace=True, drop=True)
    # Save or return the final dataframe as required    

    temp_df.to_csv("main_with_email.csv", index=False)
    print(temp_df)


if __name__ == "__main__":
    df = pd.read_csv("email.csv")
    main_df = pd.read_csv("main.csv")

    main(df, main_df)