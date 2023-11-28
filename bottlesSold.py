import requests
import json

def check_and_update_balance(previous_balance) -> float:
    """Check the balance and update the count of bottles sold"""
    # Replace endpoint_url with the actual endpoint URL
    endpoint_url = 'https://ngitl-self-service-functions.azurewebsites.net/api/drinks/balance?'
    
    # Request to get the balance
    response = requests.get(endpoint_url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()
        
        # Check if the balance is greater than the previous balance
        if "L_AMT0" in data and float(data["L_AMT0"]) > previous_balance:
            # Update the count of bottles sold
            update_bottle_count()
            
            # Update the previous balance to the new balance
            previous_balance = float(data["L_AMT0"])

        elif "L_AMT0" in data and float(data["L_AMT0"]) < previous_balance:
            # Update the previous balance to the new balance
            previous_balance = float(data["L_AMT0"])
    else:
        print(f"Failed to get balance. Status code: {response.status_code}")

    return previous_balance

def update_bottle_count() -> None:
    """Update the count of bottles sold and save it to a text file"""
    # Read the current count from the text file
    try:
        with open('bottle_count.txt', 'r') as file:
            count = int(file.read())
    except FileNotFoundError:
        print("FILE NOT FOUND")
        count = 0
    
    # Increment the count
    count += 1
    
    # Save the updated count back to the text file
    with open('bottle_count.txt', 'w') as file:
        file.write(str(count))
    
    print(f"Bottle sold! Total bottles sold: {count}")

def main() -> None:
    """Main function"""
    try:
        # Initial balance (set to a very low value as a starting point)
        previous_balance = 0.0

        # Run the script in a loop
        while True:
            # Check and update the balance
            previous_balance = check_and_update_balance(previous_balance)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()