"""In-memory context storage for the CAG module."""

from threading import RLock


class ContextStore:
    def __init__(self):
        self._items_by_user = {}
        self._lock = RLock()

    def save(self, user_id, key, value):
        with self._lock:
            user_context = self._items_by_user.setdefault(user_id, [])

            for item in user_context:
                if item["key"] == key:
                    item["value"] = value
                    return True

            user_context.append({"key": key, "value": value})
            return True

    def list_for_user(self, user_id):
        with self._lock:
            return list(self._items_by_user.get(user_id, []))