from lib_types import *

def showAirstream(airstream: Airstream):
  if airstream == Airstream.PULMONIC_EGRESSIVE:
    return "Pulmonic Egressive"
  elif airstream == Airstream.CLICK:
    return "Click"
  elif airstream== Airstream.IMPLOSIVE:
    return "Implosive"
  else:
    return "(ERROR: undefined Airstream:" + airstream


answer = Consonant(VocalFolds.VOICED,
                   Place.BILABIAL,
                   Manner.PLOSIVE,
                   Airstream.PULMONIC_EGRESSIVE)



print(answer)

print("Program terminated normally")
