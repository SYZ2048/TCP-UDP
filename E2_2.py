import time
import random

def monte_carlo(total_points):
    time_start=time.time()
    """ 圆中点的个数除以总点数即为圆周率
    Args:
         total_points: 生成点总个数
    Returns:
         pi,以list形式返回所有的x和y点
    """
    # 1：定义圆中点个数的计数器与点容器
    num_circle_points = 0
    # 2：生成total_points个随机点
    for _ in range(total_points):
        # 3：在长宽均为1的矩形内生成随机点（x，y）
        rand_x = random.uniform(0, 1)
        rand_y = random.uniform(0, 1)
        # 4：判断随机点是否在圆内，如果在则圆中点个数计数器加1
        if (rand_x ** 2+rand_y ** 2) <= 1:
            num_circle_points += 1

    # 5：根据圆中点个数与总点数的比值，即得到圆周率
    pi = 4 * float(num_circle_points) / float(total_points)
    time_end=time.time()
    print('time=',time_end-time_start,'s  ')
    return pi


point = [10000, 100000,1000000,10000000,100000000,1000000000]
for i in point:
    for j in range(0,5):
        print("第",j+1,"次 N=",i," ",monte_carlo(i) )
    print("\n")
    
        