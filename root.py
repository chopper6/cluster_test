from mpi4py import MPI
import sys,os

comm         = MPI.COMM_WORLD
rank         = comm.Get_rank()
num_workers  = comm.Get_size()-1 #dont count master
arguments    = sys.argv # arguments should contain the /path/to/configs.txt

if rank == 0:    #ie is master
    with open ('root_mpi.log','w') as f:
        f.write('Im in dir '+str(os.getcwd())+', arguments = '+str(arguments)+ ', num_workers = '+str(num_workers))
        f.flush()
        f.close()
    import master    
    master.supervise (arguments, num_workers) # master distributes workload to workers, and harvests their dumps
    
else:
    import worker 
    worker.work (arguments, rank) # workers wait for workload from master, work, and finally dump their results for the master to harvest. repeat; a worker exits when master gives it an empty workload