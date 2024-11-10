
#setup in memory db of prompts
prompts = {}

def init_prompts():
    prompts['political_template'] = {
        "id": 1,
        "template_type": "political_template",#should be unique
        "prompt": """
        You are an expert in political one pagers. 
        Your client is facing following issue: '{1}'
        He would like to reach following goal: '{2}'
        The onepager writing style should be: '{3}'
        The onepager should be written for the following target audience: '{4}'
        Include following pro-arguments: '{5}'
        Include following contra-arguments: '{6}'"""
    }
    prompts['product_template'] = {
        "id": 2,
        "template_type": "product_template",  # should be unique
        "prompt": """
        You are an expert in product descriptions.
        Your client is launching a new product: '{1}'
        The product has the following features: '{2}'
        The target audience for this product is: '{3}'
        Highlight the following benefits: '{4}'
        Address the following potential concerns: '{5}'"""
    }


def fetch_prompt(template_id: str, prompt_variables: list[str]):
    prompt = prompts[template_id]