import requests


def call_llm_api(api_key, api_url, text):
    # Prepare the request headers with your API key
    headers = {"Authorization": f"Bearer {api_key}"}

    # Send the POST request with the text as a JSON payload
    data = {"text": text}
    response = requests.post(api_url, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the generated text from the JSON response
        response_json = response.json()
        generated_text = response_json["generated_text"]
        return generated_text
    else:
        # Handle API errors
        print(f"Error calling LLM API: {response.status_code}")
        return None  # Indicate error or handle it differently