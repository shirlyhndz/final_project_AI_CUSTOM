import unittest

from backend.cag import apply_context, context_keys
from backend.context_store import ContextStore


class StudentCagUnitTest(unittest.TestCase):
    def test_context_store_saves_and_retrieves_user_context(self):
        store = ContextStore()

        saved = store.save("jorge", "style", "explicar paso a paso")
        context = store.list_for_user("jorge")

        self.assertTrue(saved)
        self.assertIn({"key": "style", "value": "explicar paso a paso"}, context)

    def test_context_store_updates_existing_key(self):
        store = ContextStore()

        store.save("jorge", "style", "respuesta corta")
        store.save("jorge", "style", "respuesta detallada")

        context = store.list_for_user("jorge")

        self.assertEqual(context, [{"key": "style", "value": "respuesta detallada"}])

    def test_apply_context_adds_context_to_answer(self):
        context_items = [{"key": "audience", "value": "explicar como principiante"}]

        answer = apply_context(
            "jorge",
            "Que es CAG?",
            "CAG usa contexto persistente.",
            context_items,
        )

        self.assertIn("principiante", answer.lower())
        self.assertIn("audience", context_keys(context_items))


if __name__ == "__main__":
    unittest.main()