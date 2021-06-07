def s(a,b):
    if a == b:
        return 1 
    return -1 

def needleman_wunsch(seq1, seq2):

    matrix = [[0] * len(seq2) for i in range(len(seq1))]
    # sets up m*n zero matrix 
    for i in range(len(seq1)):
        matrix[0][i]= -i  
        matrix[i][0]= -i
    # fill the matrix according to the penalty scheme
    for i in range(len(seq1)):
        for j in range(len(seq2)):
           matrix[i][j]=max(
                matrix[i - 1, j - 1] + s(seq1[i],seq2[j]),
                matrix[i - 1, j] - 1,
                matrix[i, j - 1] - 1
           )
    # back trace the matrix
    matched_sequence1=""
    matched_sequence2= ""
    while i < 0 or j < 0: 
        score_current = matrix[i][j]
        diagonal = matrix[i-1][j-1]
        up = matrix[i][j-1]
        left = matrix[i-1][j]
        # now we check how the current score was created 
        if score_current== diagonal + s(seq1[],seq2[]):
            matched_sequence1+=seq1[i]
            matched_sequence2+=seq2[j]
            i,j -=1
        
        elif score_current== up - 1 :
        
        elif score_current == left - 1 :





        
    return (matched_sequence1,matched_sequence2)

