# Loss function ---- categorical cross Entropy

'''
solving for x
log(logirithm)
e ** x = b
'''
import math

softmax_output = [0.7 , 0.1 , 0.2]

target_output  = [1, 0, 0]

loss = -(math.log(softmax_output[0]) * target_output[0] + 
        math.log(softmax_output[1]) * target_output[1] +
        math.log(softmax_output[2]) * target_output[2]  )

print(loss)

print(-math.log(softmax_output[0]))