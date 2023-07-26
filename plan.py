import prompts
from openai_api import OpenAI_API, MODEL
from utils import Colors, print_color, str_parse_json
# reformat the goal into a plan
import openai

api = OpenAI_API(model=MODEL)

class Curriculum:
    def __init__(self, curriculum: list[str]) -> None:
        self.curriculum = curriculum

    @classmethod
    def from_query(cls, query):
        print_color("= Init curriculum start ==========", Colors.MAGENTA)
        print(prompts.INITIAL_GOAL.format(query=query))
        response = api.chatgpt(prompts.INITIAL_GOAL.format(query=query))
        print_color("[Curriculum]: ", Colors.MAGENTA, end="")
        parsed = str_parse_json(response)
        if not parsed:
            parsed = []
        return cls(response)

    def __str__(self) -> str:
        return "\n".join(["- " + c for c in self.curriculum])


def clarify_query(query: str):
    messages = [
        {"role":"system", "content": prompts.CLARIFY_QUERY},
        {"role":"user", "content": f"query: {query}"}
    ]
    print_color("= Clarify query start ==========", Colors.MAGENTA)
    while True:
        response = openai.ChatCompletion.create(
            model=MODEL, messages=messages).choices[0].message.content 
        messages.append({"role":"assistant", "content": response})

        print_color("[AI]: ", Colors.GREEN, end="")
        print(response)
        
        print_color("[Human]: ", Colors.RED, end="")
        inp = input()
        messages.append({"role":"user", "content": inp})
        if "q" == inp:
            break
        
        # check break
        response = openai.ChatCompletion.create(
            model=MODEL, messages=messages + [{"role":"user", "content": prompts.CHECK_CLARIFY_END}]).choices[0].message.content 
        print_color(f"Checking break: {response}", Colors.GREY)
        if "YES" in response:
            break
    
    messages.append({"role":"assistant", "content":"[COMPLETE]"})
    messages.append({"role":"user", "content": f"Clarify the original query `{query}` based on the conversation so it is more specific. new_query:"})
    response = openai.ChatCompletion.create(
        model=MODEL, messages=messages).choices[0].message.content 
    print_color("[Normalized query]: ", Colors.MAGENTA, end="")
    print(response)
    return response
