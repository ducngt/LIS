import json
from pathlib import Path


class NUTEIdentityBox:
    BOX_ID = "SBB-NUTE-IDENTITY-001"
    CAPABILITY = "lis.identity.nute"
    VERSION = "0.1.0"

    def __init__(self):
        self.base_path = Path(__file__).parent
        self.interface_path = self.base_path / "interface.json"

    def load_interface(self):
        with open(self.interface_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def execute(self, context=None):
        interface = self.load_interface()

        output = interface["defaults"].copy()

        if context is None:
            context = {}

        language = context.get("language", "vi")

        if language == "en":
            output["identity_label"] = output["institution_english_name"]

        return {
            "box_id": self.BOX_ID,
            "capability": self.CAPABILITY,
            "version": self.VERSION,
            "context": context,
            "data": output
        }


if __name__ == "__main__":
    box = NUTEIdentityBox()
    result = box.execute()

    print(json.dumps(
        result,
        ensure_ascii=False,
        indent=2
    ))