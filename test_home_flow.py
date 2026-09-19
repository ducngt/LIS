import json

from boxes.lis_home_hero.box import LISHomeHeroBox
from wires.home_hero_wire.wire import HomeHeroWire


def main():
    box = LISHomeHeroBox()
    wire = HomeHeroWire()

    box_result = box.execute()
    wire_result = wire.transmit(box_result)

    print(json.dumps(
        wire_result,
        ensure_ascii=False,
        indent=2
    ))


if __name__ == "__main__":
    main()