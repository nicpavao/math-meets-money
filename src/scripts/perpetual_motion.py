import numpy as np
import matplotlib.pyplot as plt

class BusinessCycle:
    def __init__(self, inflation=2.0, unemployment=4.0, interest_rate=5.0):
        self.inflation, self.unemployment, self.interest_rate = inflation, unemployment, interest_rate
        self.time, self.history = 0, {"time": [], "inflation": [], "unemployment": [], "interest_rate": []}

    def step(self, dt=0.1):
        self.time += dt
        self.inflation += np.sin(self.time / 8) * 0.1 + np.random.normal(0, 0.05)
        self.unemployment += np.sin(self.time / 9 + np.pi / 2) * 0.1 + np.random.normal(0, 0.05)
        self.interest_rate += np.sin(self.time / 7 + np.pi) * 0.1 + np.random.normal(0, 0.05)
        for k in self.history: self.history[k].append(getattr(self, k))

    def shock(self, delta): 
        self.interest_rate += delta
        print(f"🚨 Fed action: Rate adjusted by {delta:.2f}%. Now: {self.interest_rate:.2f}%")

    def simulate(self, steps=300, dt=0.1):
        for _ in range(steps): self.step(dt)

    def plot(self):
        plt.figure(figsize=(10, 6))
        for k, c in zip(["inflation", "unemployment", "interest_rate"], ["red", "blue", "green"]):
            plt.plot(self.history["time"], self.history[k], label=k.title(), color=c)
        plt.xlabel("Time"), plt.ylabel("Levels"), plt.title("Business Cycle"), plt.legend(), plt.grid(), plt.show()

economy = BusinessCycle()
economy.simulate(100)
economy.shock(-0.50)
economy.simulate(200)
economy.plot()
