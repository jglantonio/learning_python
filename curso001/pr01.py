#!/usr/bin/env python3
# Now it's your turn to work with variables. The comments in this quiz (the lines 
# that begin with #) have instructions for creating and modifying variables. 
# After each comment write a line of code that implements the instruction.
# Note that this code uses scientific notation to define large numbers. 
# 4.445e8 is equal to 4.445 * 10 ** 8 which is equal to 444500000.0.

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6
# decrease the rainfall variable by 10% to account for runoff
descuento = 5e6*0.1;
rainfall = 5e6 - descuento;
# add the rainfall variable to the reservoir_volume variable
reservoir_volume = rainfall + reservoir_volume;
# increase reservoir_volume by 5% to account for stormwater that flows
incremento = reservoir_volume*.05;
reservoir_volume = incremento + reservoir_volume;
# into the reservoir in the days following the storm
print(reservoir_volume);
# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume = reservoir_volume - (reservoir_volume*.05) ;
# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume = reservoir_volume - 2.5e5;
# print the new value of the reservoir_volume variable
print(reservoir_volume)
