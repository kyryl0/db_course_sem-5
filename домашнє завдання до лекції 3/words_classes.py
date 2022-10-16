class Words:

    id: object

    def __init__(self, id, word, struct, pos):
        self.id = id
        self.word = word
        self.struct = struct
        self.pos = pos

    @property
    def fullword(self):
        return '{} {}'.format(self.id, self.word)

    def __repr__(self):
        return "Word('{}', '{}', {}, {})".format(self.id, self.word, self.struct, self.pos)
