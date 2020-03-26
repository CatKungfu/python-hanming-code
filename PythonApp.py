#python3.0
import np

def hm_result(hm_code):
    # 列表x用来装汉明码距离
    x = []
    #print(len(hm_code))
    for i in range(len(hm_code)):
        xmat = np.mat(hm_code)
        for j in range(i+1,len(hm_code)):
            if i < len(hm_code)-1:
                smstr = np.nonzero(xmat[i] - xmat[i+1])
                x.append(np.shape(smstr[1])[0])
    #print(x)
    return min(x)
 
if __name__ == '__main__':
    # (15,11)汉明码
    hm_code = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0], 
               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0], 
               [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
               [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
               [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]]
    print('dmin='+str(hm_result(hm_code)))