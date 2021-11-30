import heapq
import sys
N = int(sys.stdin.readline())
leftp, rightp = [], []

for _ in range(N):
    num = int(sys.stdin.readline())
    if len(leftp) == len(rightp):
        heapq.heappush(leftp, (-num, num))
    else:
        heapq.heappush(rightp, (num, num))

    if rightp and leftp[0][1] > rightp[0][1]:
        leftv = heapq.heappop(leftp)[1]
        rightv = heapq.heappop(rightp)[1]
        heapq.heappush(rightp, (leftv, leftv))
        heapq.heappush(leftp, (-rightv, rightv))

    print(leftp[0][1])