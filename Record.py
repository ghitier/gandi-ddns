from RecordType import RecordType


class Record:
    def __init__(self, type: RecordType, ttl: int, name: str, values: list):
        self.type = type
        self.ttl = ttl
        self.name = name
        self.value = values[0] if len(values) > 0 else None

    def update_ip(self, value: str):
        self.value = value
        return self

    def to_dict(self):
        return {
            'rrset_type': self.type,
            'rrset_ttl': self.ttl,
            'rrset_name': self.name,
            'rrset_values': [self.value]
        }

    def __str__(self):
        return self.type + '\t' + str(self.ttl) + '\t' + self.name + '\t' + self.value
