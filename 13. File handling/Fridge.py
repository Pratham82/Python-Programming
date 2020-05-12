
from contextlib import closing

class RefrigeratorRaider():
    # Raid a refrigerator

    def open(self):
        print("Open Fridge door")
    
    def take(self,food):
        print(f"Finding {food}....")
        if food == 'deep fried pizza':
            raise RuntimeError("Health warning")
        print(f"Taking {food}")
    
    def close(self):
        print("Closing fridge door")

def raid(food):
    with closing(RefrigeratorRaider()) as r:
        r.open()
        r.take(food)
        # r.close()
            