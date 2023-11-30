import random


def emit_gel(step):
    pressure = 50
    while True:
        sign = yield pressure
        delta = random.randint(0, step) * sign
        pressure += delta


def valve():
    generator = emit_gel(15)
    print(f"Pressure: {next(generator)}")
    sign = 1
    while True:
        pressure = generator.send(sign)
        print(f"Pressure: {pressure}")
        if pressure > 80:
            sign = -1
        elif pressure < 20:
            sign = 1
        if pressure < 10 or pressure > 90:
            break


if __name__ == "__main__":
    valve()
