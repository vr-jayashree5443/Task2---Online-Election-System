import mysql.connector

def display_candidates(cursor):
    cursor.execute("SELECT id,name,candidate_party FROM candidates")
    candidates = cursor.fetchall()
    for candidate in candidates:
        print(f"{candidate[0]}. {candidate[1]} ({candidate[2]})")

def vote_candidate(cursor, candidate_id):
    cursor.execute("UPDATE candidates SET votes = votes + 1 WHERE id = %s", (candidate_id,))
    print("Vote added successfully!")

def main():
    # Connect to MySQL
    db_connection = mysql.connector.connect(host="localhost",user="root",password="",database="test")

    cursor = db_connection.cursor()

    while True:
        print("\n==== Online Election System ====")
        print("Candidates:")
        display_candidates(cursor)
        print("Do you want to vote? (y/n): ")
        option = input()

        if option.lower() == 'y':
            candidate_id = int(input("Enter the candidate ID to vote: "))
            vote_candidate(cursor, candidate_id)
            db_connection.commit()
        elif option.lower() == 'n':
            print("Exiting the election system.")
            break
        
    # Close the MySQL connection
    cursor.close()
    db_connection.close()

if __name__ == "__main__":
    main()
