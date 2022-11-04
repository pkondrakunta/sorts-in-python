import time

class Sort:
    def __init__(self) -> None:
        pass

    def bubbleSort(self, data: list) -> None:
        tic = time.perf_counter()
        swapped = False
        N = len(data)
        for i in range(N-1):
            for j in range(N-i-1):
                if(data[j]>data[j+1]): 
                    swapped = True
                    data[j+1],data[j] = data[j], data[j+1]
            if not swapped:
                toc = time.perf_counter()
                print("BubbleSort time: ", toc-tic)
                return
        toc = time.perf_counter()
        print("BubbleSort time: ", toc-tic)


    def insertionSort(self, data: list) -> None:
        tic = time.perf_counter()

        N = len(data)
        for i in range(1, N):    
            key = data[i]
            j = i-1
            while j >=0 and key < data[j] :
                    data[j+1] = data[j]
                    j -= 1
            data[j+1] = key
        
        toc = time.perf_counter()
        print("InsertionSort time: ", toc-tic)

    def quickSort(self, data: list) -> None:
        pass

    def mergeSort(self, data: list) -> None:
        pass

    def runAll(self):
        test_data = list([3,6,7,8,1,2,5,4])

        self.bubbleSort(test_data)
        self.insertionSort(test_data)
        self.quickSort(test_data)
        self.mergeSort(test_data)
        print(test_data)
        
if __name__ == "__main__":
    sort = Sort()
    sort.runAll()