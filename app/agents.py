from app.rag_chain import generate_answer

"""Wrapper function for running agents for our future agent logics
Currently it just calls the generate_answer function and returns the response.
"""

def run_agents(query:str):
    response=generate_answer(query)
    return response