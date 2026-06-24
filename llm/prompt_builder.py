def build_context(results):

    return "\n\n".join(
        result["text"]
        for result in results
    )


def create_prompt(question, context):

    return f"""
You are an expert software engineer.

You are answering questions about a GitHub repository.

Use ONLY the provided code context.

Question:
{question}

Code Context:
{context}

Answer:
"""
