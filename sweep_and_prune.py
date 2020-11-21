from typing import List, Tuple


def sweep_and_prune(bounds: List[Tuple]) -> List[List]:
    """Detect collisions between objects in 1-dimension using a sweep and prune algorithm"""

    collisions = [[False] * len(bounds) for _ in range(len(bounds))]

    l = []
    for i, x in enumerate(bounds):
        l.append((x[0], "s", i))
        l.append((x[1], "e", i))
    l.sort()

    active_particles = set()
    for t in l:
        if t[1] == "s":
            active_particles.add(t[2])
            for p in active_particles:
                collisions[p][t[2]] = collisions[t[2]][p] = True
        elif t[1] == "e":
            active_particles.remove(t[2])

    return collisions


if __name__ == "__main__":
    print(sweep_and_prune([(0, 5), (1, 2), (3, 4)]))
