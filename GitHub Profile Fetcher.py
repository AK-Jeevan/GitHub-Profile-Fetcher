import requests

def fetch_github_profile(username):
    """
    Fetches and displays GitHub profile information for a given username.
    """
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        print(f"GitHub Profile for: {user_data['login']}")
        print(f"Name: {user_data.get('name', 'N/A')}")
        print(f"Bio: {user_data.get('bio', 'N/A')}")
        print(f"Location: {user_data.get('location', 'N/A')}")
        print(f"Public Repositories: {user_data['public_repos']}")
        print(f"Followers: {user_data['followers']}")
        print(f"Following: {user_data['following']}")
        print(f"GitHub URL: {user_data['html_url']}")
    elif response.status_code == 404:
        print("Error: User not found.")
    else:
        print(f"Error: Unable to fetch data (Status code: {response.status_code})")

if __name__ == "__main__":
    print("Welcome to the GitHub Profile Fetcher!")
    username = input("Enter the GitHub username: ").strip()
    fetch_github_profile(username)
