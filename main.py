import json
import time
import pandas as pd
from pathlib import Path
from utils import return_values, request_method, _save, generate_name


save_path = Path('/home/polymorphisma/adex/apollo-scraper-api/archive')

EMAIL_CREDIT_USED = 122
EMAIL_CREDIT_LIMIT = 8000


def create_save_dir(dir_name):
    save_dir = save_path / dir_name
    save_dir.mkdir(parents=True, exist_ok=True)
    return save_dir


def save_json_data(save_dir, file_name, data):
    file_path = save_dir / f'{file_name}.json'
    _save(file_path=str(file_path), result=data)


def get_people(which_: str = "people", organization_id: str = None, file_name: str = None):
    return_result = []
    page_number = 1

    while True:
        time.sleep(0.2)
        method, url, payload, headers = return_values(which_=which_)
        payload.update({'organization_ids': [organization_id], 'page': page_number})

        response = request_method(method, url, json.dumps(payload), headers, isJson=True)
        if response.status_code != 200:
            raise ValueError(f"Scraper stopped working with status code: {response.status_code}. Message: {response.text}")

        result = response.json()
        return_result.append(result)
        save_dir = create_save_dir("people")
        save_json_data(save_dir, file_name, result)

        total_page = result.get("pagination", {}).get("total_pages", 0)
        if page_number >= total_page:
            break
        page_number += 1

    return return_result


def _scraper(request_url: str, which_: str = "organization"):
    method, url, payload, headers = return_values(which_=which_, data=request_url)

    response = request_method(method, url, payload, headers)
    if response.status_code != 200:
        raise ValueError(f"Scraper stopped working with status code: {response.status_code}. Message: {response.text}")

    result = response.json()
    organization = result.get("organizations", [])
    if not organization:
        raise ValueError("Organization Not found")

    organization_id = organization[0].get('id')
    if not organization_id:
        raise ValueError("Organization `id` Not found")

    save_dir = create_save_dir("organization")
    file_name = generate_name(request_url)
    save_json_data(save_dir, file_name, result)

    return get_people(organization_id=organization_id, file_name=file_name)


def _parse_url(url):
    return url.replace("https://", "").replace("http://", "").replace("www.", "").replace("/", "").split("?")[0]


def get_email(which_: str = 'email', user_id: str = None, file_name: str = None):
    global EMAIL_CREDIT_USED, EMAIL_CREDIT_LIMIT

    if EMAIL_CREDIT_USED > EMAIL_CREDIT_LIMIT:
        print(EMAIL_CREDIT_USED)
        raise ValueError("Email Credit Reached.")

    time.sleep(0.2)
    method, url, payload, headers = return_values(which_=which_)
    payload['entity_ids'] = [user_id]

    response = request_method(method, url, json.dumps(payload), headers, isJson=True)
    if response.status_code != 200:
        raise ValueError(f"Scraper stopped working with status code: {response.status_code}. Message: {response.text}")

    result = response.json()
    save_dir = create_save_dir("email_dump")
    save_json_data(save_dir, file_name+"_"+user_id, result)
    title = result.get("contacts", [{}])[0].get("title")
    email = result.get("contacts", [{}])[0].get("email")
    return {title: email}


def _scrape_email(values, request_url: str):
    global EMAIL_CREDIT_USED
    file_name = generate_name(request_url)
    emails = []
    for value in values:
        contacts = value.get("contacts", [])
        people = value.get("people", [])

        for person in contacts + people:
            user_id = person.get("id")
            email_status = person.get("email_status")

            if user_id:
                if email_status == 'verified':
                    EMAIL_CREDIT_USED += 1
                print(EMAIL_CREDIT_USED)
                email = get_email(user_id=user_id, file_name=file_name)
                emails.append(email)

    return emails


def main(file_path: str, start_from: str = ""):
    start = False

    df = pd.read_csv(file_path)
    all_emails = {}

    email_df = pd.DataFrame()

    for _, row in df.iterrows():
        url = _parse_url(row['Website'])

        if url == start_from or start_from == "":
            start = True

        if not start:
            continue

        print(url)
        print('-----' * 10)

        try:
            value = _scraper(request_url=url)
            emails = _scrape_email(value, request_url=url)

            all_emails[row['Website']] = emails
            temp_df = pd.DataFrame(list(all_emails.items()), columns=['company', 'emails'])
            if len(temp_df) == 0:
                continue
            email_df = pd.concat([email_df, temp_df])
            email_df.to_csv("email.csv", index = False)

        except Exception as exp:
            with open("error.txt", 'a') as af:
                af.write(f"{url} {str(exp)}")
                af.write("\n")


if __name__ == "__main__":
    start_from = ""
    main("main.csv")
