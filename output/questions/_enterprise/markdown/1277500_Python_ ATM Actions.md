# Python: ATM Actions

## Metadata

- **ID:** 1277500
- **Type:** code
- **Difficulty:** 1
- **Points:** 100
- **Duration:** N/A minutes
- **Tags:** Python, Python 3, Hard
- **Skills:** Python (Advanced)
- **Languages:** p, y, t, h, o, n, 3

## Summary

This coding question evaluates state machine design, transition logic, and ATM operations concepts, ideal for senior-level roles. The problem requires implementing an ATM system that manages state transitions based on user actions and checks for valid operations.

## Problem Statement

Implement the transition logic for an ATM system that follows a state machine design pattern. The ATM has two states: unauthorized (initial state) and authorized (after successful login).

 

Transition Requirements

Define the transition_table variable as a Dictionary where:

	
- Keys are State objects
	
- Values are lists of transitions supported in that state.

Each transition is a 3-element tuple: (action_name, checker, next_state)

 

The checker function has this signature:

checker(action_param: Optional, atm_password: str, atm_current_balance: int) -> Tuple[bool, int, Optional]

```

 

The returned tuple contains:

	
- A boolean indicating if the transition should be performed
	
- The updated ATM balance after the transition
	
- An optional return value (only used for balance inquiries)

Supported Actions

In the unauthorized state:

	
- 
login <password> - Transitions to authorized state if password is correct

In the authorized state:

	
- 
logout - Transitions back to unauthorized state
	
- 
deposit <amount> - Adds the specified amount to the balance
	
- 
withdraw <amount> - Deducts the specified amount if sufficient funds exist
	
- 
balance - Returns the current balance

Implementation Context

The ATM class is already provided:

class ATM:
    def __init__(self, init_state: State, init_balance: int, password: str, transition_table: Dict):
        self.state = init_state
        self._balance = init_balance
        self._password = password
        self._transition_table = transition_table

    def next(self, action: Action, param: Optional) -> Tuple[bool, Optional]:
        try:
            for transition_action, check, next_state in self._transition_table[self.state]:
                if action == transition_action:
                    passed, new_balance, res = check(param, self._password, self._balance)
                    if passed:
                        self._balance = new_balance
                        self.state = next_state
                        return True, res
        except KeyError:
            pass
        return False, None

```

 

Your implementation will be tested by a provided code stub on several input files. Each input file contains the password for the ATM and its initial balance. Then, it contains descriptions of the actions that will be performed on the ATM by the provided code. The result of each transition is printed to the standard output by the provided code.

 

 DO NOT REMOVE THIS LINE-->

Input Format Format for Custom Testing

In the first line, there is a single string, password, the correct password.

In the second line, there is a single integer, init_balance, the initial balance of the ATM.

In the third line, there is a single integer, q, the number of actions the ATM will be tested on.

Each of the next, q lines describes an action request.

 DO NOT REMOVE THIS LINE-->

Sample Case 0

Sample Input

hacker
10
8
withdraw 5
login foo
login hacker
withdraw 15
deposit 20
withdraw 15
balance
logout

```

 

Sample Output

Success=False unauthorized
Success=False unauthorized
Success=True authorized
Success=False authorized
Success=True authorized
Success=True authorized
Success=True authorized 15
Success=True unauthorized

```

 

Explanation

The ATM's password is "hacker" and its initial balance is 10. There are 8 actions to perform. The first action tries to withdraw 5 from the ATM but since it always starts in the "unauthorized" state, this action is unsuccessful. The second action tries to log in with the password "foo". This does not match the ATM's password, so the action is also unsuccessful. The third action tries to log in with the correct password "hacker". This action is successful, so the ATM moves to the "authorized" state. The next action tries to withdraw 15 from the ATM but this amount is greater than the current balance of the ATM, so the action is unsuccessful. The fourth action deposits 20 into the ATM, so its current balance is now 10 + 20 = 30. The next action, again, tries to withdraw 15, and it successfully changes the balance of the ATM to 30-15=15. The next action gets the current balance of the ATM, i.e.,15. The last action logs out, so the ATM moves to the "unauthorized" state.

Sample Case 1

Sample Input

somepass
100
5
logout
login somepass
balance
login somepass
login wrongpass

```

 

Sample Output

Success=False unauthorized
Success=True authorized
Success=True authorized 100
Success=False authorized
Success=False authorized

```

 

Explanation

The ATM's password is "somepass" and its initial balance is 100. There are 5 actions to be performed. The first action tries to log out, but since the ATM always starts in the "unauthorized" state, this action is unsuccessful. The second action tries to log in with the correct password "somepass". This action is successful, so the ATM moves to the "authorized" state. The next action gets the balance of the ATM, so 100 is returned. The next two actions both try to log in, but since the ATM is already in the "authorized" state, both of them are unsuccessful.

## Sample Input/Output

## Preview

Implement the transition logic for an ATM system that follows a state machine
