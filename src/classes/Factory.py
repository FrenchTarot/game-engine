from typing import Dict


class Factory:
    available_classes = None

    def from_json(self, dict: Dict):
        filtered = [
            class_
            for class_ in self.available_classes
            if class_.__name__.lower() == dict["type"].lower()
        ]

        if not len(filtered):
            raise BaseException(f"Class for {dict} not found")

        self._check_data(dict)

        return filtered[0]

    def _check_data(self, dict: Dict):
        pass
