import pandas as pd
import json
import os
import uuid


def read_json(path: str):
    with open(path) as f:
        d = json.load(f)
    return d


def return_files(path, full_path: bool = True):
    if full_path:
        return [os.path.join(path, x) for x in os.listdir(path)]

    return [x for x in os.listdir(path)]


def return_domain(path, file_name):
    using_value = file_name.split("/")[-1]
    using_value = using_value.replace(".json", "")
    using_value = using_value.rpartition("_")[0]

    domain_path = os.path.join(path, 'organization', using_value+'.json')

    dicts = read_json(domain_path)
    domain = dicts[0].get("organizations", [{}])[0].get("domain", None)
    return domain


def parse_value(val):
    if val is None:
        return val
    val = val.replace(",", "_")
    return val


def parse(value: dict, save_list: list, domain: str):
    for val in value:
        # second_using = val.get("")
        title = val.get("contacts", [{}])[0].get("title")
        email = val.get("contacts", [{}])[0].get("email")
        name = val.get("contacts", [{}])[0].get("name")
        linkedin_url = val.get("contacts", [{}])[0].get("linkedin_url")
        # organization = val.get("contacts", [{}])[0].get("name")

        if email is None:
            continue

        save_list.append({
            "Title": title,
            "Email": email,
            "Name": name,
            "Website": domain,
            "Linkedin": linkedin_url
        })


# Function to create the new DataFrame
def transform_dataframe(df):
    # Group by the 'Website' and aggregate the 'Title', 'Name', and 'Email'
    for col in list(df.columns):
        print(col)
        df[col] = df[col].apply(parse_value)
        # print(df[col])

    df.to_csv(f"{str(uuid.uuid4())}.csv", index=False)
    grouped_df = df.groupby('Website').apply(
        lambda x: ', '.join(f"{row['Name']} ({row['Title']}): {row['Email']}" for _, row in x.iterrows())
    ).reset_index(name='value')

    return grouped_df


def main(path: str):
    files = return_files(os.path.join(path, "email_dump"))

    values = []

    for file in files:
        json_ = read_json(file)
        print(json_)
        domain = return_domain(path, file)
        parse(json_, values, domain)
        # exit()

    df = pd.DataFrame(values)
    df.to_csv("testing_for_email.csv", index=False)

    # df = pd.read_csv("email.csv")
    df = df.drop_duplicates()
    print(df)
    print(len(set(df['Website'])))
    new_df = transform_dataframe(df)
    print(new_df)
    new_df.to_csv("domain_based_email_csv.csv", index=False)


if __name__ == "__main__":
    file_path = r'/home/polymorphisma/adex/apollo-scraper-api/outreach/outreach_data_1'
    main(file_path)
