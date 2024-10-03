import random
import time
import plotly.express as px



def generate_random_int_lists(sizes_of_lists):
    """
        generates a bunch of random lists of integers

        params:
            sizes_of_lists: a list of integers representing the sizes of lists
                that you want. So [10,20,30] would indicate you want one list of
                size 10, one of size 20, and one of size 30
        
        return: a list of lists of random ints. Each list has size specified by sizes_of_lists
    """
    random_lists = []
    
    #for each list size we want to try, generate a random list of ints of that size
    for n in sizes_of_lists:
        print("Generating a random integer list of size",n)
        curr_random_list = [random.randint(1,1000000) for i in range(n)]
        random_lists.append(curr_random_list)
    
    return random_lists


def time_list_operation(input_list,num_experiment_repetitions):
    """
        runs a list operation timing experiment on copies of a list

        params:
            input_list: the list you want to run the experiment on
            list_operation: the name of a function that takes a list as an argument
            num_experiment_repetitions: the number of times you want to run the list_operation 
        
        return: the number of seconds it took to run the operation num_experiment_repetitions times
    """
    #run several repetitions of each test to average out
    #outside influences on run times
    experiment_run_time = 0
    for i in range(num_experiment_repetitions):
        
        #using a copy of the list each time in case the
        #experiment changes the list from one run to the next
        test_list_copy = input_list[:]
        
        start = time.time()

        ### BEGIN CODE BEING TIMED
        # uncomment these one operation at a time (they're sectioned off by comments) to test them

        0 in test_list_copy  #testing the built-in search operator
        
        #random_index = random.randint(0,len(test_list_copy)-1)
        #x = test_list_copy[random_index]  #testing list access

        ### END CODE  BEING TIMED

        end = time.time()
        
        #summing up the run times over all repetitions for this experiment
        experiment_run_time += (end-start)

    return experiment_run_time


def run_list_op_timing_experiments(sizes_of_lists,num_experiment_repetitions):
    """
        runs a list operation timing experiment on random lists of specific sizes

        params:
            sizes_of_lists: the sizes of the lists you want to run the experiments on
            list_operation: the name of a function that takes a list as an argument
            num_experiment_repetitions: the number of times you want to run the list_operation 
        
        return: a list containing the number of seconds it took to run the list operation 
            num_experiment_repetitions times for each size given in sizes_of_lists
    """
    test_lists = generate_random_int_lists(sizes_of_lists)

    #run the experiment for each list size
    experiment_run_times = []
    for test_list in test_lists:
        print("Running experiment on a list of size",len(test_list))
        current_experiment_run_time = time_list_operation(test_list,num_experiment_repetitions)
        experiment_run_times.append(current_experiment_run_time)

    return experiment_run_times

    
def plot_results(sizes_of_lists,experiment_run_times):
    """
        creates a scatter plot in Plotly for the timing experiment

        params:
            sizes_of_lists: the sizes of the lists that experiments were run on
            experiment_run_times: the number of seconds each experument took
        
        return: None

        side effect: A plotly figure is shown
    """
    exp_plot = { "n": sizes_of_lists,
                 "Experiment run times" : experiment_run_times
                 }
    fig = px.scatter(exp_plot,x="n",y="Experiment run times")
    fig.show()  

def display_results(sizes_of_lists,experiment_run_times):
    """
        prints results for the timing experiment

        params:
            sizes_of_lists: the sizes of the lists that experiments were run on
            experiment_run_times: the number of seconds each experument took
        
        return: None
    """
    for i in range(len(sizes_of_lists)):
        print("List size:",sizes_of_lists[i],", Expriment run time:",experiment_run_times[i],"seconds")


list_sizes = range(100000,1000001,100000)
results = run_list_op_timing_experiments(list_sizes,20)
plot_results(list_sizes,results)
display_results(list_sizes,results)