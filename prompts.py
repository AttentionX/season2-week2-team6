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
Your goal is to clarify the user's query to be as specific as possible. You can ask one question at a time
A user's question often lacks context, is vague, or can be misleading. For example, a user query may be '가성비 좋은 노트북', which is not very helpful. 

- You should ask clarifying questions to narrow down the request.
- Each question should be easy to answer and should only ask one thing at a time.
"""

CHECK_CLARIFY_END = "If the original query is sufficiently clarified, or if the user wants to end the conversation say 'YES'. Otherwise say 'NO'."
INITIAL_GOAL = """
You are an AI agent with access to the internet. You goal is to utilize the web to answer questions asked by users.
The user asked a question: {query}

Plan the tasks that has to be done to fulfil the user's request.

You must consider the following background and criteria when planning:
1. You currently have control of a headless browser. 
2. You can visit a website with a known url, search google, click on linked pages and buttons, type text, scroll and view what is currently on the page and so on.
3. Please be very specific about what information to search for, what websites to visit, and what information to extract.

Plan format: output the plan as a json file.
```
[
    "STEP 1",
    "STEP 2",
    ...
]
```
"""

