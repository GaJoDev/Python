### *My Notes:*

This is the markdown conversion of the jupyter notebook, this is a readable reference if no access to Jupyter Labs

**PROBLEM**

*Issue with the code outlined in the notebook for this session that needed to be fixed:*

```Python
elif event.type == "logout":
  machines[event.machine].remove(event.user)
```

*This was causing a `KeyError` when the cell generating the report was ran:*

```Python
-------------------------------------
KeyError                                  Traceback (most recent call last)
Cell In[46], line 1
----> 1 users = current_users(events)
      2 print(users)

Cell In[45], line 13, in current_users(events)
     11     machines[event.machine].add(event.user)
     12   elif event.type == "logout":
---> 13     machines[event.machine].remove(event.user)
     14 return machines

KeyError: 'chris'
```


*SOLUTION*

*Use `set.discard(element)` instead. Unlike `remove()`, `discard()` doesn't raise an error if the element is missing:*
```Python
elif event.type == "logout":
  machines[event.machine].discard(event.user)
```
**Practice Notebook - Putting It All Together**

Hello, coders! Below we have code similar to what we wrote in the last video. Go ahead and run the following cell that defines our get_event_date, current_users and generate_report methods.

```python
def get_event_date(event):
  return event.date

def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout":
      machines[event.machine].discard(event.user)
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))
```
No output should be generated from running the custom function definitions above. To check that our code is doing everything it's supposed to do, we need an Event class. The code in the next cell below initializes our Event class. Go ahead and run this cell next.

```python
class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user
```
Ok, we have an Event class that has a constructor and sets the necessary attributes. Next let's create some events and add them to a list by running the following cell.

```python
events = [
    Event("2020-01-21 12:45:56", "login", "myworkstation.local", "jordan"),
    Event("2020-01-22 15:53:42", "logout", "webserver.local", "jordan"),
    Event("2020-01-21 18:53:21", "login", "webserver.local", "lane"),
    Event("2020-01-22 10:25:34", "logout", "myworkstation.local", "jordan"),
    Event("2020-01-21 08:20:01", "login", "webserver.local", "jordan"),
    Event("2020-01-23 11:24:35", "logout", "mailserver.local", "chris"),
]
```
Now we've got a bunch of events. Let's feed these events into our custom_users function and see what happens.


`users = current_users(events)`

Output

```Python
-------------------------------------
KeyError                                  Traceback (most recent call last)
Cell In[46], line 1
----> 1 users = current_users(events)
      2 print(users)

Cell In[45], line 13, in current_users(events)
     11     machines[event.machine].add(event.user)
     12   elif event.type == "logout":
---> 13     machines[event.machine].remove(event.user)
     14 return machines

KeyError: 'chris'
```
 
The code in the previous cell produces an error message. This is because we have a user in our events list that was logged out of a machine he was not logged into. Do you see which user this is? Make edits to the first cell containing our custom function definitions to see if you can fix this error message. There may be more than one way to do so.

Remember when you have finished making your edits, rerun that cell as well as the cell that feeds the events list into our custom_users function to see whether the error message has been fixed. Once the error message has been cleared and you have correctly outputted a dictionary with machine names as keys, your custom functions are properly finished. Great!

*Code Updated:*

```Python
elif event.type == "logout":
  machines[event.machine].discard(event.user)
```

Now try generating the report by running the next cell.

`generate_report(users)`
```python
# webserver.local: lane
```    
Success, The error message has been cleared and the desired output is produced.

## Flow of the Code

### 1. **Event Objects Creation:**
   - The `Event` class is used to create a list of event objects. Each event has a date, type (login or logout), machine name, and user.
   - For example, the first event in the `events` list is:
     ```python
     Event('2020-01-21 12:45:46', 'login', 'myworkstation.local', 'jordan')
     ```
     This represents a login event for the user `jordan` on the machine `myworkstation.local` on January 21, 2020.

### 2. **Sorting Events:**
   - The `current_users` function is called with the `events` list.
   - The events are sorted by their date using the `get_event_date` function, which returns the `date` attribute of each event. This ensures that the events are processed in chronological order.

### 3. **Tracking Login/Logout Activity:**
   - The function then loops through the sorted events.
     - For each event, it checks whether the machine is already in the `machines` dictionary:
       - If the machine is not in the dictionary, a new entry for that machine is added with an empty set to track users.
     - If the event type is `"login"`, the user is added to the machine's set (i.e., the set of users currently logged in on that machine).
     - If the event type is `"logout"`, the user is removed from the machine's set.
       - **Note:** If a logout happens on a machine where the user isn't logged in, a `KeyError` would occur. To prevent this, `.discard()` should be used instead of `.remove()` because `.discard()` won’t raise an error if the user is not in the set.

### 4. **Generating the Report:**
   - After processing all events, the `generate_report` function is called with the `machines` dictionary, which now contains the status of users (whether they are logged in or not) for each machine.
   - It loops through each machine and its associated set of users.
   - If the set of users is not empty (i.e., there are users currently logged in), the function generates a comma-separated list of users and prints the machine name along with that list.

### 5. **Output:**
   - The expected output will display machines with active users:
     ```plaintext
     webserver.local: lane
     mailserver.local: chris
     ```
     - `myworkstation.local` is not printed because no users are logged in at the end (all login/logout events for `jordan` cancel out).

### 6. **Final State of the Data:**
   - After processing, the `machines` dictionary would look like:
     ```python
     {
       'webserver.local': {'lane'},  # Only 'lane' is logged in here
       'myworkstation.local': set(),  # No one is logged in here
       'mailserver.local': {'chris'},  # Only 'chris' is logged in here
     }
     ```

### Summary:
- The events are sorted by date.
- Then, for each event, the user’s login/logout activity is tracked by adding/removing them from the respective machine’s set.
- Finally, a report is generated by displaying only machines with users currently logged in.
