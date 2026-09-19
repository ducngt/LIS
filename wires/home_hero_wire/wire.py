import json
from pathlib import Path


class HomeHeroWire:
    WIRE_ID = "SW-LIS-HOME-HERO-001"
    VERSION = "0.1.0"

    def __init__(self):
        self.base_path = Path(__file__).parent
        self.interface_path = self.base_path / "interface.json"

    def load_interface(self):
        with open(self.interface_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def validate(self, box_result):
        interface = self.load_interface()

        required_fields = interface["validation"]["required_fields"]

        if "data" not in box_result:
            return {
                "valid": False,
                "error": interface["validation"]["failure_code"],
                "message": "Missing 'data' in Box output."
            }

        data = box_result["data"]

        missing_fields = [
            field for field in required_fields
            if field not in data
        ]

        if missing_fields:
            return {
                "valid": False,
                "error": interface["validation"]["failure_code"],
                "message": "Missing required fields.",
                "missing_fields": missing_fields
            }

        return {
            "valid": True,
            "error": None,
            "message": "Capability output is valid."
        }

    def transmit(self, box_result):
        validation = self.validate(box_result)

        if not validation["valid"]:
            return {
                "wire_id": self.WIRE_ID,
                "version": self.VERSION,
                "status": "error",
                "validation": validation,
                "data": None
            }

        return {
            "wire_id": self.WIRE_ID,
            "version": self.VERSION,
            "status": "success",
            "validation": validation,
            "source": {
                "box_id": box_result.get("box_id"),
                "capability": box_result.get("capability"),
                "box_version": box_result.get("version")
            },
            "data": box_result["data"]
        }


if __name__ == "__main__":
    print(
        "HomeHeroWire is ready. "
        "It expects output from capability 'lis.home.hero'."
    )