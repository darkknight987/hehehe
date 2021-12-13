def LCS(seq1,seq2):
    str1=len(seq1)
    str2=len(seq2)
    arr=[[0]*(str2+1) for i in range(str1+1)]

    for i in range(str1+1):
        for j in range(str2+1):
            if(i==0 or j==0) :
                arr[i][j] = 0
            elif(seq1[i-1]==seq2[j-1]):
                arr[i][j]=arr[i-1][j-1]+1
            else:
                arr[i][j]=max(arr[i-1][j],arr[i][j-1])
    return arr[str1][str2]

seq1=input("Enter First Sequence:")
seq2=input("Enter Second Sequence:")
print("Longest Common Subsequence is ",LCS(seq1,seq2))