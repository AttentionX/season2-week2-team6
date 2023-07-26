PARAPHRASE_QUERY = """
You are an AI agent with access to the internet. You goal is to utilize the web to answer questions asked by users.
The user asked a question: {query}

Rephrase the query into a more specific question that can be answered by the web.

output format: 
```
{
    "query": <rephrased query>,
}
```
"""

CLARIFY_QUERY = """
Your goal is to clarify the user's query to be as specific as possible.
A user's question often lacks context, is vague, or can be misleading. For example, a user query may be '가성비 좋은 노트북', which is not very helpful. 

- You should ask clarifying questions to narrow down the request.
- Each question should be easy to answer and should only ask one thing at a time.
"""


INITIAL_GOAL = """
You are an AI agent with access to the internet. You goal is to utilize the web to answer questions asked by users.
The user asked a question: {query}

Plan the tasks that has to be done to fulfil the user's request.

You must follow the following criteria when plan:
1. 
2. Please be very specific about what information to search for, what websites to visit, and what information to extract.
"""