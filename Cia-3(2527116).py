# File paths
USER_FILE = "users.txt"
CANDIDATE_FILE = "candidates.txt"
VOTES_FILE = "votes.txt"


# Initialize files
def initialize_files():
    files = [USER_FILE, CANDIDATE_FILE, VOTES_FILE]
    for file in files:
        with open(file, 'a'):
            pass


# Register new voter
def register_voter():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open(USER_FILE, 'r') as f:
        users = [line.strip().split(',') for line in f.readlines()]

    for user in users:
        if user[0] == username:
            print("Username already exists!")
            return

    with open(USER_FILE, 'a') as f:
        f.write(f"{username},{password}\n")

    print("Registration successful!")


# Authenticate user
def authenticate():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open(USER_FILE, 'r') as f:
        users = [line.strip().split(',') for line in f.readlines()]

    for user in users:
        if user[0] == username and user[1] == password:
            print("Login successful!")
            return username

    print("Invalid credentials!")
    return None


# Add candidate
def add_candidates():
    name = input("Enter candidate name: ")

    with open(CANDIDATE_FILE, 'r') as f:
        candidates = [line.strip().split(',')[0] for line in f.readlines()]

    if name in candidates:
        print("Candidate already exists!")
        return

    with open(CANDIDATE_FILE, 'a') as f:
        f.write(f"{name},0\n")

    print("Candidate added successfully!")


# Cast vote
def cast_vote(voter):

    with open(VOTES_FILE, 'r') as vf:
        votes = [line.strip().split(',') for line in vf.readlines()]

    for v in votes:
        if v[0] == voter:
            print("You have already voted!")
            return

    with open(CANDIDATE_FILE, 'r') as cf:
        candidates = [line.strip().split(',') for line in cf.readlines()]

    print("Candidates:")
    for c in candidates:
        print(c[0])

    choice = input("Enter candidate name to vote: ")

    updated_candidates = []
    found = False

    for c in candidates:
        name, vote_count = c
        if name == choice:
            vote_count = str(int(vote_count) + 1)
            found = True

        updated_candidates.append(f"{name},{vote_count}\n")

    if not found:
        print("Invalid candidate!")
        return

    with open(CANDIDATE_FILE, 'w') as cf:
        cf.writelines(updated_candidates)

    with open(VOTES_FILE, 'a') as vf:
        vf.write(f"{voter},{choice}\n")

    print("Vote cast successfully!")


# Display results
def show_results():
    with open(CANDIDATE_FILE, 'r') as cf:
        candidates = [line.strip().split(',') for line in cf.readlines()]

    print("\nElection Results:")
    for name, votes in candidates:
        print(f"{name}: {votes} votes")


# Main menu
def main():

    initialize_files()

    while True:

        print("\n1. Register")
        print("2. Login & Vote")
        print("3. Add Candidate")
        print("4. View Results")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register_voter()

        elif choice == "2":
            voter = authenticate()
            if voter:
                cast_vote(voter)

        elif choice == "3":
            add_candidates()

        elif choice == "4":
            show_results()

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

