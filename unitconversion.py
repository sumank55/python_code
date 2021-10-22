 # pseudo code Question number 2.
"""
    Store all the unit name in list
 
    Store the converted values of all units to inches in a list 

    Read the from unit and and convert to inches using above list

    Then converts units  from inches to requred output unit

"""

def convert(lenth,frm,to):
    all_unt = ['m','in','ft','yd','km']
    conv = [39.3701,1,12,36,39370.1]  # conversion in inches for all units

# conversion to inches for all from units 
    indx1 = all_unt.index(frm)
    conv1 = conv[indx1]
    stage_in = lenth*conv1

#conversion to final unit from inch
    indx2 = all_unt.index(to)
    print("indx2",indx2)
    conv2 = conv[indx2]
    final_conv = round((stage_in/conv2),2)
    
    print(str(final_conv) + ' ' + to )


print(convert(2,'m','yd'))