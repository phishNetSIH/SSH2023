from tensorflow import keras
import re
from urllib.parse import urlparse
import pandas as pd

def first_directory_length(url: str):
    urlpath: str = urlparse(url).path
    try:
        return len(urlpath.split("/")[1])
    except:
        return 0

# Case Change Count
def count_case_change(input_string):
    switch_count = 0
    prev_case = None
    for char in input_string:
        if char.isalpha() and (char.isupper() == (not prev_case)):
            switch_count += 1
            prev_case = char.isupper() if char.isalpha() else None
    return switch_count

def ip_present(url: str):
    match = re.search(
        "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[0-9a-fA-F]{1,4}(:[0-9a-fA-F]{1,4}){7}", url
    )
    return 1 if match else 0


def extract_features(url):
    df = pd.DataFrame()
    df['url'] = [url]
    res = []
    res.append(df["url"].apply(lambda i: len(i)))
    res.append(df["url"].apply(lambda i: len(urlparse(i).netloc)))
    #res.append(df["url"].apply(lambda i: len(urlparse(i).path)))
    res.append(df["url"].apply(lambda i: first_directory_length(i)))
    # Char Count
    chars_to_count = []
    for i in range(33, 40) or i in range(58, 65):
        if not (chr(i).isalnum() or chr(i) == '"' or chr(i) == '#'):
            chars_to_count.append(chr(i))

    for i in chars_to_count:
        res.append(df["url"].apply(lambda url: url.count(i)))
    res.append(df["url"].apply(lambda url: url.count("http")))
    res.append(df["url"].apply(lambda url: url.count("https")))
    res.append(df["url"].apply(lambda url: url.count("www")))
    res.append(df["url"].apply(lambda url: len([i for i in url if i.isnumeric()])))
    res.append(df["url"].apply(lambda url: len([i for i in url if i.isalpha()])))
    res.append(df["url"].apply(lambda url: urlparse(url=url).path.count("/")))

    res.append(df["url"].apply(lambda url: count_case_change(url)))
    res.append(df["url"].apply(lambda url: ip_present(url=url)))

    ret = []
    for i in res:
        ret.append(int(i))
    return ret

MODEL_PATH = "api\\idk_model.h5"

def get_prediction(url):

    model = keras.models.load_model(MODEL_PATH)
    url_features = extract_features(url)
    prediction = model.predict([url_features])
    i = prediction[0][0] * 100
    i = round(i, 3)
    return i


#print(extract_features("https://data-a752c.web.app/"))
