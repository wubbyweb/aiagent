import requests
import configparser

# Function to get the API key from the config file
def get_api_key(config_file='config.ini'):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config['openai']['api_key']

# Function to query the ChatGPT API
def chatgpt_query(prompt, api_key):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "model": "gpt-4",  # Replace with the appropriate model if necessary
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(API_URL, headers=headers, json=data)
    response_json = response.json()
    return response_json["choices"][0]["message"]["content"]

def parse_query(user_query, api_key):
    prompt = f"Break down the following query into actionable steps:\n\n{user_query}"
    steps = chatgpt_query(prompt, api_key)
    return steps.split('\n')

def assign_tasks(steps):
    agents = {}
    for i, step in enumerate(steps):
        agent_id = f"agent_{(i % 5) + 1}"  # Distribute tasks among 5 agents
        if agent_id not in agents:
            agents[agent_id] = []
        agents[agent_id].append(step)
    return agents

def execute_tasks(agents, api_key):
    responses = {}
    for agent_id, tasks in agents.items():
        prompt = f"Execute the following tasks:\n\n{'\n'.join(tasks)}"
        response = chatgpt_query(prompt, api_key)
        responses[agent_id] = response
    return responses

def collate_responses(responses):
    collated_response = ""
    for agent_id, response in responses.items():
        collated_response += f"Response from {agent_id}:\n{response}\n\n"
    return collated_response

def main(user_query):
    # Get the API key from the config file
    api_key = get_api_key()

    # Step 1: Parse the user query into actionable steps
    steps = parse_query(user_query, api_key)

    # Step 2: Assign tasks to different agents
    agents = assign_tasks(steps)

    # Step 3: Execute tasks and get responses
    responses = execute_tasks(agents, api_key)

    # Step 4: Collate responses into a single output
    final_response = collate_responses(responses)

    # Output the final response to the user
    return final_response

# Example usage
if __name__ == "__main__":
    user_query = "Explain how to set up a basic web server and secure it."
    print(main(user_query))
