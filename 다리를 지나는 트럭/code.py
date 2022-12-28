def solution(bridge_length, weight, truck_weights):
    answer = 0
    i = 0
    bd = [0] * bridge_length
    nw = 0
    while True:
        # print(bd)
        if len(truck_weights) == 0:
            if sum(bd) == 0:
                return i
            else:
                return i + len(bd)
        nw -= bd.pop(0)
        if len(bd) + 1 <= bridge_length and weight >=  nw + truck_weights[0]:
            bd.append(truck_weights[0])
            nw += truck_weights[0]
            truck_weights = truck_weights[1:]
        else:
            bd.append(0)
        i += 1
    