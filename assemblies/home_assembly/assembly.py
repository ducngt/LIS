import json
from pathlib import Path

from boxes.lis_home_hero.box import LISHomeHeroBox
from wires.home_hero_wire.wire import HomeHeroWire


class HomeAssembly:
    ASSEMBLY_ID = "ASM-LIS-HOME-001"
    VERSION = "0.1.0"

    def __init__(self):
        self.base_path = Path(__file__).parent
        self.config_path = self.base_path / "assembly.json"

        self.hero_box = LISHomeHeroBox()
        self.hero_wire = HomeHeroWire()

    def load_config(self):
        with open(self.config_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def execute(self, context=None):
        if context is None:
            context = {}

        config = self.load_config()

        box_result = self.hero_box.execute(context=context)

        wire_result = self.hero_wire.transmit(box_result)

        if wire_result["status"] != "success":
            return {
                "assembly_id": self.ASSEMBLY_ID,
                "version": self.VERSION,
                "status": "error",
                "error": wire_result
            }

        return {
            "assembly_id": self.ASSEMBLY_ID,
            "version": self.VERSION,
            "status": "success",
            "assembly_name": config["assembly_name"],
            "component": config["execution"]["output_component"],
            "data": {
                "hero": wire_result["data"]
            }
        }


if __name__ == "__main__":
    assembly = HomeAssembly()
    result = assembly.execute()

    print(json.dumps(
        result,
        ensure_ascii=False,
        indent=2
    ))