class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)


clock = Clock()
clock.id = "00123"
clock.price = 19.99
print(f"ID:{clock.id}, price:{clock.price}")
clock.ring()
