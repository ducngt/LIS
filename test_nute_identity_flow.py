import json

from boxes.nute_identity.box import NUTEIdentityBox
from wires.nute_identity_wire.wire import NUTEIdentityWire


def main():
    box = NUTEIdentityBox()
    wire = NUTEIdentityWire()

    box_result = box.execute()
    wire_result = wire.transmit(box_result)

    print(json.dumps(
        wire_result,
        ensure_ascii=False,
        indent=2
    ))


if __name__ == "__main__":
    main()