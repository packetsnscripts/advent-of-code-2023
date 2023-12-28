
def get_number_of_ways (time: int, distance:int):
    ways = 0
    for t in range(time + 1):
        travelled = t * (time - t)
        # print(f" in {t} seconds we travelled {travelled} millimeters")
        if travelled > distance:
            ways += 1
    
    return ways

# get_number_of_ways(7,5)
def main ():
    mor = 1
    times = [38,94,79,70]
    distances = [241,1549,1074,1091]
    for n in range(len(times)):
        mor *= get_number_of_ways(time=times[n], distance=distances[n])
        
    print(f"Part1 : marging of error = {mor}")
        
    print(f"Part 2: margin of error for 71530ms = {get_number_of_ways(time=71530, distance=940200)}")
main()