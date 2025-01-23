def tim(n):
    # Read input values
    values = input().split(' ')
    
    # Convert input to a list of integers
    valuess = [int(x) for x in values]
    
    # Validate input length
    if len(valuess) != n:
        print("Error: The number of participations does not match the number of players.")
        return None
    
    # Filter players eligible for team formation (participation <= 2)
    eligible_players = [x for x in valuess if x <= 2]
    
    # Calculate the number of teams
    participation = len(eligible_players) // 3
    
    # Return the number of teams
    return participation

# Example usage
n = int(input())
result = tim(n)
if result is not None:
    print(result)
