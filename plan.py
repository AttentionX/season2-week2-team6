import prompts
from openai_api import OpenAI_API
from utils import Colors, print_color
# reformat the goal into a plan
import openai

def clarify_query(query: str):
    messages = [
        {"role":"system", "content": prompts.CLARIFY_QUERY},
        {"role":"user", "content": f"query: {query}"}
    ]
    print_color("= Clarify query start ==========", Colors.MAGENTA)
    while True:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages).choices[0].message.content 
        messages.append({"role":"assistant", "content": response})

        print_color("[AI]: ", Colors.GREEN, end="")
        print(response)
        
        print_color("[Human]: ", Colors.RED, end="")
        inp = input()
        messages.append({"role":"user", "content": inp})
        
        # check break
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages + [{"role":"user", "content": prompts.CHECK_CLARIFY_END}]).choices[0].message.content 
        print_color(f"Checking break: {response}", Colors.GREY)
        if "YES" in response:
            break

    messages.append({"role":"user", "content": f"Rephrase the original query:```{query}```"})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages).choices[0].message.content 
    print_color("[Normalized query]: ", Colors.MAGENTA, end="")
    print(response)
    return response
