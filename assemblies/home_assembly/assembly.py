import json
from pathlib import Path

from boxes.lis_home_hero.box import LISHomeHeroBox
from boxes.nute_identity.box import NUTEIdentityBox
from wires.home_hero_wire.wire import HomeHeroWire
from wires.nute_identity_wire.wire import NUTEIdentityWire


class HomeAssembly:
    ASSEMBLY_ID = "ASM-LIS-HOME-001"
    VERSION = "0.2.0"

    def __init__(self):
        self.base_path = Path(__file__).parent
        self.config_path = self.base_path / "assembly.json"

        self.hero_box = LISHomeHeroBox()
        self.hero_wire = HomeHeroWire()

        self.identity_box = NUTEIdentityBox()
        self.identity_wire = NUTEIdentityWire()

    def load_config(self):
        with open(self.config_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def execute(self, context=None):
        if context is None:
            context = {}

        config = self.load_config()

        # Execute Hero capability
        hero_box_result = self.hero_box.execute(context=context)
        hero_wire_result = self.hero_wire.transmit(hero_box_result)

        if hero_wire_result["status"] != "success":
            return {
                "assembly_id": self.ASSEMBLY_ID,
                "version": self.VERSION,
                "status": "error",
                "source": "home_hero_wire",
                "error": hero_wire_result
            }

        # Execute NUTE Identity capability
        identity_box_result = self.identity_box.execute(context=context)
        identity_wire_result = self.identity_wire.transmit(identity_box_result)

        if identity_wire_result["status"] != "success":
            return {
                "assembly_id": self.ASSEMBLY_ID,
                "version": self.VERSION,
                "status": "error",
                "source": "nute_identity_wire",
                "error": identity_wire_result
            }

        return {
            "assembly_id": self.ASSEMBLY_ID,
            "version": self.VERSION,
            "status": "success",
            "assembly_name": config["assembly_name"],
            "component": config["execution"]["output_component"],
            "data": {
                "identity": identity_wire_result["data"],
                "hero": hero_wire_result["data"]
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