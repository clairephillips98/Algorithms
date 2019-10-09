# claire phillips
# 20010910
# 15cvp2
# Oct 8 2019
class Subset:
    def __init__(self, elements, sum):
        self.elements = elements
        self.sum = sum


class BFI_Subset:

    def __init__(self, S, k):
        self.S = S
        self.k = k
        print("why")
        BFI_Subset.BFI_Subset_Sum(self)


    def BFI_Subset_Sum(self):
        subsets = []
        subsets.append(Subset( [], 0))
        print("here")
        print(len(self.S)-1)
        for i  in  range(len(self.S)):
            #print("beginning of outer for loop")
            new_subsets = []
            for old_u in subsets:
                new_u = Subset([self.S[i]], self.S[i]+ old_u.sum)
                for j in old_u.elements:
                    if j>0: new_u.elements.append(j)
                if new_u.sum == k:
                    elemStr = ', '.join(str(e) for e in new_u.elements)
                    print ("elements == {%s}, sum = %s" %(elemStr, new_u.sum))
                    return
                elif new_u.sum < k:
                    new_subsets.append(old_u)
                    new_subsets.append(new_u)
                else: new_subsets.append(old_u)
            subsets = new_subsets
            #print("length of subsets %s" %len(subsets))
        print("no subset sums to target value.")

class HS_Subset

if __name__ == "__main__":
    #try:
        S = [12, 2, 3, 4, 5, 6]    #subset we want to evaluate
        k = 9  # target value
        print (*S)
        BFI_Subset(S,k)
    #except:
        "Error with script"


