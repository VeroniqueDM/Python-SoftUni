length_of_aquarium=int(input())
width_aq=int(input())
height_aq=int(input())
percentage_occupied=float(input())/100
volume_aq=length_of_aquarium*width_aq*height_aq
liters_total=volume_aq*0.001
liters_needed=liters_total*(1-percentage_occupied)
print(liters_needed)