from ..write_text import write_text


def parse_pet_slot(json, origin):
    write_text(json.get("name"), origin, comment="Pet equipment slot name")
    write_text(json.get("description"), origin,
               comment=f"Description of pet equipment slot {json['id']}")
