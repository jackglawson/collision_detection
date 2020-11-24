from sweep_and_prune import sweep_and_prune
from dataclasses import dataclass
from typing import List
from math import sqrt


@dataclass(frozen=True)
class Ball:
    radius: float
    x: float
    y: float
    z: float


def potentially_colliding(balls: List[Ball]):
    """
    Generate a list of balls which could potentially intersect.
    Two balls potentially intersect iff their bounding cubes intersect.
    """

    x_bounds = [(b.x - b.radius, b.x + b.radius) for b in balls]
    y_bounds = [(b.y - b.radius, b.y + b.radius) for b in balls]
    z_bounds = [(b.z - b.radius, b.z + b.radius) for b in balls]

    x_collisions = sweep_and_prune(x_bounds)
    y_collisions = sweep_and_prune(y_bounds)
    z_collisions = sweep_and_prune(z_bounds)

    potentially_colliding_pairs = []
    # This can be optimised
    for i in range(len(balls)):
        for j in range(i+1, len(balls)):
            if x_collisions[i][j] and y_collisions[i][j] and z_collisions[i][j]:
                potentially_colliding_pairs.append((i, j))

    return potentially_colliding_pairs


def check_collision(ball1: Ball, ball2: Ball) -> bool:
    """Check if two balls actually collide"""
    d = sqrt((ball1.x - ball2.x)**2 + (ball1.y - ball2.y)**2 + (ball1.z - ball2.z)**2)
    return d < (ball1.radius + ball2.radius)


def colliding(balls: List[Ball]):
    return [p for p in potentially_colliding(balls) if check_collision(balls[p[0]], balls[p[1]])]


if __name__ == "__main__":
    balls = [Ball(10, 0, 0, 0),
             Ball(2, 11, 0, 0),
             Ball(1, 2, 0, 0)]

    colliding_pairs = colliding(balls)
    for i, j in colliding_pairs:
        print(f"Balls {i} and {j} are colliding")
