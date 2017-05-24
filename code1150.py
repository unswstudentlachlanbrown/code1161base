pointsAccepted = []
pointGrid = zip(range(len(pointCurvatures)), pointCurvatures, pointLocations)
while len(pointsAccepted) < pointsNeeded:
    largestFitness = 0
    for point in pointGrid:
        tempFitness = fitnessTest(point, pointsAccepted, pointsNeeded)
        if tempFitness > largestFitness:
            largestFitness = tempFitness
            bestPoint = point
    pointsAccepted.append(bestPoint)
    pointGrid.remove(bestPoint[0])


def fitnessTest(point, pointsAccepted, pointsNeeded):
    distanceImportance = sqrt((1-(abs(len(pointsAccepted)-1))/pointsNeeded)/2)
    if len(pointsAccepted) == 0:
        return point[1]
    elif len(pointsAccepted) == 1:
        return distance(point, pointsAccepted[0])*distanceImportance*point[1]
    elif len(pointsAccepted) == 2:
        d1 = distance(point, pointsAccepted[0])
        d2 = distance(point, pointsAccepted[1])
        return (sqrt(d1) + sqrt(d2))*distanceImportance*point[1]
    else:
        closestPoints = []
        for setPoint in pointsAccepted:
            if len(closestPoints) <= 3:
                closestPoints.append(setPoint)
            else:
                count = -1
                for closePoint in closestPoints:
                    count += 1
                    if distance(point, closePoint) < distance(point, setPoint):
                        closestPoints.remove(count)
                        closestPoints.append(setPoint)
                        break
        d1 = distance(point, pointsAccepted[0])
        d2 = distance(point, pointsAccepted[1])
        d3 = distance(point, pointsAccepted[2])
        return (sqrt(d1) + sqrt(d2) + sqrt(d3))*distanceImportance*point[1]


def distance(point1, point2):
    return sqrt((point1[2].X - point2[2].X])^2 + (point1[2].Y - point2[2].Y])^2)
