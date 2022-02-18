#!/bin/bash
echo "Bash version ${BASH_VERSION}..."
# i=11
# for j in `seq 86 5 301`
#     do 
#      python prod.py --config-name offline stratergy.p.slow=$j stratergy.p.fast=$i run_id="${i}__${j}" hydra.output_subdir=null hydra/job_logging=disabled hydra/hydra_logging=disabled 
#     done

for i in {1..201..20}
  do 
     for j in `seq $((i+5)) 20 301`
    do 
     python prod.py --config-name offline stratergy.p.slow=$j stratergy.p.fast=$i run_id="${i}__${j}" data_feed.symbol_name=NIFTYBEESv2 data_feed.filepath=../../data/NIFTYBEES/data.csv broker.cash=100000 plot=True testing_param=golden_strat_test_full_vs/ratio hydra.output_subdir=null hydra/job_logging=disabled hydra/hydra_logging=disabled
    done
 done

# python prod.py stratergy.p.slow=20