'''

REFLECTION:
- What does the @app.route() decorator actually do?
It matches a url with a specific pattern, if the url matches that pattern, the handler function
attached to the app.route() will be executed.
- How does Flask know which function to call when a request arrives?
Because each function is attached to a specific pattern that that specific app.route holds. the function
that is executed is the one that contains the app.route pattern that matches the url
- What's the difference between route parameters (<name>) and query parameters (?key=value)?
route parameters are actually in the path of the url and required in order for the function to execute, they are
often passed in as arguments. query parameters are like variables inside a url, they are not necessary for the
function to execute.
- Why do we need to use request.get_json() for POST requests but request.args.get() for GET query parameters?
because with post you are actually creating something new and whatever you are posting needs to be converted to python
so the erver can work with it. with the get request, you are only retrieving data so you may need the arguments of the
request to get the data
- What happens if you try to access request.args outside of a request context?
the program will crash and cause a runtime error.
'''