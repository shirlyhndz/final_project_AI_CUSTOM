from backend.cag import apply_context, context_keys
from backend.knowledge import retrieve_snippets


def answer_question(user_id, question, context_items=None):
    snippets = retrieve_snippets(question)
    context_items = context_items or []

    if not snippets:
        base_answer = "No encontre informacion suficiente en la base de conocimiento del curso."
        answer = apply_context(user_id, question, base_answer, context_items)

        return {
            "user_id": user_id,
            "answer": answer,
            "sources": [],
            "context_used": context_keys(context_items),
        }

    source_text = " ".join(item["content"] for item in snippets)
    base_answer = f"Segun la base de conocimiento del curso: {source_text}"
    answer = apply_context(user_id, question, base_answer, context_items)

    return {
        "user_id": user_id,
        "answer": answer,
        "sources": [item["id"] for item in snippets],
        "context_used": context_keys(context_items),
    }