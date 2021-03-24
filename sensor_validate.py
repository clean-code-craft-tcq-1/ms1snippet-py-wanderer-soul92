
def  in_permissible_range(value, nextValue, maxDelta):
  if nextValue - value > maxDelta:
    return False
  return True

def validate_reading(value,parameter):
    if value == None:
        return print("No Value given as input")
    else:
        validate_Para_reading(value,parameter)

        
def validate_Para_reading(values,parameter):
  threshold = { 'soc': 0.05, 'current': 0.1}
  last_but_one_reading = len(values) - 1
  for i in range(last_but_one_reading):
    if(not in_permissible_range(values[i], values[i + 1], threshold[parameter])):
      return False
  return True

"""def validate_current_reading(values):
  last_but_one_reading = len(values) - 1
  for i in range(last_but_one_reading):
    if(not _give_me_a_good_name(values[i], values[i + 1], 0.1)):
      return False
  return True """