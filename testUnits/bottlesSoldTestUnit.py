import requests
import json
import payLeafTestUnit as pl

def check_and_update_balance(previous_balance) -> float:
    """Check the balance and update the count of bottles sold"""
    try:
        with open('config.json', 'r') as file:
            config = json.load(file)
            endpoint_url = str(config['endpoint'])
    except FileNotFoundError:
        print("CONFIG FILE NOT FOUND")
    
    # Request to get the balance
    response = requests.get(endpoint_url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:    
        # Parse the response JSON
        
        data = response.json()
        print(f"balance now: {data['L_AMT0']}")
        previous_balance = float(input("previous balance: "))
        # Check if the balance is greater than the previous balance
        if "L_AMT0" in data and float(data["L_AMT0"]) > previous_balance:
            # Update the count of bottles sold and check if the balance has increased by more than 1
            times = (float(data["L_AMT0"]) - previous_balance)
            pl.payLeaf2()
            for _ in range(int(times)):
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
        with open('bottle_count.json', 'r') as file:
            count_dict = json.load(file)
            count = int(count_dict['count'])
    except FileNotFoundError:
        print("FILE NOT FOUND")
        count = 0
    
    # Increment the count
    count += 1
    
    # Save the updated count back to the text file
    with open('bottle_count.json', 'w') as file:
        json.dump({"count": count}, file)
    
    print(f"Bottle sold! Total bottles sold: {count}")

def main() -> None:
    """Main function"""
    try:
        # Initial balance (set to a very low value as a starting point)
        previous_balance = 9999

        # Run the script in a loop
        
        # Check and update the balance
        previous_balance = check_and_update_balance(previous_balance)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
