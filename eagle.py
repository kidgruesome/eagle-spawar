# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from eagle_http import *
from datetime import *
from decimal import *

#startdate = date(2000, 1, 1)
#today = date.today()

# Initialize Rainforest Gateway
eagle = eagle_http('tandrewjordon@yahoo.com', 'P@ssword1234', '002e35')

# CurrentSummation notification provides the total consumption to date as recorded by the meter
eagle.get_current_summation()
#eagle.get_instantaneous_demand()

# Store consumption values
sum = int(eagle.CurrentSummation.SummationDelivered,0)
mul = int(eagle.CurrentSummation.Multiplier,0)
div = int(eagle.CurrentSummation.Divisor,0)
sumPower = Decimal(sum)*Decimal(mul)/Decimal(div)
print sumPower