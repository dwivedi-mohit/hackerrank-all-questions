# Circuit Breaker Pattern

## Metadata

- **ID:** 2272901
- **Type:** code
- **Difficulty:** 1
- **Points:** 50
- **Duration:** N/A minutes
- **Tags:** Easy, Javascript, State Machine, Conditional Logic, Object destructuring, Arrays and Strings
- **Skills:** JavaScript (Basic)
- **Languages:** j, a, v, a, s, c, r, i, p, t

## Summary

This coding question evaluates state machines, conditional logic, and object destructuring concepts, ideal for junior-level roles. The problem requires implementing a circuit breaker with three states to manage requests based on success and failure conditions.

## Problem Statement

Your backend relies on an unreliable third-party service. When it starts failing, repeated retries cascade and overload the system. Add a circuit breaker to cut off calls until the upstream recovers.

Implement a circuit breaker with three states: CLOSED (normal operation), OPEN (reject requests), and HALF_OPEN (testing recovery).

Rules:

- The circuit starts in CLOSED state.

- 
Track consecutive failures; when they reach failureThreshold, transition to OPEN.

- In OPEN state, reject all requests and ignore their results.

- 
After timeout milliseconds in OPEN, transition to HALF_OPEN to test recovery.

- 
In HALF_OPEN, count consecutive successes; after successThreshold successes, transition back to CLOSED.

- Any failure in HALF_OPEN immediately reopens the circuit (back to OPEN).

Return the state for each request in the order they are processed. The state label reflects the circuit state before that request's result is applied.

Example 1

Input:

6
req1 100 success
req2 200 failure
req3 300 failure
req4 400 failure
req5 1500 success
req6 1600 success
2
1
1000
```

Output:

CLOSED
CLOSED
CLOSED
OPEN
HALF_OPEN
CLOSED
```

Explanation:

- 
failureThreshold = 2, successThreshold = 1, timeout = 1000 ms.

- req1 success, remain CLOSED.

- req2 failure (1st), still below threshold, label CLOSED.

- req3 failure hits threshold, circuit opens after processing, label CLOSED.

- req4 arrives while OPEN (before timeout expires), label OPEN.

- req5 occurs after the timeout; circuit moves to HALF_OPEN before handling it, label HALF_OPEN. Success closes circuit.

- req6 processed in CLOSED.

Example 2

Input:

3
req1 100 success
req2 200 success
req3 300 failure
3
1
1000
```

Output:

CLOSED
CLOSED
CLOSED
```

Explanation:

- 
failureThreshold = 3, successThreshold = 1, timeout = 1000 ms.

- Three consecutive failures needed to open the circuit.

- Only one failure occurs; threshold never reached, all requests remain CLOSED.

Function Parameters

- 
requests (array of objects): Each object has id (string), timestamp (integer, ms), result ("success" or "failure")

- 
failureThreshold (number): Consecutive failures needed to open the circuit

- 
successThreshold (number): Consecutive successes in HALF_OPEN needed to close the circuit

- 
timeout (number): Milliseconds the circuit stays OPEN before transitioning to HALF_OPEN

Returns

An array of state strings (one per request): "CLOSED", "OPEN", or "HALF_OPEN".

Constraints

- 
1 ≤ n ≤ 1000

- 
1 ≤ failureThreshold, successThreshold ≤ 100

- 
1 ≤ timeout ≤ 10⁴ ms

- 
0 ≤ timestamp ≤ 10⁵; timestamps are non-decreasing

- 
1 ≤ length of request id ≤ 50; IDs are unique

Input Format for Custom Testing

Input from stdin will be processed as follows and passed to the function. 

The first line contains an integer n, the number of requests.

Each of the next n lines contains a string id, an integer timestamp, and a string result (either "success" or "failure"), all separated by spaces.

The next line contains an integer failureThreshold.

The next line contains an integer successThreshold.

The next line contains an integer timeout.

## Sample Input/Output

## Preview

Your backend relies on an unreliable third-party service. When it starts failin
