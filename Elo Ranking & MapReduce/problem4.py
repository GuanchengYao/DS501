from mrjob.job import MRJob
#-------------------------------------------------------------------------
'''
    Problem 4: 
    In this problem, you will use mapreduce framework to implement matrix multipication. 
    You could test the correctness of your code by typing `nosetests test4.py` in the terminal.
'''

#--------------------------
class MatMul(MRJob):
#--------------------------
    ''' 
        Given a matrix A and a matrix B, compute the product A*B = C
    '''

    #----------------------
    @staticmethod
    def parse_line(line):
        '''
            parse one line of text from the data file.
            Input:
                    line: one line of text of a data record
            return: 
                    matrix_name: 'A' or 'B' 
                    i: row index, an integer (note, the index starts from 1) 
                    j: column index (note, the index starts from 1) 
                    v: the value of the entry; 
                    nr: number of rows in the matrix C
                    nc: number of columns in the matrix C
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        matrix_name  = line.split(',')[0]
        i = int(line.split(',')[1])
        j = int(line.split(',')[2])
        v = float(line.split(',')[3])
        nr = int(line.split(',')[4])
        nc = int(line.split(',')[5])

        #########################################
        return matrix_name,i,j,v,nr,nc

    #----------------------
    def mapper(self, in_key, in_value):
        ''' 
            mapper function, which process a key-value pair in the data and generate intermediate key-value pair(s)
            Input:
                    in_key: the key of a data record (in this example, can be ignored)
                    in_value: the value of a data record, (in this example, it is a line of text string in the data file, check 'matrix.csv' for example)
            Yield: 
                    (out_key, out_value) :intermediate key-value pair(s). You need to design the format and meaning of the key-value pairs. These intermediate key-value pairs will be feed to reducers, after grouping all the values with a same key into a value list.
        '''
        
        # parse one line of text data
        matrix_name, i, j, v, nr, nc = self.parse_line(in_value)
        #########################################
        ## INSERT YOUR CODE HERE
        # generate output key-value pairs 
        if matrix_name == 'A':
            for c in range(1, nc + 1):
                yield (('C',i,c), (matrix_name,i,j,v))
        if matrix_name == 'B':
            for r in range(1, nr + 1):
                yield (('C',r,j), (matrix_name,i,j,v))

        #########################################

    #----------------------
    def reducer(self, in_key, in_values):
        ''' 
            reducer function, which processes a key and value list and produces output key-value pair(s)
            Input:
                    in_key: an intermediate key from the mapper
                    in_values: a list (generator) of values , which contains all the intermediate values with the same key (in_key) generated by all mappers
            Yield: 
                    (out_key, out_value) : output key-value pair(s). 
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        list_all = list(in_values)
        list1 = list_all[:len(list_all)//2]
        list2 = list_all[len(list_all)//2:]
        out_value = 0
        for k in range(len(list_all)//2):
            out_value += list1[k][3] * list2[k][3]
        yield (in_key, out_value)

        #########################################
