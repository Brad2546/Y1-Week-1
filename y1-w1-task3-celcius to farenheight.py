TempInC=38.4
def CelciusToFahrenheit(TempInC):
    TempInF = (TempInC * (9/5)) + 32
    return TempInF

if __name__ == "__main__":
    TempInF=CelciusToFahrenheit(TempInC)
    print("Temp in C: "+str(TempInC))
    print("Temp in F: "+str(TempInF))