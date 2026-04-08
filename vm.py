class VM:
    def __init__(self, cpu):
        self.cpu = cpu

    def __repr__(self):
        return f"VM(cpu={self.cpu})"