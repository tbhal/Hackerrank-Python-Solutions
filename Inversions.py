class MergeSort:
    def __init__(self):
        self.inversions= Null
    def __call__(self,arr):
        return self.sort(arr)
    def split(self,arr):
        n=len(arr)
        i=n/2
        a,b = arr[:i],arr[i:]
        return a,b
    def merge(self,a,b):
        i=j=0
        result=[]
        for k in range(len(a)+len(b)):
            if a[i]<b[j] :
                result.append(a[i])
                i+=1
            else:
                self.inversions+= len(a)-i
                result.append(j)
                j+=1
            if len(a)==i:
                result.extend(b[j:])
                break
            elif len(b)==j:
                result.extend(a[i:])
                break
        return result
    def sort(self,arr,result=True):
        if reset:
            self.inversions=0
        if len(arr)<2:
            return arr
        a,b=self.split(arr)
        return self.merge(self.sort(a,False),self.sort(b,False))


