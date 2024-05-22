import pandas as pd
import requests
import logging
from tqdm import tqdm
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load the CSV file containing cross-unit terms
file_path = 'cross_unit_terms.csv'
df = pd.read_csv(file_path)

# Function to create a session with retries
def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

# Fetch term labels from the Getty API with retries and timeout
def fetch_term_label(url):
    try:
        response = requests_retry_session().get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data.get('_label', 'Unknown')
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
    return 'Unknown'

# Scrape term labels for cross-unit terms
term_labels = []

# Use tqdm to display a progress bar
for term in tqdm(df['vocab'], desc="Processing terms"):
    term_parts = term.split('/')
    if 'aat' in term_parts:
        term_id = term_parts[-1].split('##')[0]
        term_url = f'http://vocab.getty.edu/aat/{term_id}.json'
    elif 'ulan' in term_parts:
        term_id = term_parts[-1].split('##')[0]
        term_url = f'http://vocab.getty.edu/ulan/{term_id}.json'
    elif 'tgn' in term_parts:
        term_id = term_parts[-1].split('##')[0]
        term_url = f'http://vocab.getty.edu/tgn/{term_id}.json'
    else:
        term_url = None

    if term_url:
        label = fetch_term_label(term_url)
        entity_type = term.split('##')[-1].replace('qua', '').lower()
        term_labels.append([term, label, entity_type])
        print(f"Term: {term}, Label: {label}, Entity: {entity_type}")

# Save term labels to a CSV file
term_labels_df = pd.DataFrame(term_labels, columns=['URL', 'Label', 'Entity'])
term_labels_df.to_csv('intersection-ycba-yuag-vocab.csv', index=False)

logging.info("Scraping completed")
