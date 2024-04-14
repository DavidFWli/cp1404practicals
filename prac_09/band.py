class Band:
    def __init__(self, name, musicians):
        self.name = name
        self.musicians = musicians

    def play(self):
        print(self.name)
        for musician in self.musicians:
            if musician.instruments:
                print(f"{musician.name} is playing: {', '.join(str(inst) for inst in musician.instruments)}")
            else:
                print(f"{musician.name} needs an instrument!")


class Musician:
    def __init__(self, name, instruments=None):
        self.name = name
        self.instruments = instruments if instruments else []

    def add_instrument(self, instrument):
        self.instruments.append(instrument)


class Guitar:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.model} : ${self.price:.2f}"


class Bass:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.model} : ${self.price:.2f}"


# Example usage:
if __name__ == "__main__":
    nuno_guitar = Guitar("Washburn N4 (1990)", 2499.95)
    takamine_guitar = Guitar("Takamine acoustic (1986)", 1200.00)
    mouradian_bass = Bass("Mouradian CS-74 Bass (2009)", 1500.00)

    nuno = Musician("Nuno Bettencourt", [nuno_guitar, takamine_guitar])
    gary = Musician("Gary Cherone")
    pat = Musician("Pat Badger", [mouradian_bass])
    kevin = Musician("Kevin Figueiredo")

    extreme = Band("Extreme", [nuno, gary, pat, kevin])
    extreme.play()