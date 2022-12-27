from collections import deque
from dataclasses import dataclass

import numpy as np

PORT = 0
WEIGHT = 1


@dataclass
class Moves:
    port: int
    load: int


class Solution:
    def boxDelivering(
        self, boxes: list[list[int]], portsCount: int, maxBoxes: int, maxWeight: int
    ) -> int:
        return self.box_delivery_numpy(boxes, portsCount, maxBoxes, maxWeight)

    def box_delivery_numpy(
        self, boxes: list[list[int]], portsCount: int, maxBoxes: int, maxWeight: int
    ) -> int:
        # initialize
        b = np.array(boxes)
        n = b.shape[0]
        cum_weight = b[:, WEIGHT].cumsum()
        min_trip_moves = np.zeros((n + 1,), dtype=np.int)
        port_change = np.zeros((n,), dtype=np.int)
        port_change[:-1] = np.where(b[:-1, PORT] == b[1:, PORT], 0, 1)

        # last trip
        tail = b[-maxBoxes:, WEIGHT][::-1].cumsum()
        last_trip_start = n - np.searchsorted(tail, maxWeight, side="right")
        min_trip_moves[last_trip_start:] = 2

        # iterate before last trip
        for i in range(last_trip_start - 1, -1, -1):
            prev_cum_weight = cum_weight[i - 1] if i > 0 else 0
            trip_weights = cum_weight[i : i + maxBoxes] - prev_cum_weight
            max_trip_len = np.searchsorted(trip_weights, maxWeight, side="right")
            min_trip_len = np.searchsorted(
                min_trip_moves[i + 1 : max_trip_len],
                min_trip_moves[i + max_trip_len] + 1,
            )
            moves_after_trip = min_trip_moves[
                i + 1 + min_trip_len : i + 1 + max_trip_len
            ]
            moves_for_trip = 2 - port_change[i + min_trip_len : i + max_trip_len]
            trip_moves = moves_for_trip + moves_after_trip
            min_trip_moves[i] = trip_moves.min()

        return min_trip_moves[0] + port_change.sum()

    def box_delivery_queue(
        self, boxes: list[list[int]], portsCount: int, maxBoxes: int, maxWeight: int
    ) -> int:
        moves: deque[Moves] = deque(Moves(0, 1))
        return 0
