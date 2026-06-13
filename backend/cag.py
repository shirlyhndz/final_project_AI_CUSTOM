"""Context-Augmented Generation helpers."""


def apply_context(user_id, question, base_answer, context_items):
    if not context_items:
        return base_answer

    context_text = "; ".join(
        f"{item['key']}: {item['value']}"
        for item in context_items
    )

    return (
        f"{base_answer}\n\n"
        f"Contexto CAG aplicado para el usuario {user_id}: {context_text}. "
        f"La respuesta fue ajustada tomando en cuenta ese contexto."
    )


def context_keys(context_items):
    return [item["key"] for item in context_items]