MatchesPlayed = 609   # M
TimesBatted = 1014    # B
TimesNotOut = 162     # NO
NoOfRuns = 48426      # R

def CalculateBattingAve(MatchesPlayed, TimesBatted, TimesNotOut, NoOfRuns):
    NoOfCompletedInnings = TimesBatted - TimesNotOut
    BattingAve = NoOfRuns / NoOfCompletedInnings
    return BattingAve

if __name__ == "__main__":
    BattingAve = CalculateBattingAve(MatchesPlayed, TimesBatted, TimesNotOut, NoOfRuns)
    print(BattingAve)