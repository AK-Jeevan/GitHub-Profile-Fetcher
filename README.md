GitHub Profile Fetcher

A simple Python script to fetch and display details about a GitHub user using the GitHub API. Enter a GitHub username, and the script retrieves information such as the user's name, bio, location, public repositories, followers, and profile URL.

Features :

Fetches user profile information directly from the GitHub API.
Displays the following details:
Username
Name
Bio
Location
Number of public repositories
Number of followers and following
GitHub profile URL

Handles errors such as invalid usernames or network issues.

Prerequisites

Python 3.6 or higher installed on your system.
The requests library installed. You can install it using the following command:
pip install requests
How to Use
Clone this repository or copy the script file.

Open a terminal or command prompt.

Run the script using Python:
python github_profile_fetcher.py
Enter the GitHub username when prompted.

Example Usage

Welcome to the GitHub Profile Fetcher!
Enter the GitHub username: octocat
GitHub Profile for: octocat
Name: The Octocat
Bio: N/A
Location: San Francisco
Public Repositories: 8
Followers: 6804
Following: 9
GitHub URL: https://github.com/octocat

Error Handling

If the entered username does not exist on GitHub, the script will display an error message:
Error: User not found.
If there’s a network issue or the API is unreachable, the script will display a message with the corresponding HTTP status code.

Future Improvements

Add a graphical user interface (GUI) for better usability.
Implement caching to reduce redundant API calls for frequently searched users.
Support fetching additional information such as a list of repositories.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to use or customize this script for your projects. Contributions and feedback are always welcome! 😊
