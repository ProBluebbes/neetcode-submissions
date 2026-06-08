class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s = set()
        n = len(position)

        sortedPos, sortedSpeed = zip(*sorted(zip(position, speed), reverse=True))

        lastStep = 0
        for i in range(n):
            steps = (target-sortedPos[i])/sortedSpeed[i]
            if steps > lastStep:
                s.add(steps)
                lastStep = steps

        return len(s)