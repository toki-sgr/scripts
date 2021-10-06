
def string_list(list):
    return map(lambda x: str(x), list)

def output_route(route, expand_length=10):
    if route and type(route) == list:
        start = route[0]
        length = len(route)
        end = route[-1]
        convergence_flag = 1
        if end != 1:
            convergence_flag = 0
        
        if length > expand_length:
            expand_length_a = int(expand_length / 2)
            expand_length_b = expand_length - expand_length_a
            a = route[:expand_length_a]
            b = route[-expand_length_b:]
            output_string = "[{}], len: {}, {} ... {}, {}".format(start, length, " -> ".join(string_list(a)), " -> ".join(string_list(b)), "cv" if convergence_flag else "ucv")
        else:
            output_string = "[{}], len: {}, {}, {}".format(start, length, " -> ".join(string_list(route)), "cv" if convergence_flag else "ucv")
    return length, output_string


def syracuse_inf(start, max_depth=10000):
    time = 0
    route = list()
    num = start
    route.append(num)
    while time < max_depth and num != 1:
        # odd
        if num % 2 == 1:
            num = int(num * 3 + 1)
        else:
            num = int(num / 2)
        route.append(num)
        time += 1
    length, output_string = output_route(route)
    return length, output_string

if __name__ == "__main__":
    import time
    start_time = time.time()
    length_record = list()
    start_to_length = dict()

    for i in range(1, 10000):
        length, output_string = syracuse_inf(i)
        length_record.append(length)
        if length >= 1:
            print(output_string)
        
    cost = time.time() - start_time
    print("time_cost: {}".format(cost))
    avg_length = sum(length_record) / len(length_record)
    print("avg_length: {}".format(avg_length))