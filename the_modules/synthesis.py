from typing import List

def generate_gpt_prompt(abstracts: List[str], theme: str) -> str:
    joined = "\n\n".join(abstracts)
    return f"""
    You are a scientific reviewer. The following abstracts relate to the topic: '{theme}'.

    Summarize the key findings, identify patterns or themes, highlight agreements and disagreements,
    note any gaps in knowledge, and suggest specific directions for future research.

    Abstracts:
    {joined}
    """