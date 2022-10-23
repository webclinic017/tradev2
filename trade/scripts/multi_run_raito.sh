#!/bin/bash
echo "Bash version ${BASH_VERSION}..."
i=1
# for j in `seq 7 1 10`
#     do 
#      python prod.py --config-name offline stratergy.p.slow=$j stratergy.p.fast=$i run_id="${i}__${j}" hydra.output_subdir=null hydra/job_logging=disabled hydra/hydra_logging=disabled 
#     done

SCRIPT_PATH=$(dirname $(realpath -s $0))

for i in {5..200..5}
  do 
   # for j in `seq $((i+5)) 5 200`
   for j in {5..200..5}
    do 
      for stock in $SCRIPT_PATH/../../data/nifty50_5year/*.csv
       do 
         symbol="${stock##*/}"
         # ::-4
         echo $i $j $stock ${symbol::-4}
         python prod.py --config-name offline stratergy.p.slow=$j stratergy.p.fast=$i run_id="daily${i}__${j}" hydra.output_subdir=null hydra/job_logging=disabled hydra/hydra_logging=disabled data_feed.filepath=$stock data_feed.symbol_name=${symbol::-4}
       done
    done
 done

# python prod.py stratergy.p.slow=20

# python prod.py --config-name offline stratergy.p.slow=$j stratergy.p.fast=$i run_id="${i}__${j}" data_feed.symbol_name=NIFTYBEESv2 data_feed.filepath=../../data/NIFTYBEES/data.csv broker.cash=100000 plot=True testing_param=golden_strat_test_full_vs/ratio hydra.output_subdir=null hydra/job_logging=disabled hydra/hydra_logging=disabled