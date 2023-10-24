[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Y44jpg97)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12544748&assignment_repo_type=AssignmentRepo)
# Python-algorithmic_thinking-quicksort

Implement the quicksort presented in pseudo code below in Python in the `quicksort.py` file. Then run the `app.py` file to test your implementation. The output should be "Congratulations! No error detected.".

```
BEGIN QuickSort(list, low=0, high=-1)
  IF high == -1
    high = LENGTH OF list -1
  ENDIF
  IF low < high
    pi = Partition(list, low, high)
    QuickSort(list, low, pi - 1)
    QuickSort(list, pi + 1, high)
  ENDIF
END QuickSort

BEGIN Partition(list, low, high)
  pivot = list[high]  
  i = low - 1
  FOR j FROM low TO high
    IF list[j] < pivot
      i++
      SWAP list[i] AND list[j]
    ENDIF
  ENDFOR
  SWAP list[i + 1] AND LIST[high]
  RETURN i + 1
END Partition
```
Source: https://www.geeksforgeeks.org/quick-sort/
