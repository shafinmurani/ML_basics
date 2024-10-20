import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score
from urllib.parse import urlparse
import re
import tkinter as tk
from tkinter import messagebox

# Load dataset from CSV
df = pd.read_csv('dataset_full.csv')

# Define features (X) and target variable (y)
X = df.drop(columns=['phishing'])  # Drop the target variable column
y = df['phishing']  # Use 'phishing' as the label column

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the KNN model
model = KNeighborsClassifier(n_neighbors=3)  # You can adjust the number of neighbors
model.fit(X_train, y_train)

# Calculate accuracy on the test set
accuracy = model.score(X_test, y_test) * 100  # Convert to percentage

# Function to extract features from the URL
def extract_url_features(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    path = parsed_url.path
    query = parsed_url.query

    # Extract features
    features = {
        'qty_dot_url': url.count('.'),
        'qty_hyphen_url': url.count('-'),
        'qty_underline_url': url.count('_'),
        'qty_slash_url': url.count('/'),
        'qty_questionmark_url': url.count('?'),
        'qty_equal_url': url.count('='),
        'qty_at_url': url.count('@'),
        'qty_and_url': url.count('&'),
        'qty_exclamation_url': url.count('!'),
        'qty_space_url': url.count(' '),
        'qty_tilde_url': url.count('~'),
        'qty_comma_url': url.count(','),
        'qty_plus_url': url.count('+'),
        'qty_asterisk_url': url.count('*'),
        'qty_hashtag_url': url.count('#'),
        'qty_dollar_url': url.count('$'),
        'qty_percent_url': url.count('%'),
        'qty_tld_url': len(domain.split('.')[-1]),  # Length of TLD
        'length_url': len(url),
        
        # Domain features
        'qty_dot_domain': domain.count('.'),
        'qty_hyphen_domain': domain.count('-'),
        'qty_underline_domain': domain.count('_'),
        'qty_slash_domain': domain.count('/'),
        'qty_questionmark_domain': domain.count('?'),
        'qty_equal_domain': domain.count('='),
        'qty_at_domain': domain.count('@'),
        'qty_and_domain': domain.count('&'),
        'qty_exclamation_domain': domain.count('!'),
        'qty_space_domain': domain.count(' '),
        'qty_tilde_domain': domain.count('~'),
        'qty_comma_domain': domain.count(','),
        'qty_plus_domain': domain.count('+'),
        'qty_asterisk_domain': domain.count('*'),
        'qty_hashtag_domain': domain.count('#'),
        'qty_dollar_domain': domain.count('$'),
        'qty_percent_domain': domain.count('%'),
        'qty_vowels_domain': len(re.findall(r'[aeiou]', domain)),
        'domain_length': len(domain),
        'domain_in_ip': 1 if re.match(r'\d+\.\d+\.\d+\.\d+', domain) else 0,  # Check if the domain is an IP
        'server_client_domain': 1 if 'server' in domain or 'client' in domain else 0,

        # Directory features
        'qty_dot_directory': path.count('.'),
        'qty_hyphen_directory': path.count('-'),
        'qty_underline_directory': path.count('_'),
        'qty_slash_directory': path.count('/'),
        'qty_questionmark_directory': path.count('?'),
        'qty_equal_directory': path.count('='),
        'qty_at_directory': path.count('@'),
        'qty_and_directory': path.count('&'),
        'qty_exclamation_directory': path.count('!'),
        'qty_space_directory': path.count(' '),
        'qty_tilde_directory': path.count('~'),
        'qty_comma_directory': path.count(','),
        'qty_plus_directory': path.count('+'),
        'qty_asterisk_directory': path.count('*'),
        'qty_hashtag_directory': path.count('#'),
        'qty_dollar_directory': path.count('$'),
        'qty_percent_directory': path.count('%'),
        'directory_length': len(path),

        # File features
        'qty_dot_file': path.count('.'),
        'qty_hyphen_file': path.count('-'),
        'qty_underline_file': path.count('_'),
        'qty_slash_file': path.count('/'),
        'qty_questionmark_file': path.count('?'),
        'qty_equal_file': path.count('='),
        'qty_at_file': path.count('@'),
        'qty_and_file': path.count('&'),
        'qty_exclamation_file': path.count('!'),
        'qty_space_file': path.count(' '),
        'qty_tilde_file': path.count('~'),
        'qty_comma_file': path.count(','),
        'qty_plus_file': path.count('+'),
        'qty_asterisk_file': path.count('*'),
        'qty_hashtag_file': path.count('#'),
        'qty_dollar_file': path.count('$'),
        'qty_percent_file': path.count('%'),
        'file_length': len(path),

        # Parameter features
        'qty_dot_params': query.count('.'),
        'qty_hyphen_params': query.count('-'),
        'qty_underline_params': query.count('_'),
        'qty_slash_params': query.count('/'),
        'qty_questionmark_params': query.count('?'),
        'qty_equal_params': query.count('='),
        'qty_at_params': query.count('@'),
        'qty_and_params': query.count('&'),
        'qty_exclamation_params': query.count('!'),
        'qty_space_params': query.count(' '),
        'qty_tilde_params': query.count('~'),
        'qty_comma_params': query.count(','),
        'qty_plus_params': query.count('+'),
        'qty_asterisk_params': query.count('*'),
        'qty_hashtag_params': query.count('#'),
        'qty_dollar_params': query.count('$'),
        'qty_percent_params': query.count('%'),
        'params_length': len(query),
        'tld_present_params': 1 if any(tld in query for tld in ['.com', '.org', '.net']) else 0,
        'qty_params': len(query.split('&')) if query else 0,

        # Other features
        'email_in_url': 1 if re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', url) else 0,
        'time_response': -1,  # Placeholder for time response
        'domain_spf': -1,  # Placeholder for domain SPF
        'asn_ip': -1,  # Placeholder for ASN
        'time_domain_activation': -1,  # Placeholder for time of domain activation
        'time_domain_expiration': -1,  # Placeholder for time of domain expiration
        'qty_ip_resolved': -1,  # Placeholder for resolved IP count
        'qty_nameservers': -1,  # Placeholder for nameserver count
        'qty_mx_servers': -1,  # Placeholder for MX server count
        'ttl_hostname': -1,  # Placeholder for TTL
        'tls_ssl_certificate': -1,  # Placeholder for SSL certificate validity
        'qty_redirects': -1,  # Placeholder for redirect count
        'url_google_index': -1,  # Placeholder for Google index check
        'domain_google_index': -1,  # Placeholder for domain Google index check
        'url_shortened': -1,  # Placeholder for URL shortening check
    }

    # Convert features to a DataFrame
    features_df = pd.DataFrame([features])
    return features_df

# Function to predict if the input domain is phishing
def predict_phishing(url):
    features_df = extract_url_features(url)
    prediction = model.predict(features_df)  # Use the features as a DataFrame
    return prediction[0]

# Function to handle the button click event
def on_predict_button_click():
    url = url_entry.get()
    if url:
        result = predict_phishing(url)
        if result == 1:
            messagebox.showinfo("Result", "The URL is a phishing site.")
        else:
            messagebox.showinfo("Result", "The URL is safe.")
    else:
        messagebox.showwarning("Input Error", "Please enter a URL.")

# Create the main window
root = tk.Tk()
root.title("Phishing Detection Tool")

# Create and place the URL input label and entry
url_label = tk.Label(root, text="Enter URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

# Create and place the accuracy label
accuracy_label = tk.Label(root, text=f"Model Accuracy: {accuracy:.2f}%")
accuracy_label.pack(pady=10)

# Create and place the predict button
predict_button = tk.Button(root, text="Check Phishing", command=on_predict_button_click)
predict_button.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()
