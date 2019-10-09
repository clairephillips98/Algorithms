# claire phillips
# 20010910
# 15cvp2
# Oct 8 2019
import operator, math

class Subset:
    def __init__(self, elements, sum):
        self.elements = elements
        self.sum = sum


class BFI_Subset:

    def __init__(self, S, k, m):
        self.S = S
        self.k = k
        self.m = m
        BFI_Subset.BFI_Subset_Sum(self)


    def BFI_Subset_Sum(self):
        subsets = []
        subsets.append(Subset( [], 0))
        for i  in  range(len(self.S)):
            #print("beginning of outer for loop")
            new_subsets = []
            for old_u in subsets:
                new_u = Subset([self.S[i]], self.S[i]+ old_u.sum)
                for j in old_u.elements:
                    if j>0:
                        new_u.elements.append(j)
                        self.m += 1
                if new_u.sum == k:
                    elemStr = ', '.join(str(e) for e in new_u.elements)
                    print ("elements == {%s}, sum = %s" %(elemStr, new_u.sum))
                    BFI_Subset.endfunction(self)
                    return
                elif new_u.sum < k:
                    new_subsets.append(old_u)
                    new_subsets.append(new_u)
                else: new_subsets.append(old_u)
            subsets = new_subsets
            #print("length of subsets %s" %len(subsets))
        print("no subset sums to target value.")
        BFI_Subset.endfunction(self)

    def endfunction(self):
        #return str(self.m)
        print (self.m)

class HS_Subset:
    def __init__(self, S, k, n):
        self.S = S
        self.k = k
        self.n = n
        if (len(S) % 2) == 0:
            half = int(len(S)/2)
            Left = HS_Subset.Sums(self, 0, half)
            if Left != None:
                Right = HS_Subset.Sums(self, half, len(S))
        else:
            half =int((len(S)-1)/2)
            Left = HS_Subset.Sums(self, 0, half)
            if Left != None:
                Right = HS_Subset.Sums(self, half+1, len(S))
        if Left != None and Right != None:
            HS_Subset.HS_Subset_Sum(self, Left, Right)

    def Sums(self, begin, finish):
        allsets = []
        subsets = []
        subsets.append(Subset([], 0))
        for i in range(begin,finish):
            new_subsets = []
            for old_u in subsets:
                new_u = Subset([self.S[i]], self.S[i] + old_u.sum)
                for j in old_u.elements:
                    if j > 0:
                        new_u.elements.append(j)
                        self.n += 1
                if new_u.sum == k:
                    elemStr = ', '.join(str(e) for e in new_u.elements)
                    print("elements == {%s}, sum = %s" % (elemStr, new_u.sum))
                    HS_Subset.endfunction(self)
                    return None
                elif new_u.sum < k:
                    new_subsets.append(old_u)
                    new_subsets.append(new_u)
                else:
                    new_subsets.append(old_u)
            subsets = new_subsets
        return subsets

    def HS_Subset_Sum(self, Left, Right):
        Left.sort(key= operator.attrgetter('sum'))
        self.n += 3* len(Left)*math.log10(len(Left))
        Right.sort(key= operator.attrgetter('sum'))
        self.n += 3 * len(Left) * math.log10(len(Left))
        i = 0
        j = len(Right)-1
        while i <= len(Left)-1 and j >= 0:
            self.n += 1
            if Left[i].sum + Right[j].sum == self.k:
                elemStr1 = ', '.join(str(e) for e in Left[i].elements)
                elemStr2= ', '.join(str(e) for e in Right[j].elements)
                print("elements == {%s, %s}, sum = %s" % (elemStr1, elemStr2, self.k))
                HS_Subset.endfunction(self)
                return
            elif Left[i].sum + Right[j].sum < self.k:
                i += 1
            elif Left[i].sum + Right[j].sum > self.k:
                j -=1
        print("no subset sums to target value.")
        HS_Subset.endfunction(self)

    def endfunction(self):
        #return str(self.n)
        print (self.n)




if __name__ == "__main__":
    try:
        S = [13,1222, 1223, 1134, 123,293,234,576, 951,290,123,617, 894, 1292, 333, 316,1441, 1000, 3, 11, 23, 8, 9,90, 45, 64, 1234, 5, 406, 9, 10, 17, 100, 18, 22, 612, 2, 511, 13]    #subset we want to evaluate
        k = 350  # target value
        print(len(S))
        print ("Looking for: %s In the set: "%k)
        print(*S)
        m = 0
        n = 0
        print("HS")
        HS_Subset(S,k, n)
        print("BFI")
        BFI_Subset(S,k, m)
        #print ("BFI Subset Sum counter: %s" %m)
        #print("HS Subset Sum counter %s" %n)
    except:
        "Error with script"


