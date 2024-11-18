#!/bin/bash

#setup
OUT_DIR="jetson"

now=`date`

mkdir $OUT_DIR

PYTHON='python3'

APP="bzip2 lane person ferret"

PPI="ff tbb spar omp threads"

PATTERN="farm pipe-farm"

METRICS="-latency -throughput"

REPETITIONS="5"

MAX_THREADS=3

./spbench 'clean' -bench 'all'
./spbench 'update' -bench 'all'

for app in $APP
do
	
	bench=$app"_sequential" # build the name of a benchmark

	now=`date`
	echo "Repeating $bench $REPETITIONS times with single thread | $now"
	
	inputName=test

	log_file_name=$app"_seq_"$pattern".log"

	./spbench 'compile' -bench $bench -clean
	./spbench 'exec' -bench $bench -input $inputName -repeat $REPETITIONS $METRICS >> $OUT_DIR/$log_file_name # run

	LATENCY_SEQ="$(grep "Average latency" $OUT_DIR/$log_file_name | cut -d":" -f2)"
	LAT_STD_DEV_SEQ="$(grep "Latency std. dev." $OUT_DIR/$log_file_name | cut -d":" -f2)"
	THROUGHPUT_SEQ="$(grep "Average throughput" $OUT_DIR/$log_file_name | cut -d":" -f2)"
	THR_STD_DEV_SEQ="$(grep "Throughput std. dev." $OUT_DIR/$log_file_name | cut -d":" -f2)"
	EXEC_TIME_SEQ="$(grep "Average exec. time" $OUT_DIR/$log_file_name | cut -d":" -f2)"
	EXEC_TIME_DEV_SEQ="$(grep "Exec. time std. dev." $OUT_DIR/$log_file_name | cut -d":" -f2)"
	
	echo "-----------------------------------------------------------------------------------"
	
	for ppi in $PPI
	do
		for pattern in $PATTERN
		do
			
			if [ "$app" = "ferret" & "$pattern" = "farm"  ]; then
				continue
			fi

			bench=$app"_"$ppi"_"$pattern # build the name of a benchmark
			
			out_file_name=$bench'.dat'
			
			echo "Thread Average_latency Std_dev_latency Average_throughput Std_dev_throughput Average_exec_time Std_dev_exec_time" > $OUT_DIR/$out_file_name
			
			echo "0$LATENCY_SEQ$LAT_STD_DEV_SEQ$THROUGHPUT_SEQ$THR_STD_DEV_SEQ$EXEC_TIME_SEQ$EXEC_TIME_DEV_SEQ" >> $OUT_DIR/$out_file_name		

			./spbench 'compile' -bench $bench -clean

			for thread in $(seq 1 $MAX_THREADS) # number of replicas
			do
				export SPAR_NUM_WORKERS=$thread

				log_file_name=$app"_"$ppi"_"$pattern""_"$thread.log"

				now=`date`
				echo "Repeating $out_file_name $REPETITIONS times with $thread threads | $now"
				./spbench 'exec' -bench $bench -input $inputName -nthreads $thread -repeat $REPETITIONS $METRICS >> $OUT_DIR/$log_file_name # run

				LATENCY="$(grep "Average latency" $OUT_DIR/$log_file_name | cut -d":" -f2)"
				LAT_STD_DEV="$(grep "Latency std. dev." $OUT_DIR/$log_file_name | cut -d":" -f2)"
				THROUGHPUT="$(grep "Average throughput" $OUT_DIR/$log_file_name | cut -d":" -f2)"
				THR_STD_DEV="$(grep "Throughput std. dev." $OUT_DIR/$log_file_name | cut -d":" -f2)"
				EXEC_TIME="$(grep "Average exec. time" $OUT_DIR/$log_file_name | cut -d":" -f2)"
				EXEC_TIME_DEV="$(grep "Exec. time std. dev." $OUT_DIR/$log_file_name | cut -d":" -f2)"

				echo "$thread$LATENCY$LAT_STD_DEV$THROUGHPUT$THR_STD_DEV$EXEC_TIME$EXEC_TIME_DEV" >> $OUT_DIR/$out_file_name
				
				#rm $OUT_DIR/$log_file_name
				echo "-----------------------------------------------------------------------------------"
			done
		done
	done
done

exit;
