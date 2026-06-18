#!/bin/bash
# Fast debug run: one theory index, one checkpoint (~few minutes)
set -e

SEED=42
BATCH_SIZE=10
ENV=rware:rware-img-3-tiny-2ag-v2
CHECKPOINTS_PATH=models
EXPLANATIONS=True
CURRENT_TIME="$(date +%Y%m%d%H%M%S)"

mkdir -p plots

for theory_index in 0
do
    for step in 1001000
    do
        echo "Quick run: step $step, index $theory_index"
        uv run python src/main.py --config=mappo --env-config=gymma with \
            env_args.time_limit=100 \
            seed=$SEED \
            current_time=$CURRENT_TIME \
            theory_index=$theory_index \
            explanations=$EXPLANATIONS \
            batch_size_run=$BATCH_SIZE \
            env_args.key=$ENV \
            t_max=1000000 \
            checkpoint_path=$CHECKPOINTS_PATH \
            load_step=$step \
            render=False \
            common_reward=False
    done
done
