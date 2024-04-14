class Band:
    def __init__(self, name, musicians):
        self.name = name
        self.musicians = musicians

    def play(self):
        print(f"band ({type(self).__name__})")
        print(f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})")
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

    def __str__(self):
        return f"{self.name} ({', '.join(str(inst) for inst in self.instruments)})"


class Instrument:
    def __init__(self, name, model, year, price):
        self.name = name
        self.model = model
        self.year = year
        self.price = price

    def __str__(self):
        return f"{self.model} ({self.year}) : ${self.price:,.2f}"


# Example usage:
if __name__ == "__main__":
    nuno_instruments = [Instrument("Guitar", "Washburn N4", 1990, 2499.95),
                        Instrument("Guitar", "Takamine acoustic", 1986, 1200.00)]
    gary_instruments = []
    pat_instruments = [Instrument("Bass", "Mouradian CS-74", 2009, 1500.00)]
    kevin_instruments = []

    nuno = Musician("Nuno Bettencourt", nuno_instruments)
    gary = Musician("Gary Cherone", gary_instruments)
    pat = Musician("Pat Badger", pat_instruments)
    kevin = Musician("Kevin Figueiredo", kevin_instruments)

    extreme = Band("Extreme", [nuno, gary, pat, kevin])
    extreme.play()