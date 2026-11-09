
"""
Lab 2.4 – Functional Tools Practice
-----------------------------------
Practice map(), filter() and zip(), and compare them with comprehensions.

IMPORTANT: map(), filter() and zip() do not return lists. They return
"lazy" objects. Wrap the result in list(...) before returning it.

Part A – functional style:
- item_totals(prices, quantities) -> list using map()
- filter_above(totals, threshold=30) -> list using filter()
- pair_up(prices, quantities) -> list of tuples using zip()

Part B – list comprehensions:
- item_totals_comp(prices, quantities) -> list
- filter_above_comp(totals, threshold=30) -> list

All functions keep the original order of items.

Examples:
>>> item_totals(PRICES, QUANTITIES)
[25.0, 49.5, 15.0, 66.9, 20.0]
>>> filter_above([25.0, 49.5, 15.0, 66.9, 20.0])
[49.5, 66.9]
>>> filter_above([5, 10, 15], threshold=8)
[10, 15]
>>> pair_up([1.5, 2.0], [3, 4])
[(1.5, 3), (2.0, 4)]
>>> item_totals_comp(PRICES, QUANTITIES) == item_totals(PRICES, QUANTITIES)
True
>>> filter_above_comp([5, 10, 15], threshold=8)
[10, 15]
>>> type(item_totals(PRICES, QUANTITIES))
<class 'list'>
"""

PRICES = [12.5, 9.9, 15.0, 22.3, 5.0]
QUANTITIES = [2, 5, 1, 3, 4]


# ---------- Part A: functional style ----------

def item_totals(prices: list[float], quantities: list[int]) -> list[float]:
    """Return price * quantity for each item, using map() and a lambda."""
    return list(map(lambda p, q: p * q, prices, quantities))


def filter_above(totals: list[float], threshold: float = 30) -> list[float]:
    """Return totals greater than threshold, using filter() and a lambda."""
    return list(filter(lambda total: total > threshold, totals))


def pair_up(prices: list[float], quantities: list[int]) -> list[tuple]:
    """Return a list of (price, quantity) tuples, using zip()."""
    return list(zip(prices, quantities))


# ---------- Part B: list comprehensions ----------

def item_totals_comp(prices: list[float], quantities: list[int]) -> list[float]:
    """Same as item_totals(), but with a list comprehension."""
    return [p * q for p, q in zip(prices, quantities)]


def filter_above_comp(totals: list[float], threshold: float = 30) -> list[float]:
    """Same as filter_above(), but with a list comprehension."""
    return [total for total in totals if total > threshold]


if __name__ == "__main__":
    totals = item_totals(PRICES, QUANTITIES)

    print(f"Totals: {totals}")
    print(f"Totals > 30: {filter_above(totals)}")
    print(f"Price-quantity pairs: {pair_up(PRICES, QUANTITIES)}")
    print(f"Totals (comprehension): {item_totals_comp(PRICES, QUANTITIES)}")
    print(f"Totals > 30 (comprehension): {filter_above_comp(totals)}")

