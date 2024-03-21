import time
import random

def waiting_game():
    wait_time = random.randint(2, 5)
    print("Your target time is {} seconds. Press Enter to begin...".format(wait_time))
    
    input(' ---Press Enter to Begin--- ')

    start_time = time.time()
    input()  # Wait for user to press Enter
    end_time = time.time()
    
    user_response_time = end_time - start_time
    
    if user_response_time < wait_time:
        print("Wow! You were fast! You responded in {:.2f} seconds.".format(user_response_time))
    elif user_response_time > wait_time:
        print("You were a bit slow. You responded in {:.2f} seconds.".format(user_response_time))
    else:
        print("Perfect timing! You responded in exactly {:.2f} seconds.".format(user_response_time))

# Test the function:
waiting_game()

