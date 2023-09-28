GroupSizes = [113,175,12]

def CalculateNoOfGroups(GroupSize):
    NoOfFullGroups = GroupSize // 24
    NoLeftOver = GroupSize % 24
    return NoOfFullGroups, NoLeftOver

if __name__ == "__main__":
    for CurrentGroupSize in GroupSizes:
        print("A class of",CurrentGroupSize,"Students would make...")
        NoOfFullGroups, NoLeftOver = CalculateNoOfGroups(CurrentGroupSize)
        print(NoOfFullGroups,"Full groups and leave",NoLeftOver,"students left over")
        print()