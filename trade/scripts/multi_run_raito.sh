#!/bin/bash
echo "Bash version ${BASH_VERSION}..."
for i in {1..201..5}
  do 
     for j in `seq $((i+5)) 5 301`
    do 
     python prod.py stratergy.p.slow=$j stratergy.p.fast=$i run_id="${i}__${j}" hydra.output_subdir=null hydra/job_logging=disabled hydra/hydra_logging=disabled
    done
 done

# python prod.py stratergy.p.slow=20