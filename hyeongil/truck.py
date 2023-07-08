def solution(bridge_length, weight, truck_weights): # O(n)
    answer = 0
    
    inBridgeList = []
    outTimeList = []
    inBridgeWeightTmp = 0
    time = 0
    while True:
        time += 1
        
        if len(outTimeList) != 0 and time == outTimeList[0]:
            inBridgeWeightTmp -= inBridgeList.pop(0)
            outTimeList.pop(0)

        if len(truck_weights) != 0:
            if inBridgeWeightTmp < weight and inBridgeWeightTmp + truck_weights[0] <= weight:
                truck_weight = truck_weights.pop(0)
                inBridgeWeightTmp += truck_weight
                inBridgeList.append(truck_weight)
                outTimeList.append(time + bridge_length)
        else:
            if len(inBridgeList) == 0:
                answer = time
                break        

    return answer


dataSet = [[2, 10, [7, 4, 5, 6]], [100, 100, [10]], [100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]]

for i in range(len(dataSet)):
    inputData = dataSet[i]
    print(solution(inputData[0], inputData[1], inputData[2]))
